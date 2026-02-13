function [T,P,x,y,c] = refine_TR_inner (T,Ti,P,TR,x,y,c)
% This function refine the triangles in TR completely
while ~isempty(TR)

    % ----- Extract last two triangles -----
    T10 = TR(end);
    T20 = TR(end-1);
    TR(end-1:end) = [];

    % ======== REFINEMENT FOR T10 ==========
    oldTlen = size(T,1);
    T1 = oldTlen + 1;
    T2 = oldTlen + 2;

    T(oldTlen+1:oldTlen+2,:) = 0;

    P123 = T(T10,Ti.vertex);
    P1 = P123(1); P2 = P123(2); P3 = P123(3);

    Pmid = numel(P) + 1;
    P(end+1) = Pmid;

    x(end+1) = 0.5*(x(P2) + x(P3));
    y(end+1) = 0.5*(y(P2) + y(P3));
    c(end+1) = 0.5*(c(P2) + c(P3));

    T([T1 T2],1) = T(T10,1);
    T(T1,Ti.vertex) = [Pmid P1 P2];
    T(T2,Ti.vertex) = [Pmid P3 P1];

    T(T1,Ti.mother) = T10;
    T(T2,Ti.mother) = T10;
    T(T10,Ti.child) = [1 T1 T2];

    if T(T10,Ti.mother) ~= 0
        T00 = T(T10,Ti.mother);
        T(T00,Ti.grandchild) = 1;
    end

    T(T1,Ti.sister) = T2;
    T(T2,Ti.sister) = T1;

    % ======== REFINEMENT FOR T20 ==========
    oldTlen = size(T,1);
    T3 = oldTlen + 1;
    T4 = oldTlen + 2;

    T(oldTlen+1:oldTlen+2,:) = 0;

    P456 = T(T20,Ti.vertex);
    P4 = P456(1); P5 = P456(2); P6 = P456(3);

    T([T3 T4],1) = T(T20,1);

    T(T3,Ti.vertex) = [Pmid P4 P5];
    T(T4,Ti.vertex) = [Pmid P6 P4];

    T(T3,Ti.mother) = T20;
    T(T4,Ti.mother) = T20;
    T(T20,Ti.child) = [1 T3 T4];

    if T(T20,Ti.mother) ~= 0
        T00 = T(T20,Ti.mother);
        T(T00,Ti.grandchild) = 1;
    end

    T(T3,Ti.sister) = T4;
    T(T4,Ti.sister) = T3;

    newLevel = T(T20,Ti.level)+1;
    T([T1 T2 T3 T4],Ti.level) = newLevel;

    % ======== NEIGHBOR UPDATE ==========
    shared26 = (P2 == P6);

    if shared26
        T(T1,Ti.neighbor) = [T2 T(T10,Ti.neighbor(1)) T4];
        T(T2,Ti.neighbor) = [T3 T(T10,Ti.neighbor(3)) T1];
        T(T3,Ti.neighbor) = [T4 T(T20,Ti.neighbor(1)) T2];
        T(T4,Ti.neighbor) = [T1 T(T20,Ti.neighbor(3)) T3];
    else
        T(T1,Ti.neighbor) = [T2 T(T10,Ti.neighbor(1)) T3];
        T(T2,Ti.neighbor) = [T1 T(T10,Ti.neighbor(3)) T4];
        T(T3,Ti.neighbor) = [T4 T(T20,Ti.neighbor(1)) T1];
        T(T4,Ti.neighbor) = [T3 T(T20,Ti.neighbor(3)) T2];
    end

    % ======== FIX NEIGHBOR-OF-NEIGHBOR LINKS ==========
    neighList = [ ...
        T10 Ti.neighbor(1) T1 ; 
        T10 Ti.neighbor(3) T2 ;
        T20 Ti.neighbor(1) T3 ;
        T20 Ti.neighbor(3) T4 ];

    for r = 1:size(neighList,1)
        tri = neighList(r,1);
        nb = T(tri, neighList(r,2));
        newTri = neighList(r,3);
        if nb ~= 0
            idx = (T(nb,Ti.neighbor) == tri);
            T(nb,Ti.neighbor(idx)) = newTri;
        end
    end
    
    % ======== PUSH NEXT TRIANGLE INTO TR STACK ==========
    if numel(TR) >= 1
        if any(T(TR(end),Ti.neighbor) == T3)
            TR(end+1) = T3;
        else
            TR(end+1) = T4;
        end
    end

end

end