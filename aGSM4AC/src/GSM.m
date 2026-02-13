function [ddf] = GSM (x,y,f,ds,T,lev)

%% ---- Precompute triangle node indices ----
i1 = T(:,1);  i2 = T(:,2);  i3 = T(:,3);

%% ---- Pull coordinates and values in matrix form ----
X = x(T);   Y = y(T);   F = f(T);

x1 = X(:,1);  x2 = X(:,2);  x3 = X(:,3);
y1 = Y(:,1);  y2 = Y(:,2);  y3 = Y(:,3);
f1 = F(:,1);  f2 = F(:,2);  f3 = F(:,3);

%% ---- Mid-edge averages ----
f_T1 = (f1+f2)/2;
f_T2 = (f2+f3)/2;
f_T3 = (f3+f1)/2;

%% ---- ds coefficients ----
dsx12 = (2*y3 - y1 - y2)/6;      dsy12 = (2*x3 - x1 - x2)/6;
dsx23 = (2*y1 - y2 - y3)/6;      dsy23 = (2*x1 - x2 - x3)/6;
dsx31 = (2*y2 - y3 - y1)/6;      dsy31 = (2*x2 - x3 - x1)/6;

%% ---- Compute fluxes on each edge ----
dfx12 = f_T1 .* dsx12;   dfy12 = f_T1 .* dsy12;
dfx23 = f_T2 .* dsx23;   dfy23 = f_T2 .* dsy23;
dfx31 = f_T3 .* dsx31;   dfy31 = f_T3 .* dsy31;

%% ---- Index arrays for accumarray ----
idx = [i1; i2; i3];

%% ---- Assemble S ----
ss = (ds*ds/6) ./ (2.^lev);
S = accumarray(idx, [ss; ss; ss], size(f));

%% ---- Assemble dfx and dfy ----
dfx = accumarray(idx, ...
    [dfx12 - dfx31; dfx23 - dfx12; dfx31 - dfx23], size(f));

dfy = accumarray(idx, ...
    [dfy12 - dfy31; dfy23 - dfy12; dfy31 - dfy23], size(f));

%% ---- Normalize and apply BC ----
dfx = dfx ./ S;  
dfy = -dfy ./ S;
dfx(x==0 | x==1) = 0;
dfy(y==0 | y==1) = 0;

%% ---- Values at triangle nodes ----
dfx1 = dfx(i1);  dfx2 = dfx(i2);  dfx3 = dfx(i3);
dfy1 = dfy(i1);  dfy2 = dfy(i2);  dfy3 = dfy(i3);

%% ---- Edge lengths and tangents ----
l12 = hypot(x2-x1, y2-y1);
l23 = hypot(x3-x2, y3-y2);
l31 = hypot(x1-x3, y1-y3);

tx12 = (x2 - x1)./l12;   ty12 = (y2 - y1)./l12;
tx23 = (x3 - x2)./l23;   ty23 = (y3 - y2)./l23;
tx31 = (x1 - x3)./l31;   ty31 = (y1 - y3)./l31;

Ul12 = (f2 - f1)./l12;
Ul23 = (f3 - f2)./l23;
Ul31 = (f1 - f3)./l31;

%% ---- Directional corrected df ----
ddfx12 = (dfx1+dfx2)/2;  ddfy12 = (dfy1+dfy2)/2;
ddfx23 = (dfx2+dfx3)/2;  ddfy23 = (dfy2+dfy3)/2;
ddfx31 = (dfx3+dfx1)/2;  ddfy31 = (dfy3+dfy1)/2;

ut12 = ddfx12.*tx12 + ddfy12.*ty12;
ut23 = ddfx23.*tx23 + ddfy23.*ty23;
ut31 = ddfx31.*tx31 + ddfy31.*ty31;

ddfx12 = ddfx12 - (ut12 - Ul12).*tx12;
ddfy12 = ddfy12 - (ut12 - Ul12).*ty12;
ddfx23 = ddfx23 - (ut23 - Ul23).*tx23;
ddfy23 = ddfy23 - (ut23 - Ul23).*ty23;
ddfx31 = ddfx31 - (ut31 - Ul31).*tx31;
ddfy31 = ddfy31 - (ut31 - Ul31).*ty31;

%% ---- Final scaling ----
ddfx12 = ddfx12 .* dsx12;    ddfy12 = ddfy12 .* dsy12;
ddfx23 = ddfx23 .* dsx23;    ddfy23 = ddfy23 .* dsy23;
ddfx31 = ddfx31 .* dsx31;    ddfy31 = ddfy31 .* dsy31;

%% ---- Final assembly of ddfx and ddfy ----
ddfx = accumarray(idx, ...
    [ddfx12 - ddfx31; ddfx23 - ddfx12; ddfx31 - ddfx23], size(f));

ddfy = accumarray(idx, ...
    [ddfy31 - ddfy12; ddfy12 - ddfy23; ddfy23 - ddfy31], size(f));

%% ---- Apply boundary conditions ----
ddfx(x==0 | x==1) = 0;
ddfy(y==0 | y==1) = 0;

%% ---- Final Laplacian ----
ddf = (ddfx + ddfy) ./ S;

end
