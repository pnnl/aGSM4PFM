function [c] = Initial_Geom(x, y)
% This function determines the initial concentration value based on
% location.
if abs(x-0.5)<0.3 && abs(y-0.5)<0.05
    c = 1.0;
else
    c = -1.0;
end

end

