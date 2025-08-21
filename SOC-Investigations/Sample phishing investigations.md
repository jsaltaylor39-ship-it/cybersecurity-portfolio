#  Phishing Investigation Report 

**Platform**  
Email / Windows Environment

**Investigation**  
Phishing Email Analysis

**Date**  
08/21/2025

**Analyst**  
Jessica Taylor

---

## 1. Objectives
- **Identify phishing emails targeting the organization**  
- **Analyze email headers, links, and attachments**  
- **Mitigate risk and provide recommendations**  

---

## 2. Setup
- **Tools used:** Outlook test environment, Wireshark, VirusTotal, PhishTool  
- **Network/Environment:**  
  - Isolated VM for email testing  
  - Monitoring system capturing outbound connections  
  - Logging enabled to track any user interaction  

---

## 3. Findings
- **Suspicious email identified:** Spoofed sender address mimicking internal HR  
- **Payload:** Malicious link attempting credential harvest  
- **Indicators of Compromise (IOCs):**  
  - Sender IP: 192.168.100.25 (external, suspicious)  
  - URLs: http://malicious-site.test/login  
  - Attachment hash flagged on VirusTotal  
- **User behavior:** No users clicked the link during test simulation  
- **Mitigation applied:** Email quarantined, IOC list updated, users alerted  

---

## 4. Lessons Learned
- **Email header analysis** is essential to detect spoofed senders  
- **Testing in isolated environments** prevents accidental compromise  
- **Educating users** reduces the risk of phishing success  
- **Documenting IOCs** helps improve SOC response for future attacks  
