#  SOC Investigation Report – Case 03

**Case ID:** SOC-003  
**Date:** 2025-08-15  
**Analyst:** Jessica Taylor  

---

## 1. Executive Summary
- **Incident type:** Unauthorized login attempts  
- **Affected system(s):** Remote VPN servers  
- **Impact:** Attempted credential brute force; no accounts compromised  
- **Status:** Mitigated  

---

## 2. Investigation Details
- **Detection source:** VPN logs & SIEM anomaly detection  
- **Timeline:**
  - 02:00 AM: Multiple failed logins detected  
  - 02:10 AM: SOC notified  
  - 02:30 AM: IP addresses blocked and MFA enforced  
- **Logs reviewed:** VPN logs, SIEM alerts  
- **Indicators of Compromise (IoCs):**
  - Source IPs: `203.0.113.45, 198.51.100.32`  
  - Username attempts: `admin, finance, hr`  

---

## 3. Findings
- Brute force attempts likely external attacker  
- MFA prevented account compromise  
- Logs indicate automated attack patterns  

---

## 4. Recommendations
- Continue enforcing MFA  
- Enable account lockout policies  
- Review VPN logs weekly for anomalies
