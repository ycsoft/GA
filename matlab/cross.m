function results = cross(popx,params)
%
% cr : 交叉概率
%

r = params.pop;
c = params.vars;

%复制数组
newx = popx;
cr = params.cp;
for i=1:r
    %均匀交叉
    for j=1:c
        p = rand();
        if p <= cr
         %对变量实施交叉
         %方式1： 双体交叉
         %%%双体交叉
        a = rand() - 0.5;
        b = rand() - 0.5;
        ind = rand(1,2)*r;
        m = ceil(ind(1));
        n = ceil(ind(2));
        newx(i,j) = a * popx(m,j) + b * popx(n,j);
        end
    end
end
results = newx;
end