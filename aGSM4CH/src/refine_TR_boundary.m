function [T,P,TR,x,y,c] = refine_TR_boundary (T,Ti,P,TR,x,y,c)
% This function refine the boundary triangel to be two child triangles and
% build the necessary information

T0 = TR(end); % get index of original boundary triangle (now, be mother)
T1 = length(T)+1; T2 = T1+1; % give index of two new child triangles
T = [T; 0*T(end,:); 0*T(end,:)]; % build information for new T1 and T2
P1 = T(T0,Ti.vertex(1)); % index of top vertex of T0 triangle
P2 = T(T0,Ti.vertex(2)); % index of one bottom vertex
P3 = T(T0,Ti.vertex(3)); % index of the other bottom vertex
P_mid = P(end)+1; % get index of the new mid-point on long edge
x = [x; x(P2)/2+x(P3)/2]; % add x of new point
y = [y; y(P2)/2+y(P3)/2]; % add y of new point
c = [c; c(P2)/2+c(P3)/2]; % add c of new point
P = [P P_mid]; % add information for the new mid-point
T(end-1:end,1) = T(T0,1); % inherent the 'refine' check information of mother triangle
T(T1,Ti.vertex) = [P_mid P1 P2]; % give vertex of T1 in anticlockwise direction
T(T2,Ti.vertex) = [P_mid P3 P1]; % give vertex of T2 in anticlockwise direction
T(T1,Ti.mother) = T0; % set its mother triangle
T(T2,Ti.mother) = T0; % set its mother triangle
T(T0,Ti.child) = [1 T1 T2]; % now, T0 has child: T1 and T2
if T(T0,Ti.mother) ~= 0 % not the 'pioneer' triangle
    T00 = T(T0,Ti.mother); % index of grandmother
    T(T00,Ti.grandchild) = 1; % Now, T00 has grandchild
end
T(T1,Ti.sister) = T2; % set its sister triangle of T1
T(T2,Ti.sister) = T1;
T(T1:T2,Ti.level) = T(T0,Ti.level) + 1;
% set neighbor of child T1 and T2
T(T1,Ti.neighbor) = [T2 T(T0,Ti.neighbor(1)), 0];
T(T2,Ti.neighbor) = [0 T(T0,Ti.neighbor(3)), T1];
% update neighbor of T1/T2's neighbor
if T(T0,Ti.neighbor(1))~=0
    n_ind = find(T(T(T0,Ti.neighbor(1)),Ti.neighbor)==T0);
    T(T(T0,Ti.neighbor(1)),Ti.neighbor(n_ind)) = T1;
end

if T(T0,Ti.neighbor(3))~=0
    n_ind = find(T(T(T0,Ti.neighbor(3)),Ti.neighbor)==T0);
    T(T(T0,Ti.neighbor(3)),Ti.neighbor(n_ind)) = T2;
end

T(T1,end) = 1; T(T2,end) = 1; % boundary? yes

% update the tail of 'relative' triangles to be the eaxt child
if isscalar(TR) % only one bounday triangle in TR
    TR = [];
else
    if isempty(find(T(T1,Ti.neighbor)==TR(end-1), 1)) % T1 is not neighbor
        TR(end) = T2;
    else
        TR(end) = T1;
    end
end
end