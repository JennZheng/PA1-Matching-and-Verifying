# PA1-Matching-and-Verifying
COP4533 Programing Assignment 1: Implementing Gale-Shapley

# Team
Jennifer Zheng: 52838059  
Srinitha Srikanth: 55178917

# Repository Structure
PA1-Matching-and-Verifying/  
│  
├─ matching.py         # Task A: Hospital-proposing Gale-Shapley algorithm  
├─ verifier.py         # Task B: Validity and stability checker  
├─ scaler.py           # Task C: Measures running time and graphs  
├─ test/               # Automatically generated input files for Task C  
├─ results/            # Outputs of timing measurements and graph  
├─ example.in          # Sample input file  
├─ example.out         # Sample output file  
└─ README.md

# Dependencies
Python3  
matplotlib for the scaler (install w/: pip install matplotlib)

# How to Run
For matching.py run:  
(Using VSCode Powershell)  
Get-Content example.in | python matching.py > example.out  
  
(Using Windows Command Prompt (CMD) or Mac/Linux Terminal)  
python matching.py < example.in > example.out  

For verfier.py run:  
python verifier.py  
- then follow the prompts for inputing the inputs and outputs (example.in/example.out)

For scaler.py run:  
python scaler.py

# Task C
The results for task C are located in the results file.  
Viewing the trends for both the matcher (blue) and verifier (orange) it can be seen that as n grows larger, the time it takes to run grows as well. Overall, both exhibit O(n^2) runtime growth which is consistent with what is expected for the Gale-Shapely algorithm.

<img width="479" height="409" alt="image" src="https://github.com/user-attachments/assets/cad8f3cc-2bc4-4ba7-a9f5-098f020fd508" />


