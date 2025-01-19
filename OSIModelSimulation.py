# OSI Model Simulation in Python

def application_layer(message):
    print(f"Application Layer: {message}")

def presentation_layer(message):
    # Convert message to hexadecimal
    encoded_message = ' '.join([format(ord(c), 'x') for c in message])
    print(f"Presentation Layer (Encoded in Hex): {encoded_message}")

def session_layer():
    print("Session Layer: Establishing session...")

def transport_layer(message):
    # Split the message into smaller packets
    packets = [message[i:i+10] for i in range(0, len(message), 10)]
    print("Transport Layer: Segmented into packets:")
    for packet in packets:
        print(f" - {packet}")

def network_layer():
    print("Network Layer: Assigning IP addresses (Source: 192.168.1.10, Destination: 203.0.113.5)")

def data_link_layer():
    print("Data Link Layer: Framing with MAC addresses (Source: 00:1A:2B:3C:4D:5E, Destination: 00:5E:4D:3C:2B:1A)")

def physical_layer():
    print("Physical Layer: Transmitting via network medium (Wi-Fi/Ethernet)")

def main():
    message = "Hello, this is Jeevan's first project"
    
    # Simulate OSI layers
    application_layer(message)
    presentation_layer(message)
    session_layer()
    transport_layer(message)
    network_layer()
    data_link_layer()
    physical_layer()

    print("\nMessage transmission complete!")

if __name__ == "__main__":
    main()
