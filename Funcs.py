#coding:utf-8
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

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

def draw_Sphere():
    X = np.arange(-5,5,0.1)
    [X,Y] = np.meshgrid(X,X)
    Z = X**2 + Y**2
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(X,Y,Z,cmap=cm.YlGn,
                       linewidth=0, antialiased=True,shade=True,rstride=1,cstride=1)
    #ax.set_zlim(-1.01, 1.01)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    #fig.colorbar(surf, shrink=0.5, aspect=1)
    plt.show()



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


draw_Sphere()