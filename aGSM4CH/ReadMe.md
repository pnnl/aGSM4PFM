# aGSM4CH — Adaptive Gradient-Stabilized Mesh Solver for the Cahn–Hilliard Equation

**aGSM4CH** is a graphical simulation framework for solving the Cahn–Hilliard phase-field equation using adaptive mesh refinement:

$$
\frac{\partial c}{\partial t} = \nabla^2 (c^3 - c - \kappa \nabla^2 c)
$$

The application enables users to configure simulation parameters, execute adaptive simulations, and export animations of phase separation dynamics with MATLAB.

<img width="700" alt="Allan-Cahn Simulation" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Panel_CH.png">  

---

## ✨ Features

* Adaptive mesh refinement for interface-resolved simulations
* GUI-based workflow — no scripting required
* Compiled standalone application (MATLAB not required)
* Optional GIF animation export
* Designed for research, teaching, and algorithm demonstration

---

## 📦 Installation

### Option A — Without MATLAB

1. Download the compiled release package.
2. Double-click: [MyAppInstaller.exe](https://github.com/pnnl/aGSM4PFM/blob/master/MyAppInstaller.exe)


3. Follow the installer instructions.

4. Navigate to build/PFMApp4CH.exe

✅ MATLAB is **NOT required**.
The installer automatically installs all necessary runtime components.

---

### Option B — With MATLAB Installed

1. Navigate to:

```
release/src/
```

2. Launch:

```
main_program.m
```

---

## 🚀 Quick Start

1. Launch **aGSM4AC** from the desktop or Start Menu.
2. Configure simulation parameters.
3. Click **RUN** to start the simulation.
4. View results in the visualization window.

---

## ⚙️ Simulation Parameters

Set parameters using the **Parameters Panel**:

### Resolution of Coarsest Mesh

* Number of grid points in one spatial direction.
* Determines base mesh resolution.

### Gradient Energy Coefficient (κ)

* Controls interfacial thickness.
* Larger values produce thicker, smoother interfaces.

### Refinement Level

* Determines adaptive mesh density.
* Higher levels increase resolution and computational cost.

### Interface Threshold

* Defines regions where mesh refinement is applied.
* Typically linked to interface gradients.

### Total Physical Time

* Specifies total simulation duration.

---

## 🎬 Exporting Animations

To save simulation animations:

1. Enable **Export as GIF**
2. Enter a file name
3. Run the simulation

The animation will be saved in the program working directory.

---

## ▶️ Running the Simulation

1. Click **RUN**
2. Initialization may take a few seconds — this is normal
3. Progress bar will begin updating
4. Simulation plots will appear automatically

---

## ⏹️ Stopping a Simulation

To stop the run early:

```
Click STOP
```

---

## 📊 After Simulation Completion

* The final solution remains displayed in the GUI.
* If GIF export was enabled, the animation file is already saved.

---

## ❌ Closing the Program

Close the application window normally.

---

## 📁 Example Project Structure

```
build/
└── PFMApp4CH.exe

src/
 └── main_program.m
```

---

## 🧪 Intended Applications

* Phase separation modeling
* Cahn–Hilliard dynamics
* Adaptive mesh method research
* Interface evolution studies
* Numerical method demonstrations

---

## 🤝 Contributing

Contributions are welcome:

* Bug reports
* Algorithm improvements
* Documentation enhancements
---
