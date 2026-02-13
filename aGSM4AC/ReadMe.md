# aGSM4AC — Adaptive Gradient-Stabilized Mesh for Allen–Cahn Equation

**aGSM4AC** is an adaptive mesh simulation framework for solving the Allen–Cahn phase-field equation:

$$
\frac{\partial \phi}{\partial t} = -(\phi^3 - \phi) + \kappa \nabla^2 \phi
$$

The software provides a graphical interface for configuring simulation parameters, running adaptive mesh simulations, and exporting animations of phase evolution.
<img width="400" alt="Allan-Cahn Simulation" src="https://github.com/pnnl/aGSM4PFM/blob/master/Figures/Panel_AC.png">  

---

## ✨ Features

* Adaptive mesh refinement for interface-resolved simulations
* Simple GUI-based workflow
* No MATLAB license required for compiled version
* Optional animation export (GIF)
* Designed for research and educational demonstrations of phase-field dynamics

---

## 📦 Installation

### Option A — Without MATLAB (Recommended)

1. Download the compiled release package.
2. Double-click:

```
MyAppInstaller.exe
```

3. Follow the installer instructions.

✅ MATLAB is **NOT required**.
The installer automatically installs all necessary runtime components.

---

### Option B — With MATLAB Installed

1. Navigate to:

```
release/build/
```

2. Launch:

```
PFMApp4AC_v3.exe
```

MATLAB is **not required at runtime**, but having MATLAB installed is compatible.

---

## 🚀 Quick Start

1. Launch **aGSM4AC** from the desktop or Start Menu.
2. Configure simulation parameters.
3. Click **RUN** to start the simulation.
4. View results in the visualization window.

---

## ⚙️ Simulation Parameters

Configure the following parameters in the **Parameters Panel**:

### Resolution of Coarsest Mesh

* Number of grid points in one spatial direction.
* Controls base grid resolution.

### Gradient Energy Coefficient (κ)

* Determines interface thickness.
* Larger κ → smoother, thicker interfaces.

### Refinement Level

* Controls adaptive mesh resolution.
* Higher values increase accuracy and computational cost.

### Interface Threshold

* Defines regions eligible for adaptive refinement.
* Typically based on interface gradient or phase variation.

### Total Physical Time

* Simulation duration in physical time units.

---

## 🎬 Exporting Animations (Optional)

To save an animation:

1. Enable **Export as GIF**
2. Enter a file name
3. Run the simulation

The GIF file will be saved in the program working directory.

---

## ▶️ Running the Simulation

1. Click **RUN**
2. The program may pause briefly during initialization
3. The progress bar will update
4. Visualization will appear automatically

---

## ⏹️ Stopping a Simulation

To stop early:

```
Click STOP
```

---

## 📊 After Simulation Completion

* Final solution remains displayed in the GUI
* If GIF export is enabled, animation is already saved

---

## ❌ Closing the Program

Close the application window normally.

---

## 📁 Project Structure (Example)

```
release/
 └── build/
     └── PFMApp4AC_v3.exe

installer/
 └── MyAppInstaller.exe
```

---

## 🧪 Intended Applications

* Phase-field modeling
* Allen–Cahn equation studies
* Interface evolution problems
* Adaptive mesh algorithm research
* Numerical method demonstrations

---

## 📚 Citation (Suggested Placeholder)

If you use **aGSM4AC** in academic work, please cite:

```
[Author Names], "Adaptive GSM Framework for Allen–Cahn Phase Field Modeling",
Journal/Conference, Year.
```

---

## 📄 License

Specify your project license here:

```
MIT / BSD / GPL / Institutional License
```

---

## 🤝 Contributing

Contributions are welcome:

* Bug reports
* Feature requests
* Algorithm improvements
* Documentation enhancements

---

## 🧑‍💻 Contact

Project Maintainer:

* Name: [Your Name]
* Institution: [Your Institution]
* Email: [your-email]

---

If you want, I can also:

* Convert this into a **high-impact research-software README style** (common for JCP/JOSS repos)
* Add **badges** (build, DOI, license, MATLAB runtime, releases)
* Create a **developer + user dual README**
* Generate a **paper-ready software documentation structure**
* Add a **theory section explaining aGSM vs AMR vs phase-field numerics**

Just tell me 👍.

