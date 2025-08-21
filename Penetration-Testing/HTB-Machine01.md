#  Penetration Test – HackTheBox Machine 02

**Target:** HTB Machine “Lame”  
**Date:** 2025-08-18  
**Tester:** Jessica Taylor 

---

## 1. Scope
- IP: 10.10.10.25  
- Engagement: Lab only  

---

## 2. Methodology
1. **Recon:** nmap scan revealed FTP & HTTP  
2. **Enumeration:** Anonymous FTP allowed read access  
3. **Exploitation:** Uploaded simple PHP reverse shell  
4. **Post-exploitation:** Escalated privileges via local misconfigurations  

---

## 3. Findings
| Vulnerability | CVSS | Exploitation Method | Impact | Remediation |
|---------------|------|------------------|--------|------------|
| Anonymous FTP | 7.5 | Read/write access | Data exposure | Disable anonymous login |
| Weak file permissions | 6.8 | Privilege escalation | Local admin access | Harden permissions |

---

## 4. Conclusion
- Demonstrates importance of proper access control and file permissions
