from flow import Flow

class FlowManager:
    """
    Manages all active network flows
    """
    def __init__(self):
        self.flows = {}
    
    def process_packet(
        self,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        packet_size,
    ):
        """
        Create a new flow and upfdate an existing flow
        """
        flow_key=(
            src_ip,
            dst_ip,
            src_port,
            dst_port,
            protocol
        )
        if flow_key not in self.flows:
            self.flows[flow_key] = Flow(
                src_ip,
                dst_ip,
                src_port,
                dst_port,
                protocol
            )
        self.flows[flow_key].update(packet_size)
    def get_all_flows(self):
        """
        Return all active flows.
        """
        return self.flows
        
        

