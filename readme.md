```markdown
# VLAN Audit Automation with Python (Cisco IOS)

This project automates the auditing of VLAN configurations across multiple Cisco switches using SSH and Netmiko.

---

## 📦 Project Structure

```

vlan\_audit\_project/
├── switches.txt         # List of switch IPs (one per line)
├── creds.txt            # Common SSH credentials (username & password)
├── vlan\_audit.py        # Main Python script to run the audit
├── vlan\_audit.csv       # Output CSV file (generated after script runs)
├── errors.log           # Log file for any connection or command failures
├── requirements.txt     # Required Python packages
├── README.md            # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Install Python dependencies

Create a virtual environment (optional but recommended), then install required packages:

```bash
pip install -r requirements.txt
````

### 2. Configure Input Files

#### `switches.txt`

List the IP addresses of Cisco switches, one per line:

```
192.168.1.10
192.168.1.11
```

#### `creds.txt`

Store your common SSH credentials in this format:

```
username=admin
password=Cisco123
```

> ⚠️ **Important:** Keep `creds.txt` secure. Do not share or commit it to version control.

---

## ▶️ Running the Script

Run the script with:

```bash
python vlan_audit.py
```

* VLAN data will be saved to `vlan_audit.csv`
* Any failed connections or errors will be logged in `errors.log`

---

## 📄 Output Format (`vlan_audit.csv`)

The output CSV contains:

| switch\_hostname | switch\_ip   | vlan\_id | vlan\_name |
| ---------------- | ------------ | -------- | ---------- |
| SW1              | 192.168.1.10 | 1        | default    |
| SW1              | 192.168.1.10 | 10       | Sales      |
| SW2              | 192.168.1.11 | 1        | default    |

---

## 🛠 Requirements

* Python 3.6+
* Cisco IOS devices with SSH enabled
* Netmiko library

---

## 📚 References

* [Netmiko GitHub](https://github.com/ktbyers/netmiko)
* Cisco IOS command: `show vlan brief`, `show run | include hostname`

---

## 🧯 Disclaimer

Use this script responsibly in production environments. Ensure that you test in a lab environment before widespread deployment.

