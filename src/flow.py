from datetime import datetime

class Flow:
    """
    Represents a single network flow
    """
    
    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        
        self.src_port =src_port
        self.dst_port = dst_port
        
        self.protocol = protocol
        
        self.packet_count = 0
        self.total_bytes = 0
        
        self.start_time = datetime.now()
        self.last_seen = datetime.now()
        
    def update(self, packet_size):
        """
        Update flow statistics whenever a new packet arrives.
        """
        self.packet_count += 1
        self.total_bytes += packet_size
        self.last_seen = datetime.now()
        
    def duration(self):
        """
        Return flow duration in seconds
        """
        return (self.last_seen - self.start_time).total_seconds()
    
    def to_dict(self):
        """
        Convert flow information into dictionary format.
        """
        return {
            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,
            "src_port": self.src_port,
            "dst_port": self.dst_port,
            "protocol": self.protocol,
            "packet_count": self.packet_count,
            "total_bytes": self.total_bytes,
            "duration": self.duration()
            
        }
    