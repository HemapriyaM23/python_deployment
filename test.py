sed -i 's/pa_matillion_master\.ksh PALIGN DEV\(.*\) PFZALGN_DEV PFZALGN_DEV/pa_matillion_master.ksh PALIGN TEST\1 PFZALGN_TEST PFZALGN_TEST/g' "${jilFile}"
Based on the provided images, here is the completed table with the required details for the support team, their leads, and the DevOps team:

## Role Creation Table

| Role Name Convention | Process/Proj Level | SSO | Comments |
|----------------------|--------------------|-----|----------|
| **Support Team**     |                    |     |          |
| Support              | Process Level      | CUSPFE-RAPID-CUSTOMER-SFA-SUPPORT-RW | Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT |
| Support Lead         | Process Level      | CUSPFE-RAPID-CUSTOMER-SFA-SUPPORT-LEAD-RW | Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT |
| **DevOps Team**      |                    |     |          |
| DevOps               | Process Level      | CUSPFE-RAPID-CUSTOMER-SFA-DEVOPS-RW | Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT |
| DevOps Lead          | Process Level      | CUSPFE-RAPID-CUSTOMER-SFA-DEVOPS-LEAD-RW | Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT |

### Comments

- **Role Name Convention**: The role names should follow the convention: `CUSPFE-RAPID-CUSTOMER-SFA-<proj/process name>-<role type>-RW`.
- **Process/Proj Level**: Roles at the process level should generally have read-only access except for DevOps and Production Support roles.
- **SSO**: Single Sign-On (SSO) names should be constructed as shown in the examples provided.

### Examples

- **Support Team**:
  - Support: `CUSPFE-RAPID-CUSTOMER-SFA-SUPPORT-RW`, Comment: Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT
  - Support Lead: `CUSPFE-RAPID-CUSTOMER-SFA-SUPPORT-LEAD-RW`, Comment: Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT

- **DevOps Team**:
  - DevOps: `CUSPFE-RAPID-CUSTOMER-SFA-DEVOPS-RW`, Comment: Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT
  - DevOps Lead: `CUSPFE-RAPID-CUSTOMER-SFA-DEVOPS-LEAD-RW`, Comment: Process Level Should always have Read only except DevOps/Production Support. Process Exp: DEV, QA, RPT

These conventions ensure that roles are clearly defined and appropriately assigned privileges based on their responsibilities.

Sources
[1] image.jpg https://pplx-res.cloudinary.com/image/upload/v1722865852/user_uploads/qfbyysmnj/image.jpg
[2] image.jpg https://pplx-res.cloudinary.com/image/upload/v1722865913/user_uploads/dyohhudah/image.jpg
