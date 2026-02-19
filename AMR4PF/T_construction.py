# This function constructs the T matrix including the necessary information for each triangles.
# Inputs:
#     x --- x-coordinates of nodes
#     y --- y-coordinates of nodes
#     Tri_list --- node # of triangles
#     N_T --- amount of triangles
#
# Outputs:
#     T: T matrix containing necessary information of each triangle
#     Ti: Column information of T matrix
#%%%%%%%%%%%%%%
# Author: Zirui Mao
# Date revised: 09-03-2021
from trimesh.graph import neighbors


def T_construction(x,y,Tri_List,N_T):
    import numpy as np

    #flag_refine = np.zeros((N_T,1)) # 0th column: index of triangle
    flag_refine = np.full((N_T, 1), -1)
    vertex = Tri_List # 1-3rd column: index of top, bottom1, bottom2, vertices
    #mother = np.zeros((N_T,1)) # 4th column: 'mother' triangle
    mother = np.full((N_T,1),-1)
    #sister = np.zeros((N_T,1)) # 5th column: 'sister' triangle
    sister = np.full((N_T, 1), -1)
    child = np.full((N_T, 3), -1)
    grandchild = np.full((N_T, 1), -1)
    neighbor = np.full((N_T, 3), -1)
    level = np.full((N_T, 1), -1)
    boundary = np.full((N_T, 1), -1)
    # child = np.zeros((N_T,3))  # 6-8th column: has child or not, child 1, child 2

    # neighbor and boundary searching
    # 1 define the mid - points of edges
    xm12 = x[Tri_List[:, 0]] / 2 + x[Tri_List[:, 1]] / 2
    ym12 = y[Tri_List[:, 0]] / 2 + y[Tri_List[:, 1]] / 2
    xm23 = x[Tri_List[:, 1]] / 2 + x[Tri_List[:, 2]] / 2
    ym23 = y[Tri_List[:, 1]] / 2 + y[Tri_List[:, 2]] / 2
    xm31 = x[Tri_List[:, 2]] / 2 + x[Tri_List[:, 0]] / 2
    ym31 = y[Tri_List[:, 2]] / 2 + y[Tri_List[:, 0]] / 2

    for i in range(0, N_T):
    # 2 calculate the distance of mid-points
        dis12 = ((xm12[i] - xm12) ** 2 + (ym12[i] - ym12) ** 2) * \
                ((xm12[i] - xm23) ** 2 + (ym12[i] - ym23) ** 2) * \
                ((xm12[i] - xm31) ** 2 + (ym12[i] - ym31) ** 2)
        dis23 = ((xm23[i] - xm12) ** 2 + (ym23[i] - ym12) ** 2) * \
                ((xm23[i] - xm23) ** 2 + (ym23[i] - ym23) ** 2) * \
                ((xm23[i] - xm31) ** 2 + (ym23[i] - ym31) ** 2)
        dis31 = ((xm31[i] - xm12) ** 2 + (ym31[i] - ym12) ** 2) * \
                ((xm31[i] - xm23) ** 2 + (ym31[i] - ym23) ** 2) * \
                ((xm31[i] - xm31) ** 2 + (ym31[i] - ym31) ** 2)

        # 3 find the index of triangle sharing the same edge 12
        index = np.where(dis12 == 0)[0]
        isTriangleZero = False
        for j in range(len(index)):
            if index[j] == 0:
                isTriangleZero = True
        index = np.sum(index) - i

        # 4 give the index as its neighbor
        if index == 0 and isTriangleZero == False: # no boundary for this edge
            boundary[i] = 0
            neighbor[i, 0] = -1
        else:
            neighbor[i, 0] = index

        # same as step 3, but this is for edge 23
        index = np.where(dis23 == 0)[0]
        isTriangleZero = False
        for j in range(len(index)):
            if index[j] == 0:
                isTriangleZero = True
        index = np.sum(index) - i

        # same as step 4, but this is for edge 23
        if index == 0 and isTriangleZero == False: # no boundary for this edge
            boundary[i] = 0
            neighbor[i, 1] = -1
        else:
            neighbor[i, 1] = index

        # same as step 3, but this is for edge 31
        index = np.where(dis31 == 0)[0]
        isTriangleZero = False
        for j in range(len(index)):
            if index[j] == 0:
                isTriangleZero = True
        index = np.sum(index) - i

        # same as step 4, but this is for edge 31
        if index == 0 and isTriangleZero == False: # no boundary for this edge
            boundary[i] = -1
            neighbor[i, 2] = -1
        else:
            neighbor[i, 2] = index

    # 5 construct the T matrix and get the column information (Ti) of T matrix

    # Define Ti as a class to hold column indices
    class Ti:
        vertex = [1, 2, 3]
        mother = 4
        sister = 5
        child = [6, 7, 8]
        grandchild = 9
        neighbor = [10, 11, 12]
        level = 13
        boundary = 14

    # Stack all columns horizontally to form T
    T = np.hstack([
        flag_refine.astype(int),           # (N_T, 1)
        vertex.astype(int),                # (N_T, 3)
        mother.astype(int),                # (N_T, 1)
        sister.astype(int),                # (N_T, 1)
        child.astype(int),                 # (N_T, 3)
        grandchild.astype(int),            # (N_T, 1)
        neighbor.astype(int),              # (N_T, 3)
        level.astype(int),                 # (N_T, 1)
        boundary.astype(int)               # (N_T, 1)
    ])

    return T, Ti