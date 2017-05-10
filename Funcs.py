#coding:utf-8

def Sphere(X):
    """
    :param X: numpy的二维数组， 1 x n
    :return:
    """
    ret = 0
    (row,col) = X.shape
    for i in xrange(col):
        ret += X[0][i] ** 2
    return  ret