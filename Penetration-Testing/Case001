#  Penetration Test Report – Lab 01

**Engagement:** HackTheBox / TryHackMe Lab  
**Date:** 2025-08-21  
**Tester:** Jessica Taylor  

---

## 1. Scope
- **Target system(s):** 10.10.10.50 / Lab VM  
- **Rules of engagement:** Lab environment only, no production systems  

---

## 2. Methodology
1. **Reconnaissance:** Network scanning and service discovery using `nmap`  
2. **Enumeration:** Identifying users, open ports, and services  
3. **Exploitation:** Using SQLmap to exploit SQL Injection vulnerability  
4. **Post-exploitation:** Collecting information, retrieving flags  
5. **Privilege escalation:** Gaining higher-level access to system  

---

## 3. Findings

| Vulnerability     | CVSS Score | Exploitation Method       | Impact              | Remediation              |
|------------------|------------|---------------------------|-------------------|-------------------------|
| SQL Injection     | 8.1 (High) | SQLmap + reverse shell    | Full database dump | Use parameterized queries |
| Weak SMB Config   | 6.5 (Medium)| smbclient enumeration    | Sensitive file exposure | Harden SMB configurations |

---

## 4. Proof of Concept
- Screenshots of shells or flags captured during exploitation  
- Command output demonstrating vulnerability  

---

## 5. Conclusion
- Lab exposed critical vulnerabilities in SQL and SMB services  
- Highlights importance of **input validation**, **secure configuration**, and **regular patching**  
- Lessons learned: Always test in a controlled environment and document methodology
