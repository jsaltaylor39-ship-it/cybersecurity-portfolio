#  Cloud Security Lab Report – [Lab 0001]

**Platform**  
[AWS / Azure / GCP]

**Lab**  
[0001]

**Date**  
[08/21/2025]

**Analyst**  
[Jessica Taylor]

---

## 1. Objectives
- **Configure IAM users, groups, and policies**  
- **Enable monitoring and logging**  
- **Test least privilege access**  

---

## 2. Setup
- **Services used:** EC2, S3, IAM, CloudTrail (for AWS example)  
- **Network/Architecture:**  
  - Single VPC with public and private subnets  
  - Test VM for validating access controls  
  - IAM roles assigned to groups  
- **Architecture Diagram:**  
![Architecture Diagram](../docs/[diagram-file-name].png)  

---

## 3. Findings
- **Misconfigurations identified:** Some IAM users had overly permissive policies granting access to all S3 buckets  
- **Security controls applied:** Least privilege policies applied, removing excessive permissions  
- **Access testing:** Attempted unauthorized access to restricted resources was blocked successfully  
- **Logging and monitoring:** CloudTrail / Audit logs captured all access attempts and policy changes  
- **Potential risk mitigated:** Unauthorized data access or accidental modification of critical resources  

---

## 4. Lessons Learned
- **Least privilege enforcement** is critical to reduce risk of compromise  
- **Logging and monitoring** are essential for detecting unauthorized access attempts  
- **Periodic policy reviews** help maintain secure access over time  
- **Hands-on practice** reinforces how cloud IAM, firewall, and logging controls work together 
