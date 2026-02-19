def refine_boundary(T, Ti, P, TR, x, y, c):
    import numpy as np
    # This function refines the boundary triangle to be two child triangles and builds the necessary information
    T0 = TR[-1] # get index of original boundary triangle (now, be mother)
    T1 = len(T)
    T2 = T1 + 1 # lines 4 and 5 give index of two new child triangles
    zero_row = np.full_like(T[-1:], -1)
    T = np.vstack([T, zero_row, zero_row]) # lines 7 and 8 build information for new T1 and T2
    P1 = T[T0,Ti.vertex[0]] # index of top vertex of T0 triangle
    P2 = T[T0,Ti.vertex[1]] # index of one bottom vertex
    P3 = T[T0,Ti.vertex[2]] # index of the other bottom vertex
    P_mid = P[-1] + 1 # get index of the new mid-point on long edge
    x = np.append(x, x[P2]/2+x[P3]/2) # add x of new point
    y = np.append(y, y[P2]/2+y[P3]/2) # add y of new point
    c = np.append(c, c[P2]/2+c[P3]/2) # add c of new point
    P = np.hstack([P, P_mid]) # add information for the new mid-point
    T[-2:, 0] = T[T0, 0] # inherit the 'refine' check information of mother triangle
    T[T1, Ti.vertex] = np.hstack([P_mid, P1, P2]) # give vertex of T1 in anticlockwise direction
    T[T2, Ti.vertex] = np.hstack([P_mid, P3, P1]) # give vertex of T2 in anticlockwise direction
    T[T1, Ti.mother] = T0 # set its mother triangle
    T[T2, Ti.mother] = T0 # set its mother triangle
    T[T0, Ti.child] = np.hstack([0, T1, T2]) # now, T0 has child: T1 and T2

    if T[T0, Ti.mother] != -1: # not the 'pioneer' triangle
        T00 = T[T0, Ti.mother] # index of grandmother
        T[T00, Ti.grandchild] = 0 # Now, T00 has grandchild

    T[T1, Ti.sister] = T2 # set sister triangle
    T[T2, Ti.sister] = T1
    T[T1:T2 + 1, Ti.level] = T[T0, Ti.level] + 1

    # set neighbor of child T1 and T2
    T[T1, Ti.neighbor] = np.hstack([T2, T[T0, Ti.neighbor[0]], -1])
    T[T2, Ti.neighbor] = np.hstack([-1, T[T0, Ti.neighbor[2]], T1])

    # update neighbor of T1/T2's neighbor
    if T[T0, Ti.neighbor[0]] != -1:
        n_ind = np.where(T[T[T0, Ti.neighbor[0]], Ti.neighbor] == T0)[0]
        T[T[T0, Ti.neighbor[0]], Ti.neighbor[n_ind]] = T1

    if T[T0, Ti.neighbor[2]] != -1:
        n_ind = np.where(T[T[T0, Ti.neighbor[2]], Ti.neighbor] == T0)[0]
        T[T[T0, Ti.neighbor[2]], Ti.neighbor[n_ind]] = T2

    T[T1, -1] = 0
    T[T2, -1] = 0 # lines 45 and 46 boundary? yes

    # update the tail of 'relative' triangles to be the eaxt child
    if len(TR) == 1: # only one boundary triangle in TR
        TR = np.array([])
    elif len(T[np.where(T[T1, Ti.neighbor] == TR[-2])]) == 0: # T1 is not neighbor
            TR[-1] = T2
    else:
            TR[-1] = T1

    return [T, P, TR, x, y, c]