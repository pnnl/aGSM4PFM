function [T,P,x,y,c] = refine(T,Ti,P,x,y,c,cri,n_level)
T(:,1) = 0;
while true

    % Identify triangles to consider (TC)
    TC = find(T(:,1)==0 & T(:,Ti.child(1))==0 & T(:,Ti.level) < n_level);
    if isempty(TC)
        break
    end

    % -----------------------------
    % Vectorized computation upfront
    % -----------------------------

    % get all vertices in one go
    v1 = T(TC, Ti.vertex(1));
    v2 = T(TC, Ti.vertex(2));
    v3 = T(TC, Ti.vertex(3));

    % compute edge-based criteria in vectorized form
    mean_c = (c(v1) + c(v2) + c(v3))/3.0;

    % determine which triangles do NOT need refinement
    no_refine = (abs(mean_c)>cri);

    % mark them as processed
    T(TC(no_refine), 1) = 1;

    % remaining triangles that need refinement
    refine_indices = TC(~no_refine);

    % -----------------------------
    % Single loop over refinement only
    % -----------------------------
    for idx = refine_indices'

        % skip if it has been refined already
        if T(idx, Ti.child(1)) == 1
            T(idx,1) = 1;
            continue
        end

        % refine main triangle
        [T,P,x,y,c] = refine_TR(T, Ti, P, x, y, c, idx);

        % child-level
        lvl = T(idx, Ti.level);

        % find children:
        c2 = T(idx, Ti.child(2));
        c3 = T(idx, Ti.child(3));

        % refine second child if needed
        if lvl < n_level-1
            [T,P,x,y,c] = refine_TR(T, Ti, P, x, y, c, c2);
        end

        % refine third child if needed
        if lvl < n_level-1
            [T,P,x,y,c] = refine_TR(T, Ti, P, x, y, c, c3);
        end
    end
end

end