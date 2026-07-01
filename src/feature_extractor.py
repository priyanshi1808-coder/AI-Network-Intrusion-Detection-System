import statistics

class FeatureExtractor:
    def extract(self, flow):
        packet_sizes = flow["packet_sizes"]
        
        features = {}
        
        # Basic Flow features
        
        features["flow_duration"] = flow["duration"]
        features["packet_count"] = flow["packet_count"]
        features["total_bytes"] = flow["total_bytes"]
        
        # Average Packet Size
        if flow["packet_count"] > 0:
            features["avg_packet_size"] = (
                flow["total_bytes"] / flow["packet_count"]
            )
        else:
            features["avg_packet_size"] = 0

        # Bytes per second
        
        if flow["duration"] > 0:
            features["flow_bytes_per_sec"] = flow["total_bytes"] / flow["duration"]
            features["flow_packets_per_sec"] = flow["packet_count"] / flow["duration"]
            
        else:
            features["flow_packets_per_sec"] = 0
            
        # Packet Statistics
        features["min_packet_size"] = min(packet_sizes)
        features["max_packet_size"] = max(packet_sizes)
        features["mean_packet_size"] = statistics.mean(packet_sizes)

        if len(packet_sizes) > 1:
            features["std_packet_size"] = statistics.stdev(packet_sizes)
        else:
            features["std_packet_size"] = 0

        return features
            
        
    