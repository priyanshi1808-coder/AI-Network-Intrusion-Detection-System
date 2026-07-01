from datetime import datetime


class Flow:

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol):

        self.src_ip = src_ip
        self.dst_ip = dst_ip

        self.src_port = src_port
        self.dst_port = dst_port

        self.protocol = protocol

        self.packet_count = 0
        self.total_bytes = 0

        # NEW
        self.packet_sizes = []
        self.timestamps = []

        # TCP Flags
        self.syn_count = 0
        self.ack_count = 0
        self.fin_count = 0
        self.rst_count = 0
        self.psh_count = 0

        self.start_time = datetime.now()
        self.last_seen = datetime.now()

    def update(self, packet_size):

        self.packet_count += 1
        self.total_bytes += packet_size

        self.packet_sizes.append(packet_size)
        self.timestamps.append(datetime.now())

        self.last_seen = datetime.now()

    def duration(self):

        return (
            self.last_seen -
            self.start_time
        ).total_seconds()

    def to_dict(self):

        return {

            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,

            "src_port": self.src_port,
            "dst_port": self.dst_port,

            "protocol": self.protocol,

            "packet_count": self.packet_count,

            "total_bytes": self.total_bytes,

            "duration": self.duration(),

            "packet_sizes": self.packet_sizes,

            "syn_count": self.syn_count,

            "ack_count": self.ack_count,

            "fin_count": self.fin_count,

            "rst_count": self.rst_count,

            "psh_count": self.psh_count
        }