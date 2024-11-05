import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translate(vertices, tx, ty, tz):
    T = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, T.T)

def scale(vertices, sx, sy, sz):
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, S.T)

def rotate_x(vertices, angle):
    rad = np.deg2rad(angle)
    R_x = np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_x.T)

def rotate_y(vertices, angle):
    rad = np.deg2rad(angle)
    R_y = np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_y.T)

def rotate_z(vertices, angle):
    rad = np.deg2rad(angle)
    R_z = np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_z.T)

def zoom(vertices, sz):
    Z = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, Z.T)

def plot_3d_shape(vertices, ax, title):
    ax.clear()
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    
    for i, v1 in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            v2 = vertices[j]
            ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], 'k-')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

vertices = np.array([
    [1, 1, 1, 1],
    [-1, 1, 1, 1],
    [-1, -1, 1, 1],
    [1, -1, 1, 1],
    [1, 1, -1, 1],
    [-1, 1, -1, 1],
    [-1, -1, -1, 1],
    [1, -1, -1, 1]
])

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(321, projection='3d')
plot_3d_shape(vertices[:, :3], ax1, 'Original Shape')
vertices_translated = translate(vertices, 2, 3, 4)
ax2 = fig.add_subplot(322, projection='3d')
plot_3d_shape(vertices_translated[:, :3], ax2, 'Translated Shape')
vertices_scaled = scale(vertices_translated, 2, 2, 2)
ax3 = fig.add_subplot(323, projection='3d')
plot_3d_shape(vertices_scaled[:, :3], ax3, 'Scaled Shape')
vertices_rotated_x = rotate_x(vertices_scaled, 45)
ax4 = fig.add_subplot(324, projection='3d')
plot_3d_shape(vertices_rotated_x[:, :3], ax4, 'Rotated X Shape')
vertices_rotated_y = rotate_y(vertices_rotated_x, 30)
ax5 = fig.add_subplot(325, projection='3d')
plot_3d_shape(vertices_rotated_y[:, :3], ax5, 'Rotated Y Shape')
vertices_rotated_z = rotate_z(vertices_rotated_y, 60)
ax6 = fig.add_subplot(326, projection='3d')
plot_3d_shape(vertices_rotated_z[:, :3], ax6, 'Rotated Z Shape')
plt.tight_layout()
plt.show()
