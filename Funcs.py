#coding:utf-8
import math

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
    fit = 100.0/(func+1.0)
    return fit


def Ackley(X):
    x = X[0]
    y = X[1]
    ret = -20 * math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.exp(1) + 20
    return ret
def Ackley_Fitness(X):
    func = Ackley(X)
    if func <= 1.0e-10:
        func = 1.0e-10
    fit = 100.0/(func+1)
    return fit