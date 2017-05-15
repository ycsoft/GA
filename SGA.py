#coding:utf-8

import numpy as np
import Funcs
import random
import GAConf as gaconf
import logging
import matplotlib.pyplot as plt

wheel = None
history = []

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
    dict_select = {}
    global  wheel
    gaconf.old_X = gaconf.new_X.copy()
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
        #print(wheel)
        pre = wheel[id]
        #if prob <= fit_prob[id]:
        #    return id
        id += 1
        dict_select[str(fit)] = 0
    """
    根据不同个体的适应度，依据轮盘赌
    算法选择个体
    """
    #print(wheel)
    for i in xrange(gaconf.POP):
        prob = random.random()
        selected = 0
        for id in xrange(gaconf.POP):
            if prob <= wheel[id]:
                key = str(gaconf.FITNESS[0,id])
                #print ('选中个体:%d, 该个体适应度为:%f'%(id,gaconf.FITNESS[0,id]))
                selected = id
                if key not in dict_select.keys():
                    print ('Key not found:%s'%key)
                dict_select[ key ] = dict_select[ key ] + 1
                break
        gaconf.new_X[i,:] = gaconf.old_X[selected,:]

    """
    测试打印
    """
    # for k,v in dict_select.items():
    #     print('Fit:%s , Times:%d'%(k,v))





def init():
    #global LOWER,POP,UPPER,FITNESS,old_X,new_X
    gaconf.old_X = gaconf.LOWER + np.random.rand(gaconf.POP, gaconf.VARS) * (gaconf.UPPER - gaconf.LOWER)
    gaconf.FITNESS = np.ones([1,gaconf.POP])
    gaconf.new_X = gaconf.old_X.copy()

def evaluate():
    """
    计算种群中个体的适应度
    :return:
    """
    for pop in xrange(gaconf.POP):
        gaconf.FITNESS[0,pop] = Funcs.Sphere_Fitness(gaconf.new_X[pop,:])


def select_std():
    """
    轮盘赌选择
    :return:
    """
    _find_by_wheel()


def cross():
    """
    遗传算法的交叉操作,每次选择两个个体进行交叉
    :return:
    """
    for i in xrange(gaconf.POP):
        #满足交叉概率
        if random.random()  < gaconf.CP:
            [m,n] = np.random.random(2) * gaconf.POP
            m = int(m)
            n = int(n)
            #选择交叉点
            pos = random.randint(0,gaconf.VARS-1)
            gaconf.new_X[i, pos] =  gaconf.new_X[i,pos]*0.6  + 0.4 *(gaconf.old_X[m, pos] - gaconf.old_X[n, pos])
            # for j in xrange(gaconf.VARS):
            #     if random.random() < gaconf.CP:
            #         gaconf.new_X[i,j] = (gaconf.old_X[m,j] + gaconf.old_X[n,j])/2
            #gaconf.new_X[i,:] = (gaconf.old_X[m,:] + gaconf.old_X[n,:])/2
        else:
            gaconf.new_X[i,:] = gaconf.old_X[i,:]

def mutate():
    """
    遗传算法变异操作
    :return:
    """
    for i in xrange(gaconf.POP):
        if random.random() < gaconf.MP:
            #选择变异位置
            pos = random.randint(0,gaconf.VARS-1)
            gaconf.new_X[i,pos] = gaconf.LOWER + (gaconf.UPPER - gaconf.LOWER)*random.random()

def out_best():
    global history
    best_fit = gaconf.FITNESS[0,0]
    best  = 0
    sz = len(gaconf.FITNESS[0,:])
    for i in xrange(sz):
        if best_fit < gaconf.FITNESS[0,i]:
            best_fit = gaconf.FITNESS[0,i]
            best = i

    print ("Best Fit: %f"%best_fit)

    #print ("Best IND:",gaconf.new_X[best,:])
    history.append(best_fit)

if __name__ == '__main__':
    init()
    max_iter = 500
    for i in xrange( max_iter ):
        cross()
        mutate()
        evaluate()
        select_std()
        out_best()
    l = len(history)
    plt.plot([x for x in xrange(l)],history)
    plt.show()
