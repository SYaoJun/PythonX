import numpy as np
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5])
Y1 = np.array([88,99,100,78,82])
Y2 = np.array([99,44,111,73,90])
plt.plot(X, Y1,  label="AAA")
plt.plot(X, Y2,  label="BBB")
plt.xlabel("The Books")
plt.ylabel("Number")
plt.legend()
# plt.grid()
plt.show()