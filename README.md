# Rotating T-Handle Dynamics Simulation (MATLAB + Python)

This project simulates the 3D rotational dynamics of a rigid T-shaped body (T-handle) using Euler’s equations of rigid body motion and 3-1-3 Euler angle kinematics.

---

## Physical Model

The T-handle is modeled as a rigid body with principal moments of inertia:

- λ₁ = 0.2 kg·m²
- λ₂ = 0.3 kg·m²
- λ₃ = 0.4 kg·m²

---

## Results

### Total Mechanical Energy

The kinetic energy of rotation is:

E = ½ (λ₁ω₁² + λ₂ω₂² + λ₃ω₃²)

Since there is no external torque:

- Total energy remains constant
- Small numerical fluctuations may appear

### Energy Conservation Plot

![Energy Plot](images/energy_plot.png)

---

## Angular Momentum About the Center of Mass

Angular momentum components:

- H₁ = λ₁ω₁
- H₂ = λ₂ω₂
- H₃ = λ₃ω₃

Magnitude:

|H| = √(H₁² + H₂² + H₃²)

Physical interpretation:

- Angular momentum is conserved
- Components vary in body coordinates
- Magnitude remains constant

### Angular Momentum Plot

![Angular Momentum](images/angular_momentum.png)

---

## 3D T-Handle Motion

The animation shows:

- Orientation evolution
- Principal axis motion
- Tumbling behavior

### Animation Snapshots

![3D Motion](images/t_handle_animation.png)

---

## Repository Structure

```text
project-msc/
│
├── matlab code/
├── python/
├── images/
│   ├── energy_plot.png
│   ├── angular_momentum.png
│   └── t_handle_animation.png
│
└── README.md
