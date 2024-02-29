import matplotlib.pyplot as plt
import FirstInFirstOut 
import LeastRecentlyUsed 
import OptimalAlgorithm 
import testdata 

data=testdata.test3arr
maxF=3

# execute all algorithms
x1=FirstInFirstOut.fifo(data,maxF)
x2=OptimalAlgorithm.opt(data,maxF)
x3=LeastRecentlyUsed.lru(data,maxF)

# plot all algorithms faults
plt.plot(x1,label="FIFO")
plt.plot(x2,label="Optimal")
plt.plot(x3,label="LRU")
plt.xlabel("Time")
plt.ylabel("Faults")
plt.legend(loc='lower right')
plt.grid()
plt.show()








