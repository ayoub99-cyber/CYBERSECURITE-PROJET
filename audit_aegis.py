import subprocess
import json
import nmap

def check_security_services():
    services = {
        "ufw": "ufw status",
        "fail2ban": "systemctl is-active fail2ban"
    }
    status_report = {}
    
    for name, cmd in services.items():
        try:
            output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
            status_report[name] = "Actif" if "active" in output or "Status: active" in output else "Inactif"
        except:
            status_report[name] = "Erreur"
            
    return status_report

def scan_ports():
    nm = nmap.PortScanner()
    nm.scan('127.0.0.1', '1-3000')
    open_ports = []
    
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    open_ports.append({"port": port, "state": "open"})
    return {"127.0.0.1": open_ports}

def run_audit():
    report = {
        "services_securite": check_security_services(),
        "ports_ouverts": scan_ports()
    }
    with open('audit_result.json', 'w') as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    run_audit()