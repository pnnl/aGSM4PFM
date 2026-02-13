function [T,Ti] = T_construction(x,y,Tri_List,N_T)
% This function constructs the T matrix including the necessary information
% for each triangles.
% Inputs: 
%     x --- x-coordinates of nodes
%     y --- y-coordinates of nodes
%     Tri_list --- node # of triangles
%     N_T --- amount of triangles
%
% Outputs:
%     T: T matrix containing necessary information of each triangle
%     Ti: Column information of T matrix
%%%%%%%%%%%%%%
% Author: Zirui Mao
% Date revised: 09-03-2021

flag_refine = zeros(N_T,1); % 1-st column: index of triangle
vertex = Tri_List; % 2-4th column: index of top, bottom1, bottom2 vertexs
mother = zeros(N_T,1); % 5th column: 'mother' triangle
sister = zeros(N_T,1); % 6th column: 'sister' triangle
child = zeros(N_T,3); % 7-9 column: has child or not, child 1, child 2
grandchild = zeros(N_T,1); % 10th column: has grandchild or not
neighbor = zeros(N_T,3); % 11-13th column: neighbor triangles
level = zeros(N_T,1); % 14th column: level of triangles
boundary = zeros(N_T,1); % 15th column: whethor boundary.


%% neighbor and boundary searching
% 1 define the mid-points of edges
xm12 = x(Tri_List(:,1))/2+x(Tri_List(:,2))/2;
ym12 = y(Tri_List(:,1))/2+y(Tri_List(:,2))/2;
xm23 = x(Tri_List(:,2))/2+x(Tri_List(:,3))/2;
ym23 = y(Tri_List(:,2))/2+y(Tri_List(:,3))/2;
xm31 = x(Tri_List(:,3))/2+x(Tri_List(:,1))/2;
ym31 = y(Tri_List(:,3))/2+y(Tri_List(:,1))/2;

for i = 1:N_T
    % 2 calcualte the distance of mid-points
    dis12 = ((xm12(i)-xm12).^2+(ym12(i)-ym12).^2).*...
        ((xm12(i)-xm23).^2+(ym12(i)-ym23).^2).*...
        ((xm12(i)-xm31).^2+(ym12(i)-ym31).^2);
    dis23 = ((xm23(i)-xm12).^2+(ym23(i)-ym12).^2).*...
        ((xm23(i)-xm23).^2+(ym23(i)-ym23).^2).*...
        ((xm23(i)-xm31).^2+(ym23(i)-ym31).^2);
    dis31 = ((xm31(i)-xm12).^2+(ym31(i)-ym12).^2).*...
        ((xm31(i)-xm23).^2+(ym31(i)-ym23).^2).*...
        ((xm31(i)-xm31).^2+(ym31(i)-ym31).^2);
    
    % 3 find the index of triangle sharing the same edge 12
    index = find(dis12 == 0);
    index = sum(index)-i;
   
    % 4 give the index as its neighbor
    if index == 0 % no boundary for this edge
        boundary(i) = 1; % the current triangle is a boundary one
        neighbor(i,1) = 0;
    else
        neighbor(i,1) = index;
    end
    
    % same as step 3, but this is for edge 23
    index = find(dis23 == 0);
    index = sum(index)-i;
    % same as step 4, but this is for edge 23
    if index == 0
        boundary(i) = 1;
        neighbor(i,2) = 0;
    else
        neighbor(i,2) = index;
    end
    
    % same as step 3, but this is for edge 31
    index = find(dis31 == 0);
    index = sum(index)-i;
    % same as step 4, but this is for edge 23
    if index == 0
        boundary(i) = 1;
        neighbor(i,3) = 0;
    else
        neighbor(i,3) = index;
    end
    
end

% 5 construct the T matrix and get the column information (Ti) of T matrix
T = [flag_refine vertex mother sister child grandchild neighbor level boundary];
Ti.vertex = 2:4; Ti.mother = 5; Ti.sister = 6; Ti.child=7:9; Ti.grandchild=10; Ti.neighbor = 11:13; Ti.level = 14;

end