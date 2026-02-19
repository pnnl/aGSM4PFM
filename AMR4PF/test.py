import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import alphashape

np.random.seed(0)
points = np.random.rand(30, 2)

hull = ConvexHull(points)
alpha = 0.3
alpha_shape = alphashape.alphashape(points, alpha)

plt.figure(figsize=(8, 6))
plt.plot(points[:,0], points[:,1], 'o', label='Points')

# Plot convex hull as a closed red polygon
hull_points = np.append(hull.vertices, hull.vertices[0])
plt.plot(points[hull_points, 0], points[hull_points, 1], 'r-', label='Convex Hull')

# Plot alpha shape
if alpha_shape.geom_type == 'Polygon':
    x, y = alpha_shape.exterior.xy
    plt.plot(x, y, 'g-', label='Alpha Shape (Non-convex Boundary)')

plt.legend()
plt.title('Convex vs Non-Convex Boundaries')
plt.show()
