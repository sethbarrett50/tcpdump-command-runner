import subprocess
import threading
import time

# The list of commands to be run
commands = [
    "nmap -sX -p 1-100 192.168.1.103",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.103",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.103",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.104",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.104",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.104",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.175",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.175",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.175",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.221",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.221",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.221",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.102",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.102",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.102",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.196",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.196",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 53 192.168.1.196",      # UDP Flood on port 53
    "nmap -sX -p 1-100 192.168.1.228",              # XMAS Flood on ports 1-100
    "hping3 -S -c 100 -p 443 192.168.1.228",        # TCP/SYN Flood on port 443
    "hping3 --udp -c 100 -p 443 192.168.1.228",     # UDP Flood on port 53
    "hping3 -S -c 100 -p 80 192.168.1.103",         # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.104",         # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.x",           # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.221",         # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.102",         # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.196",         # HTTP Flood
    "hping3 -S -c 100 -p 80 192.168.1.228",         # HTTP Flood
]

# The list of pcap file names
fileNames = [
    "echoXMAS.pcap",
    "echoTCP.pcap",
    "echoUDP.pcap",
    "kasaXMAS.pcap",
    "kasaTCP.pcap",
    "kasaUDP.pcap",
    "LongPlusXMAS.pcap",
    "LongPlusTCP.pcap",
    "LongPlusUDP.pcap",
    "RingXMAS.pcap",
    "RingTCP.pcap",
    "RingUDP.pcap",
    "NestXMAS.pcap",
    "NestTCP.pcap",
    "NestUDP.pcap",
    "HomeCamXMAS.pcap",
    "HomeCamTCP.pcap",
    "HomeCamUDP.pcap",
    "NiteBirdXMAS.pcap",
    "NiteBirdTCP.pcap",
    "NiteBirdUDP.pcap",
    "echoHTTP.pcap",
    "kasaHTTP.pcap",
    "LongPlusHTTP.pcap",
    "RingHTTP.pcap",
    "NestHTTP.pcap",
    "HomeCamHTTP.pcap",
    "NiteBirdHTTP.pcap",
]

# The duration to collect packets (8 hours)
capture_duration = 8 * 60 * 60

def run_command(command):
    subprocess.run(command, shell=True)

# Iterate through the list of commands and file names
for command, file_name in zip(commands, fileNames):
    # Start tcpdump and collect packets
    tcpdump_process = subprocess.Popen(
        ["tcpdump", "-w", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    # Sleep for the capture duration
    time.sleep(capture_duration)

    # Run the command from the commands list in a separate thread
    command_thread = threading.Thread(target=run_command, args=(command,))
    command_thread.start()

    # Wait for the command to finish
    command_thread.join()

    # Terminate the tcpdump process
    tcpdump_process.terminate()
    
