import numpy as np
import math
import scipy.io
from scipy.io import loadmat
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from T_construction import T_construction
from refine import refine
from coarsen_mesh import coarsen_mesh
from plot_out import plot_out
from scipy.spatial import Delaunay


N = 11

# generate coordinates x,y and order parameter c
x = np.zeros((N,N))
y = np.zeros((N,N))
c = np.zeros((N,N))
cri = 0.9
n_level = 4
eta = 0.0004
plot_flag = 1
save_flag = 1

for i in range(0, N):
    for j in range(0, N):
        x[i, j] = (j) / (N - 1)
        y[i, j] = (i) / (N - 1)
        r = 0.3 - math.sqrt((x[i, j]) ** 2 + (y[i, j] - 0.5) ** 2)
        c[i, j] = np.tanh(r / math.sqrt(2 * eta))

x_1 = np.arange(0, 1.01, 0.01)
y_1 = np.arange(0, 1.01, 0.01)
X, Y = np.meshgrid(x_1, y_1)
points = np.column_stack((x.ravel(), y.ravel()))
C = griddata(points, c.ravel(), (X, Y), method='linear')
plt.figure()
plt.pcolormesh(X, Y, C, shading='auto', cmap='viridis')
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

# 1 generate the most coarsen mesh
x = x.ravel()
y = y.ravel()
c = c.ravel()

coord = np.column_stack((x, y))
DT = Delaunay(coord)
Tri_List = DT.simplices
N_T = Tri_List.shape[0]
np.savetxt("Tri_List_python.csv", Tri_List, delimiter=",", fmt="%.2f")

# ensure the order of the vertices is counterclockwise
for k in range(Tri_List.shape[0]):
    i1, i2, i3 = Tri_List[k]
    # Calculate signed area
    area = 0.5 * (x[i1] * (y[i2] - y[i3]) - y[i1] * (x[i2] - x[i3]) + (y[i3] * x[i2] - x[i3] * y[i2]))
    if area < 0:
        # Swap i2 and i3 to make counterclockwise
        Tri_List[k, [1, 2]] = Tri_List[k, [2, 1]]

for k in range(0, N_T):
    i1 = Tri_List[k,0]
    i2 = Tri_List[k,1]
    i3 = Tri_List[k,2]
    len12 = math.sqrt((x[i1] - x[i2]) ** 2 + (y[i1] - y[i2]) ** 2)
    len23 = math.sqrt((x[i2] - x[i3]) ** 2 + (y[i2] - y[i3]) ** 2)
    len31 = math.sqrt((x[i3] - x[i1]) ** 2 + (y[i3] - y[i1]) ** 2)
    if len12 == max(len12, len23, len31):
        Tri_List[k, :3] = [i3, i1, i2]
    elif len31 == max(len12, len23, len31):
        Tri_List[k,:3] = [i2, i3, i1]

# 3 construct the T matrix
[T, Ti] = T_construction(x,y,Tri_List,N_T) # build information for all triangles
P = np.arange(0, len(x))
Ti.neighbor = np.array(Ti.neighbor)

# 4 Initialize the mesh T: 'preganent' triangles birth child triangles
T, P, x, y, c = refine(T,Ti,P,x,y,c,cri,n_level)
L0 = len(T[:,1])
L = L0 + 1
ini_refine = 0

while L!= L0:
    r = 0.3 - np.sqrt(x**2 + (y-0.5)**2)
    c = np.tanh(r / np.sqrt(2 * eta))
    T, P, x, y, c = refine(T,Ti,P,x,y,c,cri,n_level)
    L0 = L
    L = len(T[:,1])
    ini_refine = ini_refine + 1

print(f'The mesh is refined by {ini_refine} times.')
T, P, x, y, c = coarsen_mesh(T, Ti, P, x, y, c, cri)

# 5 results plot and save
plot_out(x,y,c,T,Ti,P,eta,plot_flag,save_flag,cri,n_level)