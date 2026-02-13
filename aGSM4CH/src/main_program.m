clc
clear all
format long

% configuration controlling parameters
N = 21; % control the resolution of coarest mesh
gamma = 0.0001; % gradient term coefficient that control interface thickness. 
n_level = 6; % control the finest mesh. !!! For better accuracy, control n_level such that the interface occupies at least 4~5 layers of grid.
c_thr = 0.9; % the threshold value defining interface area. -1 <= c <= 1. 
t_total = 0.1; % total physical time in simulation

% calculate the dependent parameters automatically
D = 1.0; % diffusion coefficient
ff = 2^(n_level/2);
% gamma = 0.004/ff^2; % gradient term coefficient. this will be adjusted according to the mesh automaticall such that the interface always occupies 4~5 layers of grid
ds=1.0/(N-1); % this is the resolution of the coarest mesh
dt = (ds/ff)^4/40/gamma; % time step for the explicit scheme
steps = ceil(t_total/dt/50)*50; % controls the total computational steps
dt = t_total/steps;


%% generate coordinates x,y and order parameter c
x = zeros(N,N);
y = zeros(N,N);
c = zeros(N,N);
for i = 1:N
    for j = 1:N
        x(i,j) = (j-1)/(N-1);
        y(i,j) = (i-1)/(N-1);
        c(i,j) = Initial_Geom(x(i,j), y(i,j));
    end
end

%% 1 generate the most coarsen mesh
x=x(:);y=y(:);c=c(:);
coord = [x y];
DT = delaunayTriangulation(coord);
Tri_List = DT.ConnectivityList; % Triangle list: anticlockwise direction
N_T = length(Tri_List(:,1));

%% 2 set the longest edge to be 23
for k=1:N_T
    i1 = Tri_List(k,1);
    i2 = Tri_List(k,2);
    i3 = Tri_List(k,3);
    len12 = sqrt((x(i1)-x(i2))^2+(y(i1)-y(i2))^2);
    len23 = sqrt((x(i2)-x(i3))^2+(y(i2)-y(i3))^2);
    len31 = sqrt((x(i3)-x(i1))^2+(y(i3)-y(i1))^2);
    if len12 == max([len12 len23 len31])
        Tri_List(k,1:3) = [i3 i1 i2];
    elseif len31 == max([len12 len23 len31])
        Tri_List(k,1:3) = [i2 i3 i1];
    end
end

%% 3 construct the T matrix
[T,Ti] = T_construction(x,y,Tri_List,N_T); % build information for all triangles
P = 1:length(x); % build information for nodes/points

%% 4 Initialize the mesh T：'preganent' triangles birth child triangles
[T,P,x,y,c] = refine0(T,Ti,P,x,y,c,c_thr,n_level);
L0 = length(T(:,1)); L = L0+1;
ini_refine = 0;
while L ~= L0
    [T,P,x,y,c] = refine0(T,Ti,P,x,y,c,c_thr,n_level);
    L0 = L; L = length(T(:,1));
    ini_refine = ini_refine + 1;
end
fprintf('The mesh is refined by %d times. \n',ini_refine)
[T,P,x,y,c] = coarsen_mesh (T,Ti,P,x,y,c,c_thr);
[xq,yq] = meshgrid(0:ds/ff:1, 0:ds/ff:1);


%% PFM simulation
figure(1);                        % create/use figure 1
set(gcf, 'Units', 'pixels');      % ensure units are pixels
set(gcf, 'Position', [100 100 800 600]);
set(gcf,'Color','w');
pic_num = 1;
for i = 1:steps
    ind = find(T(:,Ti.child(1))==0); % no child T 
    [ddc] = GSM (x,y,c,ds,T(ind,Ti.vertex),T(ind,Ti.level));
    mu = -(-c.^3+c+gamma*ddc); % calculate the chemical potential term
    [ddmu] = GSM (x,y,mu,ds,T(ind,Ti.vertex),T(ind,Ti.level));
    c=c+dt*ddmu*D; % update the concentration
   
    if mod(i,100)==0
        [T,P,x,y,c] = refine(T,Ti,P,x,y,c,c_thr,n_level);
        T(:,1) = 0;
        [TC] = search_CT(T,Ti); % get the index of triangles under coarsening examination
        [T,P,x,y,c] = coarsen_mesh (T,Ti,P,x,y,c,c_thr);
    end

    if mod(i,steps/50) == 0
        cq = griddata(x,y,c,xq,yq);
        surf(xq,yq,cq-2,'EdgeColor','None','facecolor','interp') % Note that the c is shifted to show the mesh.
        hold on
        view(2)
        xlabel('x');
        ylabel('y');
        triplot(T(:,Ti.vertex),x,y,'w','linewidth',0.5); hold off
        axis equal
        axis([0 1 0 1])
        set(gca, 'Fontname', 'Times New Roman','FontSize',25);
        colormap jet
        drawnow
        fprintf("Progress: %d %%\n", round(i/steps*100));

        F=getframe(gcf);
        I=frame2im(F);
        [I,map]=rgb2ind(I,256);
        if pic_num == 1
            imwrite(I,map,'result.gif','gif', 'Loopcount',inf,'DelayTime',0.1);
        else
            imwrite(I,map,'result.gif','gif','WriteMode','append','DelayTime',0.1);
        end
        pic_num = pic_num + 1;
    end
end
