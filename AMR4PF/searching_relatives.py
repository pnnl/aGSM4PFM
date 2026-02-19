def searching_relatives(index_TC, T, Ti):
    import numpy as np
    # This function searches the 'relatives' triangles which should be refined
    # in order to prevent the showup of hanging node

    TR = [index_TC] # build the array of 'relatives (need refine)' triangles
    index_current = index_TC
    if T[index_current, Ti.neighbor[1]] != -1: # boundary is not long edge
        index_n = T[index_current, Ti.neighbor[1]] # get index of neighbor triangle sharing the long edge of index_current
        index_n_n = T[index_n, Ti.neighbor[1]] # get principal neighbor's principal neighbor
        while index_n_n != index_current and index_n_n != -1: # not sharing the same long edge and not boundary triangle
            TR.append(index_n)
            index_current = index_n # set neighbor triangle as current to search its relative triangles
            index_n = index_n_n # now, this is the neighbor
            index_n_n = T[index_n, Ti.neighbor[1]] # get neighbor's neighbor

        TR.append(index_n) # add the 'relatives' triangles

    return np.array(TR)
