class RuleEngine:

    def __init__(self):

        # Rule Thresholds
        self.syn_threshold = 30
        self.packet_threshold = 200
        self.byte_threshold = 500000

    def detect(self, flow):

        # SYN Flood
        if flow.syn_count >= self.syn_threshold:
            return "SYN_FLOOD"

        # Packet Flood
        if flow.packet_count >= self.packet_threshold:
            return "PACKET_FLOOD"

        # Large Data Transfer
        if flow.total_bytes >= self.byte_threshold:
            return "DATA_FLOOD"

        return None