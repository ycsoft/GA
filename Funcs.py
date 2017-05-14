#coding:utf-8

def Sphere(X):
    """
    :param X: numpy的二维数组， 1 x n
    :return:
    """
    ret = 0
    for v in X:
        ret += v**2
    return ret

def Sphere_Fitness(X):
    func = Sphere(X)
    fit = 1.0/func
    return fit