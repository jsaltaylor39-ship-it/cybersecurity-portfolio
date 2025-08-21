#  Cloud Security Lab – AWS IAM

**Lab:** AWS Identity and Access Management (IAM)  
**Date:** 2025-08-21  
**Analyst:** Jessica Taylor  

---

## 1. Objectives
- Configure IAM users, groups, and roles  
- Apply least privilege principles  
- Enable MFA for sensitive accounts  

---

## 2. Setup
- AWS Account: Lab environment  
- Services used: IAM, S3, CloudTrail  
- Architecture: Single VPC with multiple IAM roles  

---

## 3. Findings
- Created groups: Admins, Developers, Auditors  
- Applied MFA on all admin accounts  
- Policies tested to restrict S3 bucket access  

---

## 4. Lessons Learned
- Least privilege improves security posture  
- MFA significantly reduces account compromise risk  
- Regular audits of IAM roles are essential  
