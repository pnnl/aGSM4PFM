def coarsen_mesh(T, Ti, P, x, y, c, cri):
    from search_CT import search_CT
    import numpy as np
    # This function coarsen the mesh
    # It searches the triangles subjected to coarsening examination
    # the triangles who and whose principal neighbor have child but no grandchild
    T[:, 0] = -1
    TC = search_CT(T, Ti)
    counter = 0

    while len(TC) > 0:
        while len(TC) > 0:

            T1 = TC[0]
            if T[T1, Ti.neighbor[1]] == -1: # then this triangle is boundary
                mean_c = (c[T[T1, Ti.vertex[0]]] + c[T[T1, Ti.vertex[1]]] + c[T[T1, Ti.vertex[2]]]) / 3

                if np.abs(mean_c)>cri and T[T1, Ti.level] > 0: # need coarsened
                    # neighbor-related changes

                    if T[T1, Ti.neighbor[0]] != -1:
                        ind_n = T[T[T1, Ti.child[1]], Ti.neighbor[1]] # index of T1's 1st child's principal neighbor
                        T[T1, Ti.neighbor[0]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T1, Ti.child[1]])[0] # find which neighbor of ind_n is T1's 1st child
                        T[ind_n, Ti.neighbor[n_ind]] = T1

                    if T[T1, Ti.neighbor[2]] != -1:
                        ind_n = T[T[T1, Ti.child[2]], Ti.neighbor[1]]  # index of T1's 2nd child's principal neighbor
                        T[T1, Ti.neighbor[2]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T1, Ti.child[2]])[0] # find which neighbor of ind_n is T1's 2nd child
                        T[ind_n, Ti.neighbor[n_ind]] = T1

                    P[T[T[T1, Ti.child[1]], Ti.vertex[0]]] = -1 # remove information of the mid-point of long edge
                    T[T[T1, Ti.child[1:3]], :] = -1 # remove the information of child information

                    # child-related changes
                    T[T1, Ti.child] = -1 # has no child now
                    if T[T1, Ti.mother] != -1: # not pioneer, has mother
                        if T[T[T[T1, Ti.mother], Ti.child[1]], Ti.child[0]] == -1 and T[T[T[T1, Ti.mother], Ti.child[2]], Ti.child[0]] == -1:
                            T[T[T1, Ti.mother], Ti.grandchild] = -1 # mother has no grandchild now

                TC = np.delete(TC, 0) # remove the triangle from TC
                T[T1, 0] = 0 # indicate the triangle has been checked
            else: # then, the boundary is not a boundary
                T2 = T[T1, Ti.neighbor[1]]
                mean_c = (c[T[T1, Ti.vertex[0]]] + c[T[T1, Ti.vertex[1]]] + c[T[T1, Ti.vertex[2]]]+c[T[T2, Ti.vertex[0]]] + c[T[T2, Ti.vertex[1]]] + c[T[T2, Ti.vertex[2]]]) / 6

                index_p = [T1, T2]

                if np.abs(mean_c) > cri: # need coarsened

                    # neighbor-related changes
                    if T[T1, Ti.neighbor[0]] != -1:
                        ind_n = T[T[T1, Ti.child[1]], Ti.neighbor[1]]  # index of T1's 1st child's principal neighbor
                        T[T1, Ti.neighbor[0]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T1, Ti.child[1]])[0]  # find which neighbor of ind_n is T1's 1st child
                        T[ind_n, Ti.neighbor[n_ind]] = T1

                    if T[T1, Ti.neighbor[2]] != -1:
                        ind_n = T[T[T1, Ti.child[2]], Ti.neighbor[1]]  # index of T1's 2nd child's principal neighbor
                        T[T1, Ti.neighbor[2]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T1, Ti.child[2]])[0]  # find which neighbor of ind_n is T1's 2nd child
                        T[ind_n, Ti.neighbor[n_ind]] = T1

                    if T[T2, Ti.neighbor[0]] != -1:
                        ind_n = T[T[T2, Ti.child[1]], Ti.neighbor[1]] # index of T2's 1st child's principal neighbor
                        T[T2, Ti.neighbor[0]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T2, Ti.child[1]])[0] # find which neighbor of ind_n is T2's 1st child
                        T[ind_n, Ti.neighbor[n_ind]] = T2

                    if T[T2, Ti.neighbor[2]] != -1:
                        ind_n = T[T[T2, Ti.child[2]], Ti.neighbor[1]]  # index of T2's 2nd child's principal neighbor
                        T[T2, Ti.neighbor[2]] = ind_n
                        n_ind = np.where((T[ind_n, Ti.neighbor]) == T[T2, Ti.child[2]])[0] # find which neighbor of ind_n is T2's 2nd child
                        T[ind_n, Ti.neighbor[n_ind]] = T2

                    P[T[T[T1, Ti.child[1]], Ti.vertex[0]]] = -1  # remove information of the mid-point of long edge
                    T[T[T1, Ti.child[1:3]], :] = -1  # remove the information of child information
                    T[T[T2, Ti.child[1:3]], :] = -1  # remove the information of child information

                    # child-related changes
                    i = 0
                    while i != len(index_p):
                        T[index_p[i], Ti.child] = -1 # has no child now
                        i+=1
                    # T[index_p, Ti.child] = -1  has no child now
                    if T[T1, Ti.mother] != -1:  # not pioneer, has mother
                        if T[T[T[T1, Ti.mother], Ti.child[1]], Ti.child[0]] == -1 and T[T[T[T1, Ti.mother], Ti.child[2]], Ti.child[0]] == -1:
                            T[T[T1, Ti.mother], Ti.grandchild] = -1  # mother has no grandchild now

                        if T[T[T[T2, Ti.mother], Ti.child[1]], Ti.child[0]] == -1 and T[T[T[T2, Ti.mother], Ti.child[2]], Ti.child[0]] == -1:
                            T[T[T2, Ti.mother], Ti.grandchild] = -1  # mother has no grandchild now

                delete_these_indices = np.concatenate(([0], np.where(TC==T2)[0]))
                TC = np.delete(TC, delete_these_indices) # remove the triangle from TC
                T[[T1, T2], 0] = 0 # indicate the triangle has been checked

            counter += 1

            break
        TC = search_CT(T, Ti)

    # update T, P, x, y, c
    index_DP = np.where(P==-1)[0] # get the index of the P that need to be deleted
    index_RT = np.where(T[:, Ti.vertex[0]] != -1)[0] # get index of remaining triangles
    index_DT = np.where(T[:, Ti.vertex[0]] == -1)[0] # get index of useless triangles
    crement_P = np.full(len(P), 0)
    for i in range(len(index_DP)):
        crement_P[(index_DP[i] + 1):] = crement_P[(index_DP[i] + 1):] - 1 # crement of P index

    # delete unecessary mid-points
    x = np.delete(x, index_DP)
    y = np.delete(y, index_DP)
    c = np.delete(c, index_DP)

    T[index_RT[:, None], Ti.vertex] += crement_P[T[index_RT[:, None], Ti.vertex]] # update the vertex index
    P = np.arange(0, len(x))

    crement_T = np.full(len(T),0)
    for i in range(len(index_DT)):
        crement_T[(index_DT[i] + 1):] = crement_T[(index_DT[i] + 1):] - 1 # crement of triangle index

    # update triangle index of mother, sister, child, and neighbor
    index_mother = np.where(T[:, Ti.mother] != -1)[0]
    T[index_mother[:, None], Ti.mother] += crement_T[T[index_mother[:, None], Ti.mother]]
    index_sister = np.where(T[:, Ti.sister] != -1)[0]
    T[index_sister[:, None], Ti.sister] += crement_T[T[index_sister[:, None], Ti.sister]]
    index_child = np.where(T[:, Ti.child[0]] != -1)[0]
    T[index_child[:, None], Ti.child[1]] += crement_T[T[index_child[:, None], Ti.child[1]]]
    T[index_child[:, None], Ti.child[2]] += crement_T[T[index_child[:, None], Ti.child[2]]]
    index_neighbor = np.where(T[:, Ti.neighbor[0]] != -1)[0]
    T[index_neighbor[:, None], Ti.neighbor[0]] += crement_T[T[index_neighbor[:, None], Ti.neighbor[0]]]
    index_neighbor = np.where(T[:, Ti.neighbor[1]] != -1)[0]
    T[index_neighbor[:, None], Ti.neighbor[1]] += crement_T[T[index_neighbor[:, None], Ti.neighbor[1]]]
    index_neighbor = np.where(T[:, Ti.neighbor[2]] != -1)[0]
    T[index_neighbor[:, None], Ti.neighbor[2]] += crement_T[T[index_neighbor[:, None], Ti.neighbor[2]]]

    T = np.delete(T, index_DT, axis=0)

    return T, P, x, y, c