# aGSM4PFM

<img width="500" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_AC.gif"> <img width="500" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Ani_CH.gif">
Animations of aGSM simulation for Allan-Cahn equation (left) and Cahn-Hillard equation (right).


# Adaptive Gradient Smoothing Method for Phase Field Modeling
This repository offers a high-performance numerical solver utilizing the [Gradient Smoothing Method](https://www.worldscientific.com/worldscibooks/10.1142/13508#t=aboutBook) (GSM) combined with adaptive remeshing of structured meshes for efficient Phase Field modeling of interface dynamics. The solver achieves general second-order accuracy and features a computational complexity of O(N), meaning the calculation time scales linearly with the number of elements. Numerical experiments demonstrate that the solver consistently outperforms existing weak-form Finite Element Method (FEM)-based software (including adaptive mesh approaches) across all test cases. Additionally, it provides significant advantages over traditional uniform-mesh-based strong-form Finite Difference methods, particularly for large-scale problems with thin interface.

<img width="600" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Performance.png">

<img width="600" alt="image" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/PF-Mesh.png">

## Source code
**1: CPU code of all-list NNPS algorithm**


The source code 'SPH_RCLL_GPU_FP16_sort.cu' is a optimized version of the 'SPH_RCLL_GPU_FP16.cu'. It sorts the particles based on their spatial distribution. 

In this way, the GPU memory bandwidth can be utilized more effectively in GPU parallel computation.

To compile the CUDA code on GPUs, using: nvcc SPH_RCLL_GPU_FP*.cu -o SPH_RCLL_GPU_FP* -arc=sm_80 -use_fast_math

TO compile the optimized FP16 code, using: ncvv --extended-lambda -std=c++14 -arch=sm_80  SPH_RCLL_GPU_FP16_sort.cu -o SPH_RCLL_GPU_FP16

To run it, using: ./SPH_RCLL_GPU_FP*




## Authors
[Zirui Mao] (PNNL)  zirui.mao@pnnl.gov

## Citation
Please cite our [Paper](to be filled later).

## License
This project is licensed under the BSD license, see [license](https://github.com/pnnl/lpNNPS4SPH/blob/master/LICENSE.txt)  for details.

## Acknowledgements
**PNNL-IPID:*******

This material is based upon work supported by the LDRD project in PNNL. This research used resources of the HPC Deception cluster in PNNL. The Pacific Northwest National Laboratory (PNNL) is operated by Battelle for the U.S. Department of Energy under Contract DE-AC05-76RL01830.
