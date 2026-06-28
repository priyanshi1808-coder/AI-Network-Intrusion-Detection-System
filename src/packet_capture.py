from scapy.all import sniff
def packet_callback(packet):
    print(packet.summary())
print("Capturing packets...")
sniff(prn=packet_callback, count=20)
