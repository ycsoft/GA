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

FITNESS = None

FIGHT_N = 2

def _find_best():
    indices = []
    best_id = 0
    best = 0
    for i in xrange(FIGHT_N):
        indices.append( random.randint(0,POP-1) )
    best = FITNESS[0][indices[0]]
    for id in xrange(POP-1):
        if FITNESS[0][id] < best
            best_id = id+1
            best = FITNESS[0][id]

def init():
    old_X = LOWER + np.random.rand(POP, VARS) * (UPPER - LOWER)
    FITNESS = np.zeros([1,POP])
    new_X = old_X.copy()
def evaluate():
    for pop in xrange(POP):
        FITNESS[0][pop] = Funcs.Sphere(new_X[pop,:])

def select():
    for i in xrange(POP):
