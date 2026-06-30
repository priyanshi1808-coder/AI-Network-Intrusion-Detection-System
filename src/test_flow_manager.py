from flow_manager import FlowManager

manager = FlowManager()

manager.process_packet(
    "192.168.1.10",
    "8.8.8.8",
    55000,
    53,
    "UDP",
    120
)
manager.process_packet(
    "192.168.1.10",
    "8.8.8.8",
    55000,
    53,
    "UDP",
    80
)
for key, flow in manager.get_all_flows().items():
    flow_data = flow.to_dict()

print("\nFlow Details")
print("-" * 40)

for key, value in flow_data.items():
    print(f"{key:<15}: {value}")