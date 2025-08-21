#  Cloud Security Lab Report – GCP Firewall & IAM Lab

**Platform**  
GCP

**Lab**  
Firewall & IAM Configuration Lab

**Date**  
08/21/2025

**Analyst**  
Jessica Taylor

---

## 1. Objectives
- **Configure firewall rules** to restrict inbound and outbound traffic  
- **Apply IAM roles** following the principle of least privilege  
- **Test access from restricted IP addresses**  

---

## 2. Setup
- **Services used:** Compute Engine, VPC Firewall, IAM  
- **Network/Architecture:**  
  - Private subnet with test VM  
  - Firewall rules configured for SSH, HTTP, and limited custom ports  
  - IAM roles assigned to test users  
- **Architecture Diagram:**  
![GCP Firewall Architecture](../docs/gcp-firewall-architecture.png)  

---

## 3. Findings
- **Default firewall rules** were overly permissive and allowed SSH from any IP  
- **Custom firewall rules** restricted access to authorized IP addresses only  
- **IAM roles** successfully limited permissions according to least privilege principles  
- **Test results:** Unauthorized access attempts were blocked; logging captured all attempted connections  

---

## 4. Lessons Learned
- **Firewall rules must be carefully scoped** to reduce attack surface  
- **IAM enforcement prevents unauthorized access** to resources  
- **Testing configurations in a lab environment** ensures proper security before production deployment  
- **Hands-on practice** reinforced the importance of combining network and identity controls for cloud security

