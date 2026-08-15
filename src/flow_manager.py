import time
from flow import Flow


class FlowManager:
    """
    Manages all active network flows.
    """

    def __init__(self):
        self.flows = {}
        self.flow_timeout = 30  # seconds

    def process_packet(
        self,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        packet_size,
        tcp_flags=None,
        header_length=20,
    ):
        """
        Create a new flow or update an existing flow.
        """

        forward_key = (
            src_ip,
            dst_ip,
            src_port,
            dst_port,
            protocol
        )

        reverse_key = (
            dst_ip,
            src_ip,
            dst_port,
            src_port,
            protocol
        )

        current_time = time.time()

        # -----------------------------
        # Existing Forward Flow
        # -----------------------------
        if forward_key in self.flows:

            flow = self.flows[forward_key]
            direction = "forward"

        # -----------------------------
        # Existing Reverse Flow
        # -----------------------------
        elif reverse_key in self.flows:

            flow = self.flows[reverse_key]
            direction = "backward"

        # -----------------------------
        # New Flow
        # -----------------------------
        else:

            flow = Flow(
                src_ip,
                dst_ip,
                src_port,
                dst_port,
                protocol
            )

            self.flows[forward_key] = flow
            direction = "forward"

        # -----------------------------
        # Flow Timeout
        # -----------------------------
        if current_time - flow.last_seen > self.flow_timeout:

            self.remove_flow(flow)

            flow = Flow(
                src_ip,
                dst_ip,
                src_port,
                dst_port,
                protocol
            )

            self.flows[forward_key] = flow
            direction = "forward"

        flow.last_seen = current_time

        # -----------------------------
        # Add Packet
        # -----------------------------
        flow.add_packet(
            packet_size=packet_size,
            direction=direction,
            tcp_flags=tcp_flags,
            header_length=header_length
        )

        return flow

    def remove_flow(self, flow):
        """
        Remove a completed flow from memory.
        """

        keys_to_delete = []

        for key, value in self.flows.items():

            if value == flow:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self.flows[key]