#coding:utf-8

import numpy as np

import Funcs

import random

POP = 10     #种群规模
CP = 0.6     #交叉概率
VARS = 5     #优化变量个数
MP = 0.1

LOWER = -5
UPPER = 5

new_X = None
old_X = None
pool_X = None

FUNC_TIMES = 0

#适应度
FITNESS = None

#锦标赛规模
FIGHT_N = 2


def _find_best_competetor():
    """
    锦标赛选择算法
    选择最优个体的下标
    """
    indices = []
    best_id = 0
    best = 0
    # 随机选取FIGHT_N个个体
    for i in xrange(FIGHT_N):
        indices.append( random.randint(0,POP-1) )
    best = FITNESS[0][indices[0]]
    for id in indices:
        if FITNESS[0][id] < best:
            best_id = id
            best = FITNESS[0][id]
    return best_id

def init():
    old_X = LOWER + np.random.rand(POP, VARS) * (UPPER - LOWER)
    FITNESS = np.zeros([1,POP])
    new_X = old_X.copy()
def evaluate():
    for pop in xrange(POP):
        FITNESS[0][pop] = Funcs.Sphere(new_X[pop,:])

def select():
    for i in xrange(POP):
        pass
