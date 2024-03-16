import matplotlib.pyplot as plt
from FirstInFirstOut import *
from LeastRecentlyUsed import *
from OptimalAlgorithm import *
from testdata import *

data=exStr
maxF=3

# execute all algorithms
x1=fifo(data,maxF)
x2=opt(data,maxF)
x3=lru(data,maxF)

# plot all algorithms faults
plt.plot(x1,label="FIFO")
plt.plot(x2,label="Optimal")
plt.plot(x3,label="LRU")
plt.xlabel("Time")
plt.ylabel("Faults")
plt.legend(loc='lower right')
plt.grid()
plt.show()








