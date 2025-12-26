# E-Commerce-Resilience-Credit-Risk-Management-System
A dual-purpose project showcasing a robust Credit Scoring Model integrated with a comprehensive Risk Management Framework for E-commerce operations.
##  Operational Risk Register
| ID | Risk Description | Category | Impact | Likelihood | Mitigation Strategy |
|:---|:---|:---|:---|:---|:---|
| R01 | Payment Gateway Failure | Technical | 5 | 2 | **Contingency:** Immediate failover to Cash on Delivery (COD). |
| R02 | Key Developer Resignation | Human | 5 | 2 | **Mitigation:** Comprehensive code documentation & pre-emptive hiring/cross-training. |
| R03 | Data Staleness | Data | 4 | 4 | **Mitigation:** Implementing automated monthly data refresh pipelines. |
##  Problem Solving: The 5 Whys Technique
In this project, I apply the **5 Whys** method to identify and fix root causes. 

**Example Scenario:** The Credit System is rejecting all users.
1. **Why?** The input income values are all zeros.
2. **Why?** The data bridge between the App and the Model is broken.
3. **Why?** A field name was changed in the UI update without updating the backend.
4. **Why?** Lack of synchronization between front-end and back-end teams.
5. **Root Cause:** Absence of a **Change Management Protocol**.

**Action Plan:** Implemented **Automated Integration Tests** to validate data integrity after every update.
