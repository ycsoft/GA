function [results,best] = select(newx,params,fitfunc)
%
% ѡ����Ӧ�ȸߵĸ��������һ��
%
fitness = zeros(1,params.pop);

%�ȼ���ÿ���������Ӧ��
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
    idx = idx(1); %��ѡ�еĸ���
    results(i,:) = newx(idx,:);
end

end