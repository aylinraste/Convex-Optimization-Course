from cvxpy import *
from zero_crossings_data import *
import matplotlib.pyplot as plt
import math

a = Variable(B)
b = Variable(B)

Y = Variable(n)

constraints = [multiply(Y, s) >= 0, scalar_product(Y, s) == n]
for i in range(n):
    y_i = 0
    for j in range(1,B+1):
        y_i += a[j-1] * math.cos(2 * math.pi / n * (f_min + j - 1) * i) + b[j-1] * math.sin(2 * math.pi / n * (f_min + j - 1) * i)
    constraints += [Y[i] == y_i]

obj = Minimize(norm(Y))

prob = Problem(obj, constraints)
sol = prob.solve()
print(sol)
print("the relative recovery error:" , np.linalg.norm(y - Y.value) / np.linalg.norm(y))

plt.figure()
plt.plot(np.arange(0, n), y, color='tab:blue', label="y")
plt.plot(np.arange(0, n), Y.value, color='tab:orange', linestyle='--', label="Y")
plt.xlim([0, n])
plt.legend(loc="lower left")
plt.savefig("signal recovery.png")
plt.show()