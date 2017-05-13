#coding:utf-8

import numpy as np
import Funcs
import random
import GAConf as gaconf
import logging

wheel = None

def _find_best_competetor():
    """
    锦标赛选择算法
    选择最优个体的下标
    """
    #global FITNESS,FIGHT_N
    indices = []
    best_id = 0
    best = 0
    # 随机选取FIGHT_N个个体
    for i in xrange(gaconf.FIGHT_N):
        indices.append( random.randint(0,gaconf.POP-1) )
    best = gaconf.FITNESS[0][indices[0]]
    for id in indices:
        if gaconf.FITNESS[0][id] < best:
            best_id = id
            best = gaconf.FITNESS[0][id]
    return best_id

def _find_by_wheel():
    """
    轮盘赌选择
    :return:
    """
    global  wheel
    """
    先根据适应度构造赌轮
    """
    fit_all = np.sum(gaconf.FITNESS)
    id = 0
    wheel = np.zeros(gaconf.POP)
    pre = 0
    for fit in gaconf.FITNESS[0]:
        prob_cmp = 1.0*fit/fit_all
        wheel[id] = pre + prob_cmp
        print(wheel)
        pre = wheel[id]
        #if prob <= fit_prob[id]:
        #    return id
        id += 1
    """
    根据不同个体的适应度，依据轮盘赌
    算法选择个体
    """
    for i in xrange(gaconf.POP):
        prob = random.random()
        for id in xrange(gaconf.POP):
            if prob <= wheel[id]:
                print ('选中个体:%d'%id)
                break



def init():
    #global LOWER,POP,UPPER,FITNESS,old_X,new_X
    old_X = gaconf.LOWER + np.random.rand(gaconf.POP, gaconf.VARS) * (gaconf.UPPER - gaconf.LOWER)
    gaconf.FITNESS = np.ones([1,gaconf.POP])
    new_X = old_X.copy()
def evaluate():
    for pop in xrange(gaconf.POP):
        gaconf.FITNESS[0][pop] = Funcs.Sphere(gaconf.new_X[pop,:])


def select_std():
    """
    轮盘赌选择
    :return:
    """
    #计算总适应度


    for i in xrange(gaconf.POP):
        pass



if __name__ == '__main__':
    init()
    ga = gaconf.FITNESS

    _find_by_wheel()