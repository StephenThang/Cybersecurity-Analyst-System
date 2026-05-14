class Analyst():
    def __init__(self, name , clearance, tools, shift, loggedin = False):
            self.clearance = clearance
            self.tools = tools
            self.shift = shift
            self.loggedin = loggedin
            self.name = name

    def log_in(self):
        self.log_in = True

    def log_out(self):
        self.log_in = False

    def file_report(self):
        report = ""
        return report
        
    def get_tools(self):
        return self.tools
        
    def is_on_shift(self):
        if self.shift in ["day", "night", "weekend"]:
            return True
        return False
        
    def __str__(self):
        return f"Analyst Card: {self.name}"
        
class SOCAnalyst(Analyst):
    def __init__(self, name, clearance, tools, shift, triage_level="low"):
        super().__init__(name, clearance, tools, shift)
        self.alerts = []
        self.triage_level = triage_level

    def monitor_alerts(self):
        return self.alerts

    def add_alerts(self, alert):
        self.alerts.append(alert)
        return f"Alert added: {alert}"
    
    def triage(self):
        for alert in self.alerts:
            if "critical" in alert.lower():
                self.triage_level = "critical"
            elif "high" in alert.lower():
                self.triage_level = "higher"
            elif "medium" in alert.lower():
                self.triage_level = "medium"
            else:
                self.triage_level = "low"
        return f"Triage level: {self.triage_level}"
    def escalate(self):
        if self.triage_level in ["high", "critical"]:
            return f"Escalating {self.triage_level} alert to Threat Hunter"
        return "No escalation needed"
    
    def respond_to_incidents(self):
        return f"SOC Analyst {self.name} is monitoring alerts and triaging incidents"
    
class ThreatHunter(Analyst):
    def __init__(self, name, clearance, tools, shift):
        super().__init__(name, clearance, tools, shift)
        #User super() to copy parent class attributes instead of rewriting them all over again
        self.hypothesis = ""
        self.ioc = []
        self.pivot_trail = []
    def build_hypothesis(self, hypothesis):
        self.hypothesis = hypothesis
        return f"Hypothesis set: {self.hypothesis}"
    
    def add_ioc(self, ioc):
        self.ioc.append(ioc)
        return f"IOC added: {ioc}"
    
    def hunt(self):
        if len(self.ioc) == 0:
            return "No IOCs to hunt"
        findings = []
        for i in self.ioc:
            print(f"Hunting IOC: {i}")
            findings.append(f"Suspicious activity found for: {i}")
        return findings
    
    def pivot(self, new_lead):
        self.pivot_trail.append(new_lead)
        return f"Pivoted to new lead: {new_lead}"
    
    def get_pivot_trail(self):
        if len(self.pivot_trail) == 0:
            return "No pivots yet"
        result = ""
        for i, lead in enumerate(self.pivot_trail):
            result += f" [{i+1}] {lead}\n"
        return result
    
    def respond_to_incident(self):
        return f"Threat Hunter {self.name} is hunting based on hypothesis: {self.hypothesis}"
    
    def __str__(self):
        return (f"[Threat Hunter] {self.name} | Clearance: {self.clearance}\n"
                f"  Hypothesis: {self.hypothesis}\n"
                f"  IOCs Tracked: {len(self.ioc)}\n"
                f"  Pivots: {len(self.pivot_trail)}")
            

hunter = ThreatHunter(
    name="Stephen",
    clearance=3,
    tools=["Splunk", "Velociraptor", "MISP"],
    shift="night"
)

hunter.build_hypothesis("Ransomware spreading via phishing email attachment")
hunter.add_ioc("suspicious_attachment.exe")
hunter.add_ioc("185.220.101.45")  # known ransomware C2 IP
hunter.add_ioc("encrypt_files.bat")
hunter.hunt()
hunter.pivot("Found lateral movement to finance server")
hunter.pivot("Discovered encrypted files on 3 workstations")
hunter.pivot("Traced back to phishing email from hr@fakecorp.com")
print(hunter)