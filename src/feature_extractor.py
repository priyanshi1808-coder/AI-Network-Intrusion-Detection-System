class FeatureExtractor:
    """
    Convert Flow objects into ML Feature vectors.
    """
    def extract(self, flow):
        features = {
            "packet_count": flow.packet_count,
            "total_bytes": flow.total_bytes,
            "duration": flow.duration(),
            "bytes_per_packet": (
                flow.total_bytes / flow.packet_count
                if flow.packet_count > 0 else 0
            )
        }
        return features