function [results,best] = select(newx,params,fitfunc)
%
% 选择适应度高的个体进入下一代
%
fitness = zeros(1,params.pop);

%先计算每个个体的适应度
for i=1:params.pop
    fitness(i) = feval(fitfunc,newx(i,:));
end

best = max(fitness);

allfit = sum(fitness);
fitness = fitness / allfit;

for i=2:params.pop
    fitness(i) = fitness(i) + fitness(i-1);
end

results = zeros(params.pop,params.vars);

for i=1:params.pop
    rnd = rand();
    idx = find(fitness >= rnd );
    idx = idx(1); %被选中的个体
    results(i,:) = newx(idx,:);
end

end