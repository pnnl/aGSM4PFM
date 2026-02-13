function [T,P,x,y,c] = coarsen_mesh (T,Ti,P,x,y,c,cri)

% This function coarsen the mesh 
% It searches the triangles subjected to coarsening examination
% the triangles who and whose principal neighbor have child but no grandchild
T(:,1) = 0;
[TC] = search_CT(T,Ti); % get the index of triangles under coarsening examination
while ~isempty(TC)
    while ~isempty(TC)
        
        T1 = TC(1);
        if T(T1,Ti.neighbor(2)) == 0 % then this triangle is boundary
            mean_c = (c(T(T1,Ti.vertex(1)))+c(T(T1,Ti.vertex(2)))+c(T(T1,Ti.vertex(3))))/3.0;
            if (mean_c>cri || mean_c<-cri) && T(T1, Ti.level) > 0  
            % c12 = abs(c(T(T1,Ti.vertex(1)))-c(T(T1,Ti.vertex(2))));
            % c23 = abs(c(T(T1,Ti.vertex(1)))-(c(T(T1,Ti.vertex(2)))+c(T(T1,Ti.vertex(3))))/2)*sqrt(2);
            % c31 = abs(c(T(T1,Ti.vertex(3)))-c(T(T1,Ti.vertex(1))));
            % 
            % if c12<cri && c23<cri && c31<cri 
                               
                % neighbor-related changes
                if T(T1,Ti.neighbor(1))~=0
                    ind_n = T(T(T1,Ti.child(2)),Ti.neighbor(2)); % index of T1's 1st child's principal neighbor
                    T(T1,Ti.neighbor(1)) = ind_n;
                    n_ind = logical(T(ind_n, Ti.neighbor) == T(T1, Ti.child(2))); % find which neighbor of ind_n is T1's 1st child
                    T(ind_n,Ti.neighbor(n_ind)) = T1;
                end
                
                if T(T1,Ti.neighbor(3))~=0
                    ind_n = T(T(T1,Ti.child(3)),Ti.neighbor(2)); % index of T1's 2nd child's principal neighbor
                    T(T1,Ti.neighbor(3)) = ind_n;
                    n_ind = find(T(ind_n,Ti.neighbor)==T(T1,Ti.child(3))); % find which neighbor of ind_n is T1's 2nd child
                    T(ind_n,Ti.neighbor(n_ind)) = T1;
                end
                
                
                P(T(T(T1,Ti.child(2)),Ti.vertex(1))) = 0; % remove the information of the mid-point of long edge
                T(T(T1,Ti.child(2:3)),:) = 0; % remove the information of child information
           
                % child-realted changes
                T(T1,Ti.child) = 0; % has no child now
                if T(T1,Ti.mother) ~= 0 % not pioneer, has mother
                    if T(T(T(T1,Ti.mother),Ti.child(2)),Ti.child(1))==0 && T(T(T(T1,Ti.mother),Ti.child(3)),Ti.child(1))==0
                        T(T(T1,Ti.mother),Ti.grandchild) = 0; % mother has no grandchild now
                    end
                                     
                end
            end
 
            TC(1) = []; % remove the triangle from TC
            T(T1,1) = 1; % indicates that this trinalg has been examined
        else % then, the boundary is not boundary
            T2 = T(T1,Ti.neighbor(2)); index_p = [T1 T2];
            mean_c = (c(T(T1,Ti.vertex(1)))+c(T(T1,Ti.vertex(2)))+c(T(T1,Ti.vertex(3))));
            mean_c = mean_c + (c(T(T2,Ti.vertex(1)))+c(T(T2,Ti.vertex(2)))+c(T(T2,Ti.vertex(3))));
            mean_c = mean_c/6.0;
            if (mean_c>cri || mean_c<-cri) % need coarsened
            
            % c121 = abs(c(T(T1,Ti.vertex(1)))-c(T(T1,Ti.vertex(2))));
            % c231 = abs(c(T(T1,Ti.vertex(1)))-(c(T(T1,Ti.vertex(2)))+c(T(T1,Ti.vertex(3))))/2)*sqrt(2);
            % c311 = abs(c(T(T1,Ti.vertex(3)))-c(T(T1,Ti.vertex(1))));
            % c122 = abs(c(T(T2,Ti.vertex(1)))-c(T(T2,Ti.vertex(2))));
            % c232 = abs(c(T(T2,Ti.vertex(1)))-(c(T(T2,Ti.vertex(2)))+c(T(T2,Ti.vertex(3))))/2)*sqrt(2);
            % c312 = abs(c(T(T2,Ti.vertex(3)))-c(T(T2,Ti.vertex(1))));
            % if c121<cri && c231<cri && c311<cri && c122<cri && c232<cri && c312<cri % need coarsened
                
                % neighbor-related changes
                if T(T1,Ti.neighbor(1))~=0
                    ind_n = T(T(T1,Ti.child(2)),Ti.neighbor(2)); % index of T1's 1st child's principal neighbor
                    T(T1,Ti.neighbor(1)) = ind_n;
                    n_ind = logical(T(ind_n,Ti.neighbor)==T(T1,Ti.child(2))); % find which neighbor of ind_n is T1's 1st child
                    T(ind_n,Ti.neighbor(n_ind)) = T1;
                end
                
                if T(T1,Ti.neighbor(3))~=0
                    ind_n = T(T(T1,Ti.child(3)),Ti.neighbor(2)); % index of T1's 2nd child's principal neighbor
                    T(T1,Ti.neighbor(3)) = ind_n;
                    n_ind = logical(T(ind_n,Ti.neighbor)==T(T1,Ti.child(3))); % find which neighbor of ind_n is T1's 2nd child
                    T(ind_n,Ti.neighbor(n_ind)) = T1;
                end
                
                if T(T2,Ti.neighbor(1))~=0
                    ind_n = T(T(T2,Ti.child(2)),Ti.neighbor(2)); % index of T1's 1st child's principal neighbor
                    T(T2,Ti.neighbor(1)) = ind_n;
                    n_ind = find(T(ind_n,Ti.neighbor)==T(T2,Ti.child(2))); % find which neighbor of ind_n is T1's 1st child
                    T(ind_n,Ti.neighbor(n_ind)) = T2;
                end
                
                if T(T2,Ti.neighbor(3))~=0
                    ind_n = T(T(T2,Ti.child(3)),Ti.neighbor(2)); % index of T2's 2nd child's principal neighbor
                    T(T2,Ti.neighbor(3)) = ind_n;
                    n_ind = find(T(ind_n,Ti.neighbor)==T(T2,Ti.child(3))); % find which neighbor of ind_n is T2's 2nd child
                    T(ind_n,Ti.neighbor(n_ind)) = T2;
                end
                
                P(T(T(T1,Ti.child(2)),Ti.vertex(1))) = 0; % remove the information of the mid-point of long edge
                T(T(T1,Ti.child(2:3)),:) = 0; % remove the information of child information
                T(T(T2,Ti.child(2:3)),:) = 0;% remove the information of child information
                
                % child-realted changes
                T(index_p,Ti.child) = 0; % has no child now
                if T(T1,Ti.mother) ~= 0 % not pioneer, has mother
                    if T(T(T(T1,Ti.mother),Ti.child(2)),Ti.child(1))==0 && T(T(T(T1,Ti.mother),Ti.child(3)),Ti.child(1))==0
                        T(T(T1,Ti.mother),Ti.grandchild) = 0; % mother has no grandchild now
                    end
                    
                    if T(T(T(T2,Ti.mother),Ti.child(2)),Ti.child(1))==0 && T(T(T(T2,Ti.mother),Ti.child(3)),Ti.child(1))==0
                        T(T(T2,Ti.mother),Ti.grandchild) = 0; % mother has no grandchild now
                    end                    
                end
            end
 
            TC([1 find(TC==T2)]) = []; % remove the triangle from TC
            T([T1 T2],1) = 1; % indicates that this trinalg has been examined
        end
    end
    
    [TC] = search_CT(T,Ti);
    
