function results = mutate(popx,params)
mp = params.mp;
results = popx;
for i=1:params.pop
    for j=1:params.vars
        if rand() < mp
            %变异，重新生成
            results(i,j) = params.lower + rand()* ( params.upper - params.lower);
        end
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end