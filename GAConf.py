#coding:utf-8


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
