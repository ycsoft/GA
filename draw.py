#coding:utf-8

import matplotlib.pyplot as plt

f = open('20.txt').read().split("\n")
y = []
for line in f:
    y.append(line)
sz = len(y)
print(sz)
x = [i+1 for i in xrange(sz)]
print(x)
print(y)
plt.plot(x,y)
plt.xlabel('Iteration')
plt.ylabel('Best Fitness')
plt.show()