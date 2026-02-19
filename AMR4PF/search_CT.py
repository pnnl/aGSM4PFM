def search_CT(T, Ti):
    import numpy as np
    # This function searches the triangles for coarsening examination
    # search inner triangles

    # get the index of triangles who have principal neighbors

    index_NT = np.where((T[:, Ti.neighbor[1]] != -1) & (T[:, 0] == -1))[0] # get the index of triangles who have principal neighbors
    index_PN = T[index_NT, Ti.neighbor[1]] # get the index of principal neighbors

    TC = np.where(((T[index_NT, Ti.child[0]]) + (T[index_NT, Ti.grandchild]) == -1) &
                   ((T[index_PN, Ti.child[0]]) + (T[index_PN, Ti.grandchild]) == -1))[0]
    TC = index_NT[TC] # index array of triangles subjected to coarsening examination

    BT = np.where((T[:, 0] == -1) & (T[:, Ti.neighbor[1]] == -1) & ((T[:, Ti.child[0]] + T[:, Ti.grandchild]) == -1))[0]
    TC = np.concatenate((TC, BT), axis=0)

    return TC