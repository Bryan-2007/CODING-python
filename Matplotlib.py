# Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.axis('off')
plt.title("1st graph")

x = np.array([9, 7, 5, 3])
y = np.array([3, 2, 1, 7])
plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.axis('off')
plt.title("2nd graph")

x = np.array([4, 2, 5, 1])
y = np.array([5, 2, 9, 7])
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.title("3rd graph")
plt.axis('off')

x = np.array([9, 7, 5, 3])
y = np.array([3, 2, 1, 7])
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.title("4th graph")

plt.suptitle("super title")
plt.axis("off")
plt.show()

# Histogram 

import matplotlib.pyplot as plt
import numpy as np

x = np.array([[1, 2], [3, 4]])
plt.hist(x)
plt.show()

# Matrix Multiplication

import numpy as np

A = np.array([[1, 2], [3, 4], [3, 1]])  # 3 by 2
B = np.array([[5], [7]])                # 2 by 1

C = np.dot(A, B)                        # 3 by 1
print(C)

# Scipy

'''solve for x and y for linear equation in two var:
3x + 4y = 12
5x - 2y = 10'''

import numpy as np
import scipy.linalg as sp

x = np.array([[3, 4], [5, -2]])
y = np.array([12, 10])
print(sp.solve(x, y))
