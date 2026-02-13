# aGSM4PFM

# Nearest Neighboring Particles Searching (NNPS) algorithms for Smoothed Particle Hydrodynamics method
This algorithm serves as an efficient neighbors searching operator that can be easily integrated into the Smoohthed Particle Hydrodynamics (SPH) method. This algorithm is designed to utilize low-precision float-point 16 computation on GPU for efficiency purpose. To maintain the NNPS accuracy while using the low-precision FP16 computation, a cell-based relative coordinate link list (RCLL) algorithm is developed.

The RCLL algorithms exhibits a 1.5x efficiency improvement over the standard FP64 GPU computation, and its efficiency can be further boosted by 2.7x through optimizing GPU memory bandwidth utilization.


## Source code
**1: CPU code of all-list NNPS algorithm**


The source code 'SPH_RCLL_GPU_FP16_sort.cu' is a optimized version of the 'SPH_RCLL_GPU_FP16.cu'. It sorts the particles based on their spatial distribution. 

In this way, the GPU memory bandwidth can be utilized more effectively in GPU parallel computation.

To compile the CUDA code on GPUs, using: nvcc SPH_RCLL_GPU_FP*.cu -o SPH_RCLL_GPU_FP* -arc=sm_80 -use_fast_math

TO compile the optimized FP16 code, using: ncvv --extended-lambda -std=c++14 -arch=sm_80  SPH_RCLL_GPU_FP16_sort.cu -o SPH_RCLL_GPU_FP16

To run it, using: ./SPH_RCLL_GPU_FP*




## Authors
(Zirui Mao)[zirui.mao@pnnl.gov] (PNNL)

## Citation
Please cite our [Paper](to be filled later).

## License
This project is licensed under the BSD license, see [license](https://github.com/pnnl/lpNNPS4SPH/blob/master/LICENSE.txt)  for details.

## Acknowledgements
**PNNL-IPID:*******

This material is based upon work supported by the LDRD project in PNNL. This research used resources of the HPC Deception cluster in PNNL. The Pacific Northwest National Laboratory (PNNL) is operated by Battelle for the U.S. Department of Energy under Contract DE-AC05-76RL01830.
