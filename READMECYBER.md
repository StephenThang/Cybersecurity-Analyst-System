# Cybersecurity Analyst System — Python OOP Project

A Python object oriented programming project that models a cybersecurity operations team using inheritance and polymorphism. The system simulates three analyst roles — SOC Analyst, Threat Hunter, and Penetration Tester — all inheriting from a shared parent Analyst class.

---

## Overview

This project demonstrates core OOP principles applied to a real world cybersecurity operations center. Each analyst role inherits shared behavior from the parent class and extends it with role specific methods and attributes that reflect how each role actually operates in the field.

---

## OOP Concepts Demonstrated

| Concept | How it appears |
|---|---|
| Encapsulation | Each class owns its own data and methods |
| Inheritance | SOCAnalyst, ThreatHunter, PenTester all inherit from Analyst |
| Polymorphism | Every class has `respond_to_incident()` but each responds differently |

---

## Class Structure

```
Analyst                          ← Parent class
    ↓
SOCAnalyst(Analyst)              ← Monitors and triages alerts
ThreatHunter(Analyst)            ← Hunts threats using IOCs and hypotheses
PenTester(Analyst)               ← Tests systems for vulnerabilities
```

---

## Parent Class — Analyst

Shared attributes and methods inherited by all child classes.

### Attributes
| Attribute | Description |
|---|---|
| `name` | Analyst's name |
| `clearance` | Security clearance level (1, 2, 3) |
| `tools` | List of tools the analyst uses |
| `shift` | day, night, or weekend |
| `loggedin` | Whether analyst is currently logged in |
| `reports` | List of filed reports |

### Methods
| Method | Description |
|---|---|
| `log_in()` | Sets loggedin to True |
| `log_out()` | Sets loggedin to False |
| `file_report(finding)` | Appends a finding to the reports list |
| `get_tools()` | Returns the analyst's tools |
| `is_on_shift()` | Returns True if analyst is on a valid shift |
| `__str__()` | Returns formatted analyst card |

---

## Child Class — SOCAnalyst

Monitors incoming alerts and performs triage.

### Extra Attributes
| Attribute | Description |
|---|---|
| `alerts` | List of active alerts |
| `triage_level` | low, medium, high, or critical |

### Extra Methods
| Method | Description |
|---|---|
| `monitor_alerts()` | Returns current alert list |
| `add_alert(alert)` | Adds a new alert to the list |
| `triage()` | Evaluates alerts and assigns severity level |
| `escalate()` | Escalates high or critical alerts to Threat Hunter |
| `respond_to_incident()` | SOC specific incident response |

---

## Child Class — ThreatHunter

Proactively hunts threats using hypotheses and indicators of compromise.

### Extra Attributes
| Attribute | Description |
|---|---|
| `hypothesis` | Current hunt hypothesis |
| `ioc` | List of indicators of compromise |
| `pivot_trail` | Trail of evidence followed during hunt |

### Extra Methods
| Method | Description |
|---|---|
| `build_hypothesis(hypothesis)` | Sets the hunt hypothesis |
| `add_ioc(ioc)` | Adds an IOC to track |
| `hunt()` | Scans through all IOCs for findings |
| `pivot(new_lead)` | Follows a new lead and adds to pivot trail |
| `get_pivot_trail()` | Returns numbered list of all pivots |
| `respond_to_incident()` | Threat Hunter specific incident response |

---

## Child Class — PenTester

Tests systems for vulnerabilities within a defined scope.

### Extra Attributes
| Attribute | Description |
|---|---|
| `scope` | List of systems in scope |
| `findings` | List of vulnerabilities discovered |

### Extra Methods
| Method | Description |
|---|---|
| `recon(target)` | Gathers information on a target |
| `exploit(target)` | Attempts to find a vulnerability |
| `write_findings(finding)` | Documents a discovered vulnerability |
| `respond_to_incident()` | PenTester specific incident response |

---

## Example Usage

```python
# SOC Analyst
soc = SOCAnalyst(
    name="Stephen",
    clearance=2,
    tools=["Splunk", "IBM QRadar", "CrowdStrike"],
    shift="day"
)
soc.log_in()
soc.add_alert("critical - ransomware detected on workstation 10.0.0.5")
soc.triage()
soc.escalate()
print(soc)

# Threat Hunter
hunter = ThreatHunter(
    name="Marcus",
    clearance=3,
    tools=["Splunk", "MISP", "Wireshark"],
    shift="night"
)
hunter.build_hypothesis("APT28 lateral movement via RDP using stolen credentials")
hunter.add_ioc("192.168.1.200")
hunter.add_ioc("mimikatz.exe")
hunter.hunt()
hunter.pivot("Compromised domain admin account found")
hunter.pivot("C2 beacon to 185.220.101.99 every 60 seconds")
print(hunter)

# Pen Tester
tester = PenTester(
    name="Diana",
    clearance=3,
    tools=["Metasploit", "Burp Suite", "Nmap"],
    shift="day"
)
tester.recon("192.168.1.1")
tester.exploit("192.168.1.1")
tester.write_findings("CVE-2021-41773 - Apache path traversal vulnerability")
print(tester)
```

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/StephenThang/cybersecurity-analyst-system.git
cd cybersecurity-analyst-system
```

**2. Make sure Python is installed**
```bash
python --version
```
Requires Python 3.10 or higher.

**3. Run the program**
```bash
python CyberSystem.py
```

---

## Real World Relevance

| Role | Real world equivalent |
|---|---|
| SOCAnalyst | Tier 1/2 SOC Analyst monitoring SIEM alerts |
| ThreatHunter | Threat Intelligence Analyst proactively hunting APTs |
| PenTester | Ethical Hacker conducting authorized penetration tests |

---

## Skills Demonstrated

- Python object oriented programming
- Inheritance and polymorphism
- Encapsulation and single responsibility design
- Cybersecurity operations concepts
- MITRE ATT&CK aligned threat scenarios
- Formatted report generation

---

## Author

**Stephen Vanlian Thang**
Dual B.S. Psychology & Information Science (Cybersecurity) — University of Maryland
Certified Ethical Hacker (CEH)
[Portfolio](https://StephenThang.github.io) | [LinkedIn](https://www.linkedin.com/in/stephen-thang-743338264/)
