# -*- coding: utf-8 -*-
"""

@author: khan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from animation import animate_t_handle

# ============================================================
# Physical parameters
# ============================================================

lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.4

# ============================================================
# Simulation parameters
# ============================================================

tf = 10
dt = 0.005

t_eval = np.linspace(0, tf, int(tf/dt) + 1)

# Initial conditions

omega10 = 0.1
omega20 = 15
omega30 = 0.1

psi0 = 0
theta0 = np.pi / 2
phi0 = 0

Y0 = [omega10, omega20, omega30,
      psi0, theta0, phi0]

# ============================================================
# Differential equations
# ============================================================

def t_handle_dynamics(t, Y):

    omega1, omega2, omega3, psi, theta, phi = Y

    # Euler rigid body equations

    domega1 = ((lambda2 - lambda3) / lambda1) * omega2 * omega3

    domega2 = ((lambda3 - lambda1) / lambda2) * omega3 * omega1

    domega3 = ((lambda1 - lambda2) / lambda3) * omega1 * omega2

    # 3-1-3 Euler angle kinematics

    sin_theta = np.sin(theta)

    # Avoid division by zero
    if abs(sin_theta) < 1e-8:
        sin_theta = 1e-8

    dpsi = (
        omega1 * np.sin(phi)
        + omega2 * np.cos(phi)
    ) / sin_theta

    dtheta = (
        omega1 * np.cos(phi)
        - omega2 * np.sin(phi)
    )

    dphi = omega3 - np.cos(theta) * dpsi

    return [
        domega1,
        domega2,
        domega3,
        dpsi,
        dtheta,
        dphi
    ]

# ============================================================
# Numerical integration
# ============================================================

solution = solve_ivp(
    t_handle_dynamics,
    [0, tf],
    Y0,
    t_eval=t_eval,
    rtol=1e-6,
    atol=1e-6
)

# ============================================================
# Extract results
# ============================================================

t = solution.t

omega1 = solution.y[0]
omega2 = solution.y[1]
omega3 = solution.y[2]

psi = solution.y[3]
theta = solution.y[4]
phi = solution.y[5]

# ============================================================
# Mechanical energy
# ============================================================

E = 0.5 * (
    lambda1 * omega1**2
    + lambda2 * omega2**2
    + lambda3 * omega3**2
)

plt.figure(figsize=(8, 5))

plt.plot(t, E, linewidth=2)

plt.xlabel('Time (s)')
plt.ylabel('Mechanical Energy (J)')

plt.title('Total Mechanical Energy')

plt.grid(True)

# ============================================================
# Angular momentum
# ============================================================

H1 = lambda1 * omega1
H2 = lambda2 * omega2
H3 = lambda3 * omega3

H = np.sqrt(H1**2 + H2**2 + H3**2)

plt.figure(figsize=(8, 5))

plt.plot(t, H1, label='H1')
plt.plot(t, H2, label='H2')
plt.plot(t, H3, label='H3')

plt.plot(t, H, linewidth=2, label='|H|')

plt.xlabel('Time (s)')
plt.ylabel('Angular Momentum')

plt.title('Angular Momentum Components')

plt.legend()

plt.grid(True)

plt.show()

# ============================================================
# Animate motion
# ============================================================

animate_t_handle(psi, theta, phi, dt)