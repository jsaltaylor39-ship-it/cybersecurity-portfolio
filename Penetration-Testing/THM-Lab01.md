#  Penetration Test – TryHackMe Lab 01

**Target:** THM “Intro Linux” Lab  
**Date:** 2025-08-15  
**Tester:** Your Name  

---

## 1. Scope
- Target VM: 10.10.200.15  
- Lab environment only  

---

## 2. Methodology
1. **Recon:** nmap scan – open ports: 22 (SSH), 80 (HTTP)  
2. **Enumeration:** Found default web page and SSH login  
3. **Exploitation:** SSH brute force with known credentials  
4. **Post-exploitation:** Captured user.txt flag  

---

## 3. Findings
| Vulnerability | CVSS | Exploitation Method | Impact | Remediation |
|---------------|------|------------------|--------|------------|
| Weak SSH creds | 7.0 | Brute force | User access gained | Enforce strong passwords |
| Default web config | 5.5 | Enumeration | Information leakage | Remove default pages |

---

## 4. Conclusion
- Highlights importance of password hygiene and removing default web content
