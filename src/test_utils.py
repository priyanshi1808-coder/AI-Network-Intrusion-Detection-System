from scapy.all import sniff

from utils import (
    get_source_ip,
    get_destination_ip,
    get_protocol,
    get_source_port,
    get_destination_port,
    get_packet_size,
)
def process(packet):
    print("=" * 60)
    print("Source Ip     :",get_source_ip(packet))
    print("Destination Ip:",get_destination_ip(packet))
    print("Protocol      :",get_protocol(packet))
    print("Source Port   :",get_source_port(packet))
    print("Destination Port:",get_destination_port(packet))
    print("Packet Size   :",get_packet_size(packet))
    
print("Waiting for packets...\n")

sniff(prn=process, count=5)