function [T,P,x,y,c] = refine_TR(T,Ti,P,x,y,c,index_TC)
% This function first searches the relatives triangles connecting to the given
% 'refine' triangle to avoid hanging nodes, then refine all the 'relatives'
% triangles

% 1 searches 'relatives' triangles
[TR] = searching_relatives(index_TC,T,Ti); % searhing 'relatives' triangles TR backwards from the last to the first element of TR
ind_n = TR(end); % its neighbor sharing the long edge
if T(ind_n,Ti.neighbor(2)) == 0 % starting from boundary triangle
    [T,P,TR,x,y,c] = refine_TR_boundary (T,Ti,P,TR,x,y,c);
end
if ~isempty(TR)
    [T,P,x,y,c] = refine_TR_inner (T,Ti,P,TR,x,y,c);
end

end