Rotating T-Handle Dynamics Simulation (MATLAB + Python)

This project simulates the 3D rotational dynamics of a rigid T-shaped body (T-handle) using Euler’s equations of rigid body motion and 3-1-3 Euler angle kinematics. The system evolves freely in space with no external torque, making it a classical demonstration of angular momentum conservation and rigid body dynamics instability.

The project includes both:

MATLAB implementation (original thesis version)
Python implementation (converted version for reproducibility and visualization)
Physical Model

The T-handle is modeled as a rigid body with principal moments of inertia:

λ₁ = 0.2 kg·m²
λ₂ = 0.3 kg·m²
λ₃ = 0.4 kg·m²

The motion follows:

1. Euler’s Equations (Torque-free rotation)

In the body-fixed frame:

dH/dt + ω × H = 0
where H = Iω

This leads to nonlinear coupled differential equations describing rotational motion.

2. Angular Velocity Kinematics (3-1-3 Euler angles)

The orientation of the rigid body is described using Euler angles:

ψ (precession)
θ (nutation)
φ (spin)

These define the transformation between the inertial frame and the body frame.

Numerical Method
ODE solver: ode45 (MATLAB) / solve_ivp (Python)
Time step: dt = 0.005 s
Total simulation time: 10 s
Initial conditions: asymmetric angular velocity to induce rotational instability
Key Physical Quantities
Total Mechanical Energy

The kinetic energy of rotation is:

E = ½ (λ₁ω₁² + λ₂ω₂² + λ₃ω₃²)

Since there is no external torque, the system is conservative and:

✔ Total energy remains constant over time
✔ Numerical fluctuations may appear due to discretization

Angular Momentum About the Center of Mass

The angular momentum components are:

H₁ = λ₁ω₁
H₂ = λ₂ω₂
H₃ = λ₃ω₃

Magnitude:

|H| = √(H₁² + H₂² + H₃²)

Physical interpretation:
Angular momentum is conserved in absence of external torque
Components change due to rotation in the body frame
The magnitude remains constant (ideal case)
🔹 Total Angular Momentum Conservation

✔ In inertial space: total angular momentum vector is conserved
✔ In body frame: components vary due to rotation
✔ This is a key demonstration of rigid body dynamics

Animation

The 3D animation shows:

Orientation evolution of the T-handle
Rotation of principal axes (e₁, e₂, e₃)
Motion reconstructed from Euler angles
Real-time rigid body tumbling behavior

Results

(Add your figures here in GitHub)

Suggested images to include:

Energy vs Time plot
Angular momentum components
3D animation screenshots
Initial vs final orientation
