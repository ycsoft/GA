#coding:utf-8


POP = 40     #种群规模
CP = 0.9     #交叉概率
VARS = 2     #优化变量个数
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

#迭代次数
max_iter = 50

#运行次数
run_times = 10