function [TR] = searching_relatives(index_TC,T,Ti)
% This function searches the 'relatives' triangles which should be refined
% in order to prevent the showup of hanging node

TR = index_TC; % build the array of 'relatives (need refine)' triangles
index_current = index_TC; % get the index of current triangle
if T(index_current,Ti.neighbor(2)) ~= 0 % boundary is not long edge
    index_n = T(index_current,Ti.neighbor(2)); % get index of neighbor triangle sharing the long edge of index_current
    index_n_n = T(index_n,Ti.neighbor(2)); % get principal neighbor's principal neighbor
    while index_n_n ~= index_current && index_n_n ~= 0 % not shariing the same long edge and not boundary triangle
        TR = [TR; index_n];
        index_current = index_n; % set neighbor triangle as current to search its relative triangles
        index_n = index_n_n; % now, this is the neighbor
        index_n_n = T(index_n,Ti.neighbor(2)); % get neighbor's neighbor
    end
    TR = [TR; index_n]; % add the 'relatives' triangles
end
end
