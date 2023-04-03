import subprocess
import threading
import time

# The list of commands to be run
commands = [
    "command1",
    "command2",
    "command3",
]

# The list of pcap file names
fileNames = [
    "file1.pcap",
    "file2.pcap",
    "file3.pcap",
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
