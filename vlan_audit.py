import csv
import re
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# Read switches
with open("switches.txt") as f:
    switch_ips = [line.strip() for line in f if line.strip()]

# Read creds
creds = {}
with open("creds.txt") as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            creds[key.strip()] = value.strip()

username = creds.get("username")
password = creds.get("password")

# Output files
output_file = "vlan_audit.csv"
error_log = "errors.log"

# CSV Header
with open(output_file, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["switch_hostname", "switch_ip", "vlan_id", "vlan_name"])

# Start collecting data
for ip in switch_ips:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }

    try:
        conn = ConnectHandler(**device)

        # Get hostname
        hostname_output = conn.send_command("show run | include hostname")
        hostname_match = re.search(r"hostname\s+(\S+)", hostname_output)
        hostname = hostname_match.group(1) if hostname_match else "UNKNOWN"

        # Get VLANs
        vlan_output = conn.send_command("show vlan brief")
        vlan_lines = vlan_output.splitlines()

        for line in vlan_lines:
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0].isdigit():
                vlan_id = parts[0]
                vlan_name = parts[1]
                with open(output_file, mode='a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([hostname, ip, vlan_id, vlan_name])

        conn.disconnect()

    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        with open(error_log, mode='a') as errfile:
            errfile.write(f"{ip} - Connection failed: {str(e)}\n")
    except Exception as e:
        with open(error_log, mode='a') as errfile:
            errfile.write(f"{ip} - Unexpected error: {str(e)}\n")
