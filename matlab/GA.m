%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% �Ŵ��㷨
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;clc;
params.pop = 40; %��Ⱥ��ģ
params.vars = 5; %������Ŀ
params.max_iter = 50; %��������
params.lower = -5;
params.upper = 5;
params.cp = 0.5;
params.mp = 0.01; 

%������ʼ��Ⱥ
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


















