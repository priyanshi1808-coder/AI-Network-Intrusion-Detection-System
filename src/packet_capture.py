# from scapy.all import sniff
# def packet_callback(packet):
#     print(packet.summary())
# print("Capturing packets...")
# sniff(prn=packet_callback, count=20)

from scapy.all import sniff
from scapy.layers.inet import IP,TCP,UDP
from flow_manager import FlowManager
manager = FlowManager()

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
        
    pcket_size = len(packet)
    manager.process_packet(
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        pcket_size
    )
    
    print("\n==============================")

    for flow in manager.get_all_flows().values():

        data = flow.to_dict()

        for key, value in data.items():
            print(f"{key:<20}: {value}")

    print("==============================")

print("Capturing packets...")

sniff(prn=packet_callback, store=False)
        
    
    
