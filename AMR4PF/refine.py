def refine(T,Ti,P,x,y,c,cri,n_level):
    import numpy as np
    from sympy import sqrt
    from refine_TR import refine_TR

    #This function works by refining the mesh based on the given criterion
    T[:,0] = -1
    TC = np.where((T[:, 0] == -1) & (T[:, Ti.child[0]] == -1) & (T[:, Ti.level] < n_level))[0] # triangles for checking refinement
    N_TC = len(TC) # size of TC
    mylist = []
    while N_TC > 0:
        while N_TC > 0:

            index_TC = TC[0] # get an index of 'unchecked' TC triangle
            if T[index_TC, Ti.child[0]] == 0:
                TC = np.delete(TC, 0)
            else:
                c12 = abs(c[T[index_TC, Ti.vertex[0]]] - c[T[index_TC, Ti.vertex[1]]])
                c23 = abs(c[T[index_TC, Ti.vertex[0]]] - (c[T[index_TC, Ti.vertex[1]]] + (c[T[index_TC, Ti.vertex[2]]]))/2)*1.41421
                c31 = abs(c[T[index_TC, Ti.vertex[2]]] - c[T[index_TC, Ti.vertex[0]]])
                mean_c = (c[T[index_TC, Ti.vertex[0]]] + c[T[index_TC, Ti.vertex[1]]] + c[T[index_TC, Ti.vertex[2]]]) / 3

                if np.abs(mean_c)>cri: # no action needed
                    T[index_TC, 0] = 0 # indicate the current triangle as 'checked'
                    break
                else:
                    # first, cut the current triangle
                    [T, P, x, y, c] = refine_TR(T, Ti, P, x, y, c, index_TC)

                    if T[index_TC, Ti.level] < n_level - 1: # the 12 should be cut
                        # refine the child T1
                        [T, P, x, y, c] = refine_TR(T, Ti, P, x, y, c, T[index_TC, Ti.child[1]])
                        [T, P, x, y, c] = refine_TR(T, Ti, P, x, y, c, T[index_TC, Ti.child[2]])

                TC = np.delete(TC, 0) # remove the 'checked' index from TC
                N_TC = len(TC)

            N_TC = len(TC)

        TC = np.where((T[:, 0] == -1) & (T[:, Ti.child[0]] == -1) & (T[:, Ti.level] < n_level))[0] # updates triangles for checking refinement
        N_TC = len(TC) # size of TC

    return T, P, x, y, c