end

%% update the T,P,x,y,c
index_DP = find(P==0); % get the index of P need to be deleted
index_RT = find(T(:,Ti.vertex(1))~=0); % get index of remaining triangles
index_DT = find(T(:,Ti.vertex(1)) == 0); % index of useless triangles
crement_P = zeros(length(P),1);
for i = 1:length(index_DP)
    crement_P(index_DP(i)+1:end) = crement_P(index_DP(i)+1:end) - 1; % crement of P index 
end
x(index_DP) = []; y(index_DP) = []; c(index_DP) = []; % delete the unnecessary mid-points
T(index_RT,Ti.vertex)=T(index_RT,Ti.vertex) + crement_P(T(index_RT,Ti.vertex)); % update the vertex index
P=[1:length(x)];

crement_T = zeros(length(T(:,1)),1);
for i = 1:length(index_DT)
    crement_T(index_DT(i)+1:end) = crement_T(index_DT(i)+1:end) - 1; % crement of triangle index
end
% update the triangle index of mother, sister, child, and neighbor
index_mother=find(T(:,Ti.mother)~=0);
T(index_mother,Ti.mother) = T(index_mother,Ti.mother) + crement_T(T(index_mother,Ti.mother));
index_sister=find(T(:,Ti.sister)~=0);
T(index_sister,Ti.sister) = T(index_sister,Ti.sister) + crement_T(T(index_sister,Ti.sister));
index_child=find(T(:,Ti.child(1))~=0);
T(index_child,Ti.child(2)) = T(index_child,Ti.child(2)) + crement_T(T(index_child,Ti.child(2)));
T(index_child,Ti.child(3)) = T(index_child,Ti.child(3)) + crement_T(T(index_child,Ti.child(3)));
index_neighbor=find(T(:,Ti.neighbor(1))~=0);
T(index_neighbor,Ti.neighbor(1)) = T(index_neighbor,Ti.neighbor(1)) + crement_T(T(index_neighbor,Ti.neighbor(1)));
index_neighbor=find(T(:,Ti.neighbor(2))~=0);
T(index_neighbor,Ti.neighbor(2)) = T(index_neighbor,Ti.neighbor(2)) + crement_T(T(index_neighbor,Ti.neighbor(2)));
index_neighbor=find(T(:,Ti.neighbor(3))~=0);
T(index_neighbor,Ti.neighbor(3)) = T(index_neighbor,Ti.neighbor(3)) + crement_T(T(index_neighbor,Ti.neighbor(3)));
T(index_DT,:) = []; % delete the information of deleted triangles
end