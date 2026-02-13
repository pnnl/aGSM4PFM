# **aGSM4PFM**  
### Adaptive Gradient Smoothing Method for Phase Field Modeling  

<img width="400" alt="Allan-Cahn Simulation" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_AC.gif">   <img width="400" alt="Cahn-Hillard Simulation" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_CH.gif">  

**Figure 1:** Animations of aGSM simulation for Allan-Cahn equation (left) and Cahn-Hillard equation (right).  

---

## **Overview**
This repository provides a high-performance numerical solver leveraging the [Gradient Smoothing Method (GSM)](https://www.worldscientific.com/worldscibooks/10.1142/13508#t=aboutBook), integrated with adaptive remeshing of structured meshes, for efficient Phase Field modeling of interface dynamics.  

### Key Features:
- **Second-Order Accuracy:** Achieves general 2nd-order accuracy across computations.  
- **Linear Computational Complexity:** Scales as **O(N)**, meaning runtime increases linearly with the number of elements.  
- **Superior Performance:** Outperforms weak-form Finite Element Method (FEM)-based software, including adaptive mesh approaches.  
- **Efficient for Large-Scale Problems:** Exhibits significant advantages over uniform structured strong-form Finite Difference Methods (FDM), especially for thin interfaces or large-scale simulations.  

---

### **Performance Comparison**  
<img width="800" alt="Performance Metrics" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Performance.png">  

**Figure 2:** Accuracy (a) and Computational Complexity (b) of aGSM compared to Finite Difference Method (FDM) and FEM-based software (MOOSE).  

---

### **Mesh Adaptation**  
<img width="850" alt="Mesh Comparison" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/PF-mesh.png">  

**Figure 3:** Meshes used in computation for cases with different interface thickness (a). Comparison between FDM (b), aGSM (c), and MOOSE (d).  


<img width="850" alt="HAMR" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Adaptive-nlevel.png">  

**Figure 4:** Hierarchical adaptive mesh refinement: effect of refinement level on mesh quality

---

## **Source Code**
The repository contains MATLAB source code implementing aGSM for solving phase field equations, including Allan-Cahn (A-C) and Cahn-Hillard (C-H) models.  

**Usage:**  
- **MATLAB License Required:** You will need a MATLAB license to run the provided scripts.  
- **Executable File Available:** For users without access to MATLAB, a standalone executable file is provided, enabling exploration of the algorithm. (Please download and install the MyAppInstaller.exe before running the standalone file) 

---

## **Getting Started**
To use the code, follow these steps:  
1. Clone the repository:  
   ```bash
   git clone https://github.com/pnnl/aGSM4PFM.git
   cd aGSM4PFM
   ```
2. Ensure that MATLAB is installed and licensed.  
3. Run the provided MATLAB scripts or executable file to explore the solver.  

---

## 📁 Project Structure

```
aGSM4PFM
└── aGSM4AC/
    └── build
        └── PFMAPP4AC.exe (standalone file)
    └── src
        └── main_program.m (source code)
└── aGSM4CH/
   └── build
       └── PFMAPP4CH.exe (standalone file)
   └── src
    └── main_program.m (source code)
```


## **Authors**
[**Zirui Mao**](https://maozirui.github.io/)  
Pacific Northwest National Laboratory (PNNL)  
📧 zirui.mao@pnnl.gov  

---

## **Citation**
If you use this code or find it helpful, please cite our upcoming publication:  
[**Paper**](#) *(to be added later)*  

---

## **License**
This project is licensed under the **BSD License**.  
Refer to the [license file](https://github.com/pnnl/lpNNPS4SPH/blob/master/LICENSE.txt) for more details.  

By using this freeware, you are agree to the following:    
   1. you are free to copy and redistribute the material in any medium or format.
   2. you are free to remix, transform, and build upon the material for any personal purpose.
   3. you must provide the name of the creator and attribution parties, a copyright notice, a license notice, paper citation, a  
      disclaimer notice, and a link to the material.
   4. users are entirely at their own risk using this freeware and techniques. 
 
 Before use, please read the License carefully.

---

## **Acknowledgments**
This work is supported by the **PNNL LDRD Project** and utilized resources from the **HPC Deception Cluster** at PNNL.  

> The **Pacific Northwest National Laboratory (PNNL)** is operated by **Battelle** for the U.S. Department of Energy under Contract **DE-AC05-76RL01830.**  

---

### **Feedback & Contributions**
We welcome feedback, issues, or improvements.

---

