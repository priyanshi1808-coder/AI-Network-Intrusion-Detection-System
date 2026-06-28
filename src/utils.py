"""
Utility functions for AI Network Intrusion Detection System
"""

from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.inet6 import IPv6


def get_source_ip(packet):
    """Return source IP address"""
    if IP in packet:
        return packet[IP].src
    elif IPv6 in packet:
        return packet[IPv6].src
    return None


def get_destination_ip(packet):
    """Return destination IP address"""
    if IP in packet:
        return packet[IP].dst
    elif IPv6 in packet:
        return packet[IPv6].dst
    return None


def get_protocol(packet):
    """Return protocol name"""
    if TCP in packet:
        return "TCP"
    elif UDP in packet:
        return "UDP"
    return "OTHER"


def get_source_port(packet):
    """Return source port"""
    if TCP in packet:
        return packet[TCP].sport
    elif UDP in packet:
        return packet[UDP].sport
    return None


def get_destination_port(packet):
    """Return destination port"""
    if TCP in packet:
        return packet[TCP].dport
    elif UDP in packet:
        return packet[UDP].dport
    return None


def get_packet_size(packet):
    """Return packet size in bytes"""
    return len(packet)