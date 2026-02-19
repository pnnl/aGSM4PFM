def refine_TR(T, Ti, P, x, y, c, index_TC):
    import numpy as np
    from searching_relatives import searching_relatives
    from refine_boundary import refine_boundary
    from refine_mesh import refine_mesh

    # This function first searches the relatives triangles connecting to the given
    # 'refine' triangle to avoid hanging nodes, then refine all the 'relatives'
    # triangles

    # 1 searches 'relatives' triangles

    TR = searching_relatives(index_TC, T, Ti) # searching 'relatives' triangles TR backwards from the last to the first element of TR
    ind_n = TR[-1] # its neighbor sharing the long edge
    if T[ind_n, Ti.neighbor[1]] == -1: # starting from boundary triangle
        [T, P, TR, x, y, c] = refine_boundary(T, Ti, P, TR, x, y, c)

    if len(TR) > 0:
        [T, P, x, y, c] = refine_mesh(T, Ti, P, TR, x, y, c)

    return T, P, x, y, c