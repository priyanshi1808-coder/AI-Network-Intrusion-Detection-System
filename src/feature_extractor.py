import statistics
from scipy.stats import skew, kurtosis

def calculate_iat(times):
    """
    Calculate Inter Arrival Time statistics.
    """

    if len(times) < 2:
        return 0, 0, 0, 0, 0, 0

    iats = []

    for i in range(1, len(times)):
        iats.append(times[i] - times[i - 1])

    mean = statistics.mean(iats)

    if len(iats) > 1:
        std = statistics.stdev(iats)
        var = statistics.variance(iats)
    else:
        std = 0
        var = 0

    return (
        sum(iats),
        mean,
        std,
        var,
        max(iats),
        min(iats)
    )
def calculate_stats(values):
    """
    Calculate Mean, Std, Max and Min.
    """

    if len(values) == 0:
        return 0, 0, 0, 0

    mean = statistics.mean(values)

    if len(values) > 1:
        std = statistics.stdev(values)
    else:
        std = 0

    return (
    mean,
    std,
    max(values),
    min(values)
)


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
        # Header Length Features
        # ===============================

        features["Fwd Header Length"] = sum(
           flow["forward_header_lengths"]
        )

        features["Bwd Header Length"] = sum(
           flow["backward_header_lengths"]
        )
    

        # CICIDS has this duplicate column
        features["Fwd Header Length.1"] = features["Fwd Header Length"]
        # ===============================
        
        # ===============================
        # Destination Port
        # ===============================

        features["Destination Port"] = flow["dst_port"]
        
        # ==============================
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
        # Packet Length Distribution
        # ===============================

        if len(packets) > 1:
            features["Packet Length Median"] = statistics.median(packets)
        else:
            features["Packet Length Median"] = 0

        if len(packets) > 0:
            features["Packet Length Range"] = (
                max(packets) - min(packets)
            )
        else:
            features["Packet Length Range"] = 0
            
        # ===============================
        # Packet Length Skewness
        # ===============================

        if len(packets) > 2:
            features["Packet Length Skewness"] = float(skew(packets))
        else:
            features["Packet Length Skewness"] = 0
            
        # ===============================
        # Packet Length Kurtosis
        # ===============================

        if len(packets) > 3:
            features["Packet Length Kurtosis"] = float(
               kurtosis(packets)
            )
        else:
            features["Packet Length Kurtosis"] = 0
            
        
        # ===============================
        # TCP Flags
        # ===============================

        features["FIN Flag Count"] = flow["fin_count"]
        features["SYN Flag Count"] = flow["syn_count"]
        features["RST Flag Count"] = flow["rst_count"]
        features["PSH Flag Count"] = flow["psh_count"]
        features["ACK Flag Count"] = flow["ack_count"]
        features["URG Flag Count"] = flow["urg_count"]
        
        # ===============================
        # Segment Size Features
        # ===============================

        if flow["forward_packets"] > 0:
            features["Avg Fwd Segment Size"] = (
                flow["forward_bytes"] /
                flow["forward_packets"]
    )
        else:
            features["Avg Fwd Segment Size"] = 0

        if flow["backward_packets"] > 0:
            features["Avg Bwd Segment Size"] = (
                flow["backward_bytes"] /
                flow["backward_packets"]
            )
        else:
            features["Avg Bwd Segment Size"] = 0
            
        # ===============================
        # Flow Packet Length Statistics
        # ===============================

        if len(packets) > 0:

            features["Flow Packet Length Mean"] = statistics.mean(packets)

            if len(packets) > 1:
                features["Flow Packet Length Std"] = statistics.stdev(packets)
                features["Flow Packet Length Variance"] = statistics.variance(
                    packets
              )
            else:
                features["Flow Packet Length Std"] = 0
                features["Flow Packet Length Variance"] = 0

        else:

            features["Flow Packet Length Mean"] = 0
            features["Flow Packet Length Std"] = 0
            features["Flow Packet Length Variance"] = 0
            
            
        # ===============================
        # Flow Byte Ratio Features
        # ===============================

        if flow["total_bytes"] > 0:

            features["Fwd Byte Ratio"] = (
                flow["forward_bytes"] /
                flow["total_bytes"]
            )

            features["Bwd Byte Ratio"] = (
                flow["backward_bytes"] /
                flow["total_bytes"]
            )

        else:

            features["Fwd Byte Ratio"] = 0
            features["Bwd Byte Ratio"] = 0
            
        # ===============================
        # Packet Size Ratio Features
        # ===============================

        overall_avg = features["Average Packet Size"]

        if overall_avg > 0:

            features["Fwd Packet Size Ratio"] = (
                features["Avg Fwd Segment Size"] /
                overall_avg
            )

            features["Bwd Packet Size Ratio"] = (
                features["Avg Bwd Segment Size"] /
                overall_avg
            )

        else:

            features["Fwd Packet Size Ratio"] = 0
            features["Bwd Packet Size Ratio"] = 0

        # ===============================
        # Flow IAT Features
        # ===============================

        flow_total, flow_mean, flow_std, flow_var, flow_max, flow_min = calculate_iat(
            flow["packet_times"]
    )

        features["Flow IAT Total"] = flow_total
        features["Flow IAT Mean"] = flow_mean
        features["Flow IAT Std"] = flow_std
        features["Flow IAT Variance"] = flow_var
        features["Flow IAT Max"] = flow_max
        features["Flow IAT Min"] = flow_min

        # ===============================
        # Forward IAT Features
        # ===============================

        fwd_total, fwd_mean, fwd_std, fwd_var, fwd_max, fwd_min = calculate_iat(
            flow["forward_times"]
    )

        features["Fwd IAT Total"] = fwd_total
        features["Fwd IAT Mean"] = fwd_mean
        features["Fwd IAT Std"] = fwd_std
        features["Fwd IAT Variance"] = fwd_var
        features["Fwd IAT Max"] = fwd_max
        features["Fwd IAT Min"] = fwd_min

        # ===============================
        # Backward IAT Features
        # ===============================

        bwd_total, bwd_mean, bwd_std, bwd_var, bwd_max, bwd_min = calculate_iat(
            flow["backward_times"]
    )

        features["Bwd IAT Total"] = bwd_total
        features["Bwd IAT Mean"] = bwd_mean
        features["Bwd IAT Std"] = bwd_std
        features["Bwd IAT Variance"] = bwd_var
        features["Bwd IAT Max"] = bwd_max
        features["Bwd IAT Min"] = bwd_min

        # ===============================
        # Subflow Features
        # ===============================
    
        features["Subflow Fwd Packets"] = flow["forward_packets"]
        features["Subflow Fwd Bytes"] = flow["forward_bytes"]

        features["Subflow Bwd Packets"] = flow["backward_packets"]
        features["Subflow Bwd Bytes"] = flow["backward_bytes"]
        
        # =============================
        # Packet Rate Features
        # =============================
        features["Fwd Packets/s"] = (
            flow["forward_packets"] / duration
        )

        features["Bwd Packets/s"] = (
            flow["backward_packets"] / duration
        )
        
        # =============================
        # Down/Up Ratio
        # =============================
        if flow["forward_packets"] > 0:
            features["Down/Up Ratio"] = (
                flow["backward_packets"] /
                flow["forward_packets"]
            )
        else:
            features["Down/Up Ratio"] = 0
            
        # ===============================
        # Active / Idle Features
        # ===============================

        active_mean, active_std, active_max, active_min = calculate_stats(
            flow["active_times"]
        )

        features["Active Mean"] = active_mean
        features["Active Std"] = active_std
        features["Active Max"] = active_max
        features["Active Min"] = active_min

        idle_mean, idle_std, idle_max, idle_min = calculate_stats(
            flow["idle_times"]
        )

        features["Idle Mean"] = idle_mean
        features["Idle Std"] = idle_std
        features["Idle Max"] = idle_max
        features["Idle Min"] = idle_min
        
        # ===============================
        # Bulk Transfer Features
        # ===============================

        features["Fwd Avg Bytes/Bulk"] = flow["fwd_bulk_bytes"]
        features["Fwd Avg Packets/Bulk"] = flow["fwd_bulk_packets"]
        features["Fwd Avg Bulk Rate"] = flow["fwd_bulk_rate"]

        features["Bwd Avg Bytes/Bulk"] = flow["bwd_bulk_bytes"]
        features["Bwd Avg Packets/Bulk"] = flow["bwd_bulk_packets"]
        features["Bwd Avg Bulk Rate"] = flow["bwd_bulk_rate"]
            
        return features