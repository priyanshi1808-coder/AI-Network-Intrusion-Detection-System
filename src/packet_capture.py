# from scapy.all import sniff
# def packet_callback(packet):
#     print(packet.summary())
# print("Capturing packets...")
# sniff(prn=packet_callback, count=20)
from logger import AlertLogger
from alert import AlertManager
from scapy.all import sniff
from scapy.layers.inet import IP,TCP,UDP
from flow_manager import FlowManager
from feature_extractor import FeatureExtractor
from predictor import Predictor
from rules import RuleEngine

manager = FlowManager()
extractor = FeatureExtractor()
rules = RuleEngine()
predictor = Predictor()
logger = AlertLogger()
alert = AlertManager()

def packet_callback(packet):
    # Only Process IP Packets
    if IP not in packet:
        return 
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    
    protocol = "OTHER"
    src_port = 0
    dst_port= 0
    
    if TCP in packet:
        protocol= "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        
    packet_size = len(packet)
    
    tcp_flags = None

    if TCP in packet:
        tcp_flags = packet[TCP].flags

    header_length = packet[IP].ihl * 4

    flow = manager.process_packet(
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        packet_size,
        tcp_flags=tcp_flags,
        header_length=header_length
   )
    
    print(
    f"[DEBUG] Packets={flow.packet_count}, "
    f"SYN={flow.syn_count}, "
    f"Bytes={flow.total_bytes}"
)
    if flow.predicted:
      return
    
    # Wait until the flow has enough packets
    if flow.packet_count < 10:
        return
    # flow_data = flow.to_dict()
    # features = extractor.extract(flow_data)
    
    # prediction = predictor.predict(features)
    # probabilities = predictor.predict_proba(features)
    
    # confidence = max(probabilities) * 100
    
    flow_data = flow.to_dict()
    features = extractor.extract(flow_data)

    # -----------------------------
    # First check Rule Engine
    # -----------------------------
    rule_prediction = rules.detect(flow)

    if rule_prediction is not None:

       prediction = rule_prediction
       confidence = 100.0

   # -----------------------------
   # Otherwise use AI Model
   # -----------------------------
    else:

        prediction = predictor.predict(features)

        probabilities = predictor.predict_proba(features)

        confidence = max(probabilities) * 100
    
    if prediction != "BENIGN":
        alert.raise_alert(flow, prediction, confidence)

    logger.log(
       flow.src_ip,
       flow.dst_ip,
       flow.src_port,
       flow.dst_port,
       flow.protocol,
       prediction,
       confidence
   )
    if prediction != "BENIGN":

        print("\n🚨 ATTACK DETECTED 🚨")

    print("\n==============================")
    print(f"Flow       : {flow.src_ip}:{flow.src_port} -> {flow.dst_ip}:{flow.dst_port}")
    print(f"Packets    : {flow.packet_count}")
    print(f"Prediction : {prediction}")
    print(f"Confidence : {confidence:.2f}%")
    print("==============================")
    flow.predicted = True


print("[INFO]Capturing packets...")

sniff(prn=packet_callback, store=False)
        
    
    
