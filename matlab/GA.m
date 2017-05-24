%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% 遗传算法
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;clc;
params.pop = 40; %种群规模
params.vars = 5; %变量数目
params.max_iter = 50; %迭代次数
params.lower = -5;
params.upper = 5;
params.cp = 0.5;
params.mp = 0.01; 

%生产初始种群
newx = params.lower + rand(params.pop,params.vars) .* (params.upper - params.lower);
oldx = newx;
hist=zeros(params.max_iter);
for i=1:params.max_iter
    newx=cross(newx,params);
    newx=mutate(newx,params);
    [newx,best] = select(newx,params,'sphere');
    hist(i) = best;
end
plot(hist)


















