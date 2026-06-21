\# AI-Powered Candidate Ranking System



\## Overview



This project was developed for the Data \& AI Challenge.



The objective is to identify and rank the most suitable candidates for a job role using candidate profile information, skills, experience, and recruiter engagement signals.



\## Dataset



The dataset contains:



\* Candidate Profiles

\* Career History

\* Education

\* Skills

\* Certifications

\* Languages

\* Recruiter Signals



Total Records: 100,000 Candidates



\## Methodology



\### Feature Engineering



The following features were extracted:



\* Years of Experience

\* AI Skill Count

\* Recruiter Response Rate

\* GitHub Activity Score



\### Scoring Formula



Score =

(AI Skill Count × 10)



\* (Experience × 2)

\* (Recruiter Response Rate × 20)

\* GitHub Activity Score



\### Ranking Process



1\. Load candidate dataset

2\. Extract relevant features

3\. Calculate candidate scores

4\. Sort candidates by score

5\. Apply tie-breaking using candidate\_id

6\. Select Top 100 candidates

7\. Generate submission CSV



\## Output



The final output contains:



\* candidate\_id

\* rank

\* score

\* reasoning



The submission file successfully passes the official validation script.



\## Technologies Used



\* Python

\* Pandas

\* JSON

\* VS Code



\## Author



Akarapu Madhu Shalini



