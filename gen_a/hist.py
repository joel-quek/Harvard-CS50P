from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

a = ["some file", "22", "43", "11","34", "26"]

r = list(map(int, (a[1], a[2], a[3], a[4], a[5])))
s = np.array([int((x - min(r))/(max(r) - min(r)) * 10) for x in r])

plt.bar(np.arange(len(s)), s)
plt.show()

# https://www.youtube.com/watch?v=XDv6T4a0RNc 
# https://stackoverflow.com/questions/43264883/plotting-a-numpy-array-as-a-histogram