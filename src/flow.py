import time


class Flow:

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol):

        # Flow Identification
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol

        # Time Information
        self.start_time = time.time()
        self.last_seen = self.start_time

        # Packet Statistics
        self.packet_count = 0
        self.total_bytes = 0
        self.packet_sizes = []

        # Forward / Backward Statistics
        self.forward_packets = 0
        self.backward_packets = 0

        self.forward_bytes = 0
        self.backward_bytes = 0

        self.forward_packet_sizes = []
        self.backward_packet_sizes = []

        # Packet Arrival Times
        self.packet_times = []
        self.forward_times = []
        self.backward_times = []
        
        # Active / Idle Times
        self.active_times = []
        self.idle_times = []

        # TCP Flag Counters
        self.syn_count = 0
        self.ack_count = 0
        self.fin_count = 0
        self.rst_count = 0
        self.psh_count = 0
        self.urg_count = 0

        # Header Lengths
        self.forward_header_lengths = []
        self.backward_header_lengths = []

    # ------------------------------------

    def add_packet(
        self,
        packet_size,
        direction="forward",
        tcp_flags=None,
        header_length=20
    ):

        now = time.time()

        self.packet_count += 1
        self.total_bytes += packet_size

        self.packet_sizes.append(packet_size)
        
        # Calculate Active / Idle gap
        if len(self.packet_times) > 0:

            gap = now - self.packet_times[-1]

            if gap > 1:
                self.idle_times.append(gap)
            else:
                self.active_times.append(gap)

        self.packet_times.append(now)

        self.last_seen = now

        # Forward Direction
        if direction == "forward":

            self.forward_packets += 1
            self.forward_bytes += packet_size

            self.forward_packet_sizes.append(packet_size)

            self.forward_times.append(now)

            self.forward_header_lengths.append(header_length)

        # Backward Direction
        else:

            self.backward_packets += 1
            self.backward_bytes += packet_size

            self.backward_packet_sizes.append(packet_size)

            self.backward_times.append(now)

            self.backward_header_lengths.append(header_length)

        # TCP Flags
        if tcp_flags:

            if "S" in tcp_flags:
                self.syn_count += 1

            if "A" in tcp_flags:
                self.ack_count += 1

            if "F" in tcp_flags:
                self.fin_count += 1

            if "R" in tcp_flags:
                self.rst_count += 1

            if "P" in tcp_flags:
                self.psh_count += 1

            if "U" in tcp_flags:
                self.urg_count += 1

    # ------------------------------------

    def get_duration(self):

        return self.last_seen - self.start_time

    # ------------------------------------

    def to_dict(self):

        return {

            "src_ip": self.src_ip,
    "dst_ip": self.dst_ip,
    "src_port": self.src_port,
    "dst_port": self.dst_port,
    "protocol": self.protocol,

    "packet_count": self.packet_count,
    "total_bytes": self.total_bytes,
    "duration": round(self.get_duration(), 6),

    "forward_packets": self.forward_packets,
    "backward_packets": self.backward_packets,

    "forward_bytes": self.forward_bytes,
    "backward_bytes": self.backward_bytes,

    "packet_sizes": self.packet_sizes,

    "forward_packet_sizes": self.forward_packet_sizes,
    "backward_packet_sizes": self.backward_packet_sizes,
    
    "forward_header_lengths": self.forward_header_lengths,
    "backward_header_lengths": self.backward_header_lengths,

    # NEW
    "packet_times": self.packet_times,
    "forward_times": self.forward_times,
    "backward_times": self.backward_times,
    
    "active_times": self.active_times,
    "idle_times": self.idle_times,

    "syn_count": self.syn_count,
    "ack_count": self.ack_count,
    "fin_count": self.fin_count,
    "rst_count": self.rst_count,
    "psh_count": self.psh_count,
    "urg_count": self.urg_count
}
