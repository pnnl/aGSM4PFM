function [TC] = search_CT(T,Ti)
% This function searches the triangles for coarsening examination
% search inner triangles
index_NT = find(T(:,Ti.neighbor(2)) ~= 0 & T(:,1) == 0); % get the index of triangles who has principal neighbors
index_PN = T(index_NT,Ti.neighbor(2)); % get the index of the principal neighbors
TC = T(index_NT,Ti.child(1))+T(index_NT,Ti.grandchild) == 1 & ...
    T(index_PN,Ti.child(1))+T(index_PN,Ti.grandchild) == 1;
TC = index_NT(TC); % index array of triangles subjected to coarsening examination

%search boundary triangles
BT = find(T(:,1)==0 & T(:,Ti.neighbor(2))==0 & T(:,Ti.child(1))+T(:,Ti.grandchild(1))==1);
TC = [TC; BT];
end