import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_rgb_colors(ax):
 colors = [
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 1],
 [1, 1, 0],
 [1, 0, 1],
 [0, 1, 1],
 [0.5, 0.5, 0.5]
 ]
 ax.set_title('RGB Color Model')
 for i, color in enumerate(colors):
    ax.fill_between([i, i+1], 0, 1, color=color)
 ax.set_xlim(0, len(colors))
 ax.set_ylim(0, 1)
 ax.invert_yaxis()
 ax.set_xticks([])
 ax.set_yticks([])

def plot_hsv_to_rgb_colors(ax):
 hsv_colors = [
 [0, 1, 1],
 [120/360, 1, 1],
 [240/360, 1, 1],
 [60/360, 1, 1],
 [300/360, 1, 1],
 [180/360, 1, 1],
 [0, 0, 0.5]
 ]
 rgb_colors = [hsv_to_rgb(color) for color in hsv_colors]
 ax.set_title('HSV to RGB Color Model')
 for i, color in enumerate(rgb_colors):
    ax.fill_between([i, i+1], 0, 1, color=color)
 ax.set_xlim(0, len(rgb_colors))
 ax.set_ylim(0, 1)
 ax.invert_yaxis()
 ax.set_xticks([])
 ax.set_yticks([])

vertices_cube = np.array([
 [1, 1, 1],
 [-1, 1, 1],
 [-1, -1, 1],
 [1, -1, 1],
 [1, 1, -1],
 [-1, 1, -1],
 [-1, -1, -1],
 [1, -1, -1]
])
faces_cube = [
 [vertices_cube[0], vertices_cube[1], vertices_cube[2], vertices_cube[3]],
 [vertices_cube[4], vertices_cube[5], vertices_cube[6], vertices_cube[7]],
 [vertices_cube[0], vertices_cube[1], vertices_cube[5], vertices_cube[4]],
 [vertices_cube[2], vertices_cube[3], vertices_cube[7], vertices_cube[6]],
 [vertices_cube[0], vertices_cube[3], vertices_cube[7], vertices_cube[4]],
 [vertices_cube[1], vertices_cube[2], vertices_cube[6], vertices_cube[5]]
]
face_colors_cube = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']

vertices_pyramid = np.array([
 [0, 0, 1],
 [-1, -1, 0],
 [1, -1, 0],
 [1, 1, 0],
 [-1, 1, 0]
])
faces_pyramid = [
 [vertices_pyramid[0], vertices_pyramid[1], vertices_pyramid[2]],
 [vertices_pyramid[0], vertices_pyramid[2], vertices_pyramid[3]],
 [vertices_pyramid[0], vertices_pyramid[3], vertices_pyramid[4]],
 [vertices_pyramid[0], vertices_pyramid[4], vertices_pyramid[1]],
 [vertices_pyramid[1], vertices_pyramid[2], vertices_pyramid[3], vertices_pyramid[4]]
]
vertex_colors_pyramid = np.array([
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 1],
 [1, 1, 0],
 [0, 1, 1]
])

fig = plt.figure(figsize=(18, 15))
ax1 = fig.add_subplot(321)
plot_rgb_colors(ax1)
ax2 = fig.add_subplot(322)
plot_hsv_to_rgb_colors(ax2)
ax3 = fig.add_subplot(323, projection='3d')
poly3d_cube = Poly3DCollection(faces_cube, facecolors=face_colors_cube, linewidths=1, 
edgecolors='k', alpha=0.8)
ax3.add_collection3d(poly3d_cube)
ax3.set_title('Flat Shading - Cube')
ax3.set_xlim([-2, 2])
ax3.set_ylim([-2, 2])
ax3.set_zlim([-2, 2])
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax4 = fig.add_subplot(324, projection='3d')
mean_color_pyramid = vertex_colors_pyramid.mean(axis=0)
poly3d_pyramid = Poly3DCollection(faces_pyramid, facecolors=mean_color_pyramid, 
linewidths=1, edgecolors='k', alpha=0.8)
ax4.add_collection3d(poly3d_pyramid)
ax4.set_title('Gouraud Shading - Pyramid')
ax4.set_xlim([-2, 2])
ax4.set_ylim([-2, 2])
ax4.set_zlim([-2, 2])
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
plt.tight_layout()
plt.show()
