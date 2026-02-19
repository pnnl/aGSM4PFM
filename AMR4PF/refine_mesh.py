def refine_mesh(T, Ti, P, TR, x, y, c):
    # This function refine the triangles in TR completely
    import numpy as np

    while len(TR) != 0:
        ind1 = TR[-1]
        ind2 = TR[-2] # lines 6 and 7 get the index of last two triangles
        # refine the triangle ind1
        T10 = ind1
        T1 = len(T)
        T2 = T1 + 1 # lines 10 and 11 give index of two new child triangles
        zero_row = np.full_like(T[-1:], -1)
        T = np.vstack([T, zero_row, zero_row]) # lines 12 and 13 build new information for new T1 and T2
        P1 = T[T10, Ti.vertex[0]]  # index of top vertex of T10 triangle
        P2 = T[T10, Ti.vertex[1]]  # index of one bottom vertex
        P3 = T[T10, Ti.vertex[2]]  # index of the other bottom vertex
        P_mid = P[-1] + 1 # get index of the new mid-point on long edge
        P = np.append(P, P_mid)  # add information for the new mid-point
        x = np.append(x, x[P2] / 2 + x[P3] / 2)  # add x of new point
        y = np.append(y, y[P2] / 2 + y[P3] / 2)  # add y of new point
        c = np.append(c, c[P2] / 2 + c[P3] / 2)  # add c of new point
        T[-2:, 0] = T[T10, 0]  # inherit the 'refine' check information of mother triangle
        T[T1, Ti.vertex] = np.hstack([P_mid, P1, P2])  # give vertex of T1 in anticlockwise direction
        T[T2, Ti.vertex] = np.hstack([P_mid, P3, P1])  # give vertex of T2 in anticlockwise direction
        T[T1, Ti.mother] = T10  # set its mother triangle
        T[T2, Ti.mother] = T10  # set its mother triangle
        T[T10, Ti.child] = np.hstack([0, T1, T2])  # now, T0 has child: T1 and T2

        if T[T10, Ti.mother] != -1:  # not the 'pioneer' triangle
            T00 = T[T10, Ti.mother]  # index of grandmother
            T[T00, Ti.grandchild] = 0  # Now, T00 has grandchild

        T[T1, Ti.sister] = T2  # set its sister triangle of T1
        T[T2, Ti.sister] = T1

        T20 = ind2
        T3 = len(T)
        T4 = T3 + 1  # lines 39 and 40 give index of two new child triangles
        zero_row = np.full_like(T[-1:], -1)
        T = np.vstack([T, zero_row, zero_row])  # lines 38 and 39 build new information for new T1 and T2
        P4 = T[T20, Ti.vertex[0]]  # index of top vertex of T10 triangle
        P5 = T[T20, Ti.vertex[1]]  # index of one bottom vertex
        P6 = T[T20, Ti.vertex[2]]  # index of the other bottom vertex
        T[-2:, 0] = T[T20, 0]  # inherit the 'refine' check information of mother triangle
        T[T3, Ti.vertex] = np.hstack([P_mid, P4, P5])  # give vertex of T1 in anticlockwise direction
        T[T4, Ti.vertex] = np.hstack([P_mid, P6, P4])  # give vertex of T2 in anticlockwise direction
        T[T3, Ti.mother] = T20  # set its mother triangle
        T[T4, Ti.mother] = T20  # set its mother triangle
        T[T20, Ti.child] = np.hstack([0, T3, T4])  # now, T0 has child: T3 and T4

        if T[T20, Ti.mother] != -1:  # not the 'pioneer' triangle
            T00 = T[T20, Ti.mother]  # index of grandmother
            T[T00, Ti.grandchild] = 0  # Now, T00 has grandchild

        T[T3, Ti.sister] = T4  # set its sister triangle of T1
        T[T4, Ti.sister] = T3
        T[T1:T4+1, Ti.level] = T[T20, Ti.level] + 1

        # determine neighbors
        if P2 == P6:
            T[T1, Ti.neighbor] = [T2, T[T10, Ti.neighbor[0]], T4]
            T[T2, Ti.neighbor] = [T3, T[T10, Ti.neighbor[2]], T1]
            T[T3, Ti.neighbor] = [T4, T[T20, Ti.neighbor[0]], T2]
            T[T4, Ti.neighbor] = [T1, T[T20, Ti.neighbor[2]], T3]

        # update neighbor's neighbor
        if T[T10, Ti.neighbor[0]] != -1:
            n_ind = np.where(T[T[T10, Ti.neighbor[0]], Ti.neighbor] == T10)[0]
            T[T[T10, Ti.neighbor[0]], Ti.neighbor[n_ind]] = T1

        if T[T10, Ti.neighbor[2]] != -1:
            n_ind = np.where(T[T[T10, Ti.neighbor[2]], Ti.neighbor] == T10)[0]
            T[T[T10, Ti.neighbor[2]], Ti.neighbor[n_ind]] = T2

        if T[T20, Ti.neighbor[0]] != -1:
            n_ind = np.where(T[T[T20, Ti.neighbor[0]], Ti.neighbor] == T20)[0]
            T[T[T20, Ti.neighbor[0]], Ti.neighbor[n_ind]] = T3

        if T[T20, Ti.neighbor[2]] != -1:
            n_ind = np.where(T[T[T20, Ti.neighbor[2]], Ti.neighbor] == T20)[0]
            T[T[T20, Ti.neighbor[2]], Ti.neighbor[n_ind]] = T4

        if len(TR) > 2: # the one of T3/T4 need refine
            TR = np.delete(TR, -1) # remove T10 from TR
            if len(T[np.where(T[TR[-2], Ti.neighbor] == T3)]) > 0:
                TR[-1] = T3
            else:
                TR[-1] = T4
        else: # T10 and T20 are the last two triangles
            TR = np.array([])

    return T, P, x, y, c