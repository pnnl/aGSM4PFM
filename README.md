# aGSM4PFM

<img width="500" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_AC.gif"> <img width="500" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_CH.gif">
Fig. 1 Animations of aGSM simulation for Allan-Cahn equation (left) and Cahn-Hillard equation (right).


# Adaptive Gradient Smoothing Method for Phase Field Modeling
This repository offers a high-performance numerical solver utilizing the [Gradient Smoothing Method](https://www.worldscientific.com/worldscibooks/10.1142/13508#t=aboutBook) (GSM) combined with adaptive remeshing of structured meshes for efficient Phase Field modeling of interface dynamics. The solver achieves general second-order accuracy and features a computational complexity of O(N), meaning the calculation time scales linearly with the number of elements. Numerical experiments demonstrate that the solver consistently outperforms existing weak-form Finite Element Method (FEM)-based software (including adaptive mesh approaches) across all test cases. Additionally, it provides significant advantages over traditional uniform-mesh-based strong-form Finite Difference methods, particularly for large-scale problems with thin interface.

<img width="600" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Performance.png">
Fig. 2 Accuracy (a) and computational complexities (b) of aGSM compared to Finite Difference Method (FDM) and Finite Element Method (FEM)-based software MOOSE.

<img width="600" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/PF-mesh.png">
Fig. 3 The meshes used in FDM(b), aGSM(c), and MOOSE(d) in computation for the cases with difference interface thickness (a).

## Source code
The Matlab source code that implements aGSM for solving the phase field equations, including A-C and C-H models are stored. Note that, Matlab license is needed to run the source code. To make it more accessible to users without license, an executible file is provided as well to allow exploring the algorithm freely.  



## Authors
[Zirui Mao](https://maozirui.github.io/) (PNNL)  zirui.mao@pnnl.gov

## Citation
Please cite our [Paper](to be filled later).

## License
This project is licensed under the BSD license, see [license](https://github.com/pnnl/lpNNPS4SPH/blob/master/LICENSE.txt)  for details.

## Acknowledgements
**PNNL-IPID:*******

This material is based upon work supported by the LDRD project in PNNL. This research used resources of the HPC Deception cluster in PNNL. The Pacific Northwest National Laboratory (PNNL) is operated by Battelle for the U.S. Department of Energy under Contract DE-AC05-76RL01830.
