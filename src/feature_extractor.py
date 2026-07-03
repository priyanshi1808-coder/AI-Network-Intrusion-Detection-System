import statistics


class FeatureExtractor:

    def extract(self, flow):

        features = {}

        duration = flow["duration"]

        if duration <= 0:
            duration = 0.000001

        # ===============================
        # Flow Features
        # ===============================

        features["Flow Duration"] = flow["duration"]

        features["Total Fwd Packets"] = flow["forward_packets"]

        features["Total Backward Packets"] = flow["backward_packets"]

        features["Total Length of Fwd Packets"] = flow["forward_bytes"]

        features["Total Length of Bwd Packets"] = flow["backward_bytes"]

        # ===============================
        # Flow Speed
        # ===============================

        features["Flow Bytes/s"] = (
            flow["total_bytes"] / duration
        )

        features["Flow Packets/s"] = (
            flow["packet_count"] / duration
        )

        # ===============================
        # Forward Packet Statistics
        # ===============================

        fwd = flow["forward_packet_sizes"]

        if len(fwd) > 0:

            features["Fwd Packet Length Max"] = max(fwd)
            features["Fwd Packet Length Min"] = min(fwd)
            features["Fwd Packet Length Mean"] = statistics.mean(fwd)

            if len(fwd) > 1:
                features["Fwd Packet Length Std"] = statistics.stdev(fwd)
            else:
                features["Fwd Packet Length Std"] = 0

        else:

            features["Fwd Packet Length Max"] = 0
            features["Fwd Packet Length Min"] = 0
            features["Fwd Packet Length Mean"] = 0
            features["Fwd Packet Length Std"] = 0

        # ===============================
        # Backward Packet Statistics
        # ===============================

        bwd = flow["backward_packet_sizes"]

        if len(bwd) > 0:

            features["Bwd Packet Length Max"] = max(bwd)
            features["Bwd Packet Length Min"] = min(bwd)
            features["Bwd Packet Length Mean"] = statistics.mean(bwd)

            if len(bwd) > 1:
                features["Bwd Packet Length Std"] = statistics.stdev(bwd)
            else:
                features["Bwd Packet Length Std"] = 0

        else:

            features["Bwd Packet Length Max"] = 0
            features["Bwd Packet Length Min"] = 0
            features["Bwd Packet Length Mean"] = 0
            features["Bwd Packet Length Std"] = 0

        # ===============================
        # Overall Packet Statistics
        # ===============================

        packets = flow["packet_sizes"]

        if len(packets) > 0:

            features["Min Packet Length"] = min(packets)

            features["Max Packet Length"] = max(packets)

            features["Packet Length Mean"] = statistics.mean(packets)

            if len(packets) > 1:

                features["Packet Length Std"] = statistics.stdev(packets)

                features["Packet Length Variance"] = statistics.variance(
                    packets
                )

            else:

                features["Packet Length Std"] = 0

                features["Packet Length Variance"] = 0

            features["Average Packet Size"] = (
                flow["total_bytes"] /
                flow["packet_count"]
            )

        else:

            features["Min Packet Length"] = 0
            features["Max Packet Length"] = 0
            features["Packet Length Mean"] = 0
            features["Packet Length Std"] = 0
            features["Packet Length Variance"] = 0
            features["Average Packet Size"] = 0

        # ===============================
        # TCP Flags
        # ===============================

        features["FIN Flag Count"] = flow["fin_count"]

        features["SYN Flag Count"] = flow["syn_count"]

        features["RST Flag Count"] = flow["rst_count"]

        features["PSH Flag Count"] = flow["psh_count"]

        features["ACK Flag Count"] = flow["ack_count"]

        features["URG Flag Count"] = flow["urg_count"]

        return features