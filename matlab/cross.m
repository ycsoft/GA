function results = cross(popx,params)
%
% cr : �������
%

r = params.pop;
c = params.vars;

%��������
newx = popx;
cr = params.cp;
for i=1:r
    %���Ƚ���
    for j=1:c
        p = rand();
        if p <= cr
         %�Ա���ʵʩ����
         %��ʽ1�� ˫�彻��
         %%%˫�彻��
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