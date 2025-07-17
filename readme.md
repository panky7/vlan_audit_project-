
---

```markdown
# VLAN Audit Automation for Cisco Switches

This project provides a Python-based automation solution to audit VLAN configurations from multiple Cisco IOS switches using SSH and the Netmiko library.

---

## 📁 Project Structure

```

vlan_audit_project/  
├── vlan_audit.py # Main script to collect VLAN data  
├── switches.txt # List of switch IP addresses (one per line)  
├── creds.txt # Common SSH credentials (username & password)  
├── vlan_audit.csv # Output CSV file with VLAN info (auto-generated)  
├── errors.log # Error log for connection or command issues (auto-generated)  
├── requirements.txt # Python dependencies  
├── README.md # This documentation file

````

---

## 🔧 Requirements

- Python 3.6+
- Cisco IOS switches with SSH enabled
- Netmiko library

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📄 Input Files

### `switches.txt`

List of switch IP addresses:

```
192.168.1.10
192.168.1.11
```

### `creds.txt`

Common credentials in key=value format:

```
username=admin
password=Cisco123
```

> ⚠️ **Keep this file secure.** Do not share or upload to version control.

---

## ▶️ How to Run

Execute the script using:

```bash
python vlan_audit.py
```

The script will:

- SSH into each switch listed in `switches.txt`
    
- Retrieve the switch hostname using: `show run | include hostname`
    
- Retrieve VLAN information using: `show vlan brief`
    
- Save data into `vlan_audit.csv` with columns:
    
    - `switch_hostname`
        
    - `switch_ip`
        
    - `vlan_id`
        
    - `vlan_name`
        
- Log any connection or parsing errors in `errors.log`
    

---

## ✅ Output Example (`vlan_audit.csv`)

```csv
switch_hostname,switch_ip,vlan_id,vlan_name
SW1,192.168.1.10,1,default
SW1,192.168.1.10,10,Sales
SW2,192.168.1.11,1,default
SW2,192.168.1.11,30,HR
```

---

## 🛠 Notes

- Script is designed for Cisco IOS switches
    
- Use in test environments before deploying in production
    
- Extendable for more commands or data formats
    

---

## 📚 Resources

- [Netmiko on GitHub](https://github.com/ktbyers/netmiko)
    
- Cisco CLI command: `show vlan brief`, `show run | include hostname`
    

---
