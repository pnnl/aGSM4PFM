
# AMR4PF — Adaptive Mesh Refinement for Phase Field modeling

**AMR4PF** is an adaptive mesh refinement demo for interface tracking in phase field modeling written by python script. The main contribution is from an outstanding high school student, Alice Xu, who transfered the Matlab code into Python version for best accessibility without license requirement. Please encorage.
This scripts tracking the interface movement of a circular interface (not driven by real phase field modeling) as a toy example to showcase the performance of the proposed hierarchic AMR algorithm.


<img width="700" alt="Allan-Cahn Simulation" src="https://github.com/pnnl/aGSM4PFM/blob/master/AMR4PF/result.gif">  

---


## 🚀 Quick Start

to run the code, please use the command in terminal:
python main_program.py

It will generate a gif animation file.

---

## ⚙️ Simulation Parameters
The controllable parameters locate in lines 15-25 in the main_program.py

### Resolution of Coarsest Mesh N 

* Number of grid points in one spatial direction.
* Controls base grid resolution.

### Gradient Energy Coefficient eta

* Determines interface thickness.
* Larger eta → smoother, thicker interfaces.

### Refinement Level n_level

* Controls adaptive mesh resolution.
* Higher values increase accuracy and computational cost.

### Interface Threshold cri

* Defines regions eligible for adaptive refinement.
* Typically based on interface gradient or phase variation.


---

Authors:
Alice Xu (Hanford High School), Zirui Mao (PNNL)

## 🤝 Contributing

Contributions are welcome:

* Bug reports
* Algorithm improvements
* Documentation enhancements
---
