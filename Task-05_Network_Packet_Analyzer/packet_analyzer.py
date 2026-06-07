from scapy.all import sniff


# Function to process packets
def packet_callback(packet):

    print("\n--- Packet Captured ---")

    # Source and Destination IP
    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)

    # Protocol
    print("Protocol:", packet.summary())


# Start sniffing packets
print("Starting Packet Analyzer...")

sniff(prn=packet_callback, count=5)

print("Packet Capture Completed.")