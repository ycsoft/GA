function results = mutate(popx,params)
mp = params.mp;
results = popx;
for i=1:params.pop
    for j=1:params.vars
        if rand() < mp
            %���죬��������
            results(i,j) = params.lower + rand()* ( params.upper - params.lower);
        end
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end