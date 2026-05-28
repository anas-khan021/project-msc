# -*- coding: utf-8 -*-
"""

@author: khan
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

# ============================================================
# Animation function
# ============================================================

def animate_t_handle(psi, theta, phi, dt):

    # Dimensions

    LAG = 0.5
    LBC = 4
    LAD = 2

    # Storage arrays

    xA, yA, zA = [], [], []
    xB, yB, zB = [], [], []
    xC, yC, zC = [], [], []
    xD, yD, zD = [], [], []

    # ========================================================
    # Compute orientation
    # ========================================================

    for k in range(len(psi)):

        R1 = np.array([
            [np.cos(psi[k]), np.sin(psi[k]), 0],
            [-np.sin(psi[k]), np.cos(psi[k]), 0],
            [0, 0, 1]
        ])

        R2 = np.array([
            [1, 0, 0],
            [0, np.cos(theta[k]), np.sin(theta[k])],
            [0, -np.sin(theta[k]), np.cos(theta[k])]
        ])

        R3 = np.array([
            [np.cos(phi[k]), np.sin(phi[k]), 0],
            [-np.sin(phi[k]), np.cos(phi[k]), 0],
            [0, 0, 1]
        ])

        R = R3 @ R2 @ R1

        e1 = R[:, 0]
        e2 = R[:, 1]

        A = -LAG * e2

        B = A + (LBC / 2) * e1

        C = A - (LBC / 2) * e1

        D = A + LAD * e2

        xA.append(A[0])
        yA.append(A[1])
        zA.append(A[2])

        xB.append(B[0])
        yB.append(B[1])
        zB.append(B[2])

        xC.append(C[0])
        yC.append(C[1])
        zC.append(C[2])

        xD.append(D[0])
        yD.append(D[1])
        zD.append(D[2])

    # ========================================================
    # Figure setup
    # ========================================================

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim([-LBC, LBC])
    ax.set_ylim([-LBC, LBC])
    ax.set_zlim([-LAD, LAD])

    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')

    ax.set_title('Rotating T-Handle Dynamics')

    ax.grid(True)

    # T-handle lines

    line1, = ax.plot([], [], [], linewidth=5)

    line2, = ax.plot([], [], [], linewidth=5)

    # ========================================================
    # Animation update
    # ========================================================

    def update(frame):

        line1.set_data(
            [xA[frame], xD[frame]],
            [yA[frame], yD[frame]]
        )

        line1.set_3d_properties(
            [zA[frame], zD[frame]]
        )

        line2.set_data(
            [xB[frame], xC[frame]],
            [yB[frame], yC[frame]]
        )

        line2.set_3d_properties(
            [zB[frame], zC[frame]]
        )

        return line1, line2

    ani = FuncAnimation(
        fig,
        update,
        frames=len(psi),
        interval=dt * 1000,
        blit=False
    )

    plt.show()