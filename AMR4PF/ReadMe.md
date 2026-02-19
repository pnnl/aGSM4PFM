# AMR4PF — Adaptive Mesh Refinement (AMR) Demo for Phase-Field Interface Tracking

**AMR4PF** is a Python demo that showcases a hierarchical **adaptive mesh refinement (AMR)** strategy for interface tracking for phase-field modeling. The example tracks the motion of a circular interface (a *toy problem*; not a full physical phase-field simulation) to illustrate refinement behavior and performance.

A major contribution to this python code comes from an outstanding high student intern **Alice Xu**, who translated the original MATLAB implementation into Python to improve accessibility and remove proprietary license requirements.

<p align="center">
  <img width="700" alt="AMR4PF interface tracking animation" src="https://github.com/pnnl/aGSM4PFM/blob/master/AMR4PF/result.gif">
</p>

---

## Features
- Hierarchical AMR for 2D interface tracking
- Simple, lightweight Python implementation
- Produces an animated GIF of the evolving interface and mesh refinement

---

## Quick Start

### Requirements
- Python 3.x  
- Common packages (e.g., `numpy`, `matplotlib`) as used in the scripts

### Run
From the repository directory:
```bash
python main_program.py
```
This will generate an animated GIF (see output path/message printed by the script).

---

## Configuration / Simulation Parameters

Key parameters are defined in **`main_program.py` (approximately lines 15–25)**.

### Coarsest mesh resolution (`N`)
- Number of grid points in one spatial direction.
- Controls the base (coarsest) grid resolution.

### Gradient energy coefficient (`eta`)
- Controls the effective interface thickness.
- Larger `eta` → smoother and thicker interfaces.

### Refinement level (`n_level`)
- Number of refinement levels used by AMR.
- Higher values increase resolution near the interface (and increase computational cost).

### Interface refinement threshold (`cri`)
- Criterion for selecting cells/regions eligible for refinement.
- Typically based on interface gradient magnitude or phase variation.

---

## Authors
- **Alice Xu** (Hanford High School)  
- **Zirui Mao** (Pacific Northwest National Laboratory, PNNL)

---

## Contributing
Contributions are welcome, including:
- Bug reports and fixes
- Algorithm and performance improvements
- Documentation updates and usage examples

Please open an issue or submit a pull request.

--- 

If you want, I can also add sections for **License**, **Citation**, and **Repository structure** (files/folders) once you tell me what license you plan to use and whether there’s a preferred citation format.
