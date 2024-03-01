# import matplotlib

# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([45, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

x = lambda a : a*a

print(x(2))

x = lambda a,b,c : a*b*c
print(x(2,3,4))

# x = lambda n : n(n-1) if n%2 ==0
print(x(10))