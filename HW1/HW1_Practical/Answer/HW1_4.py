from cvxpy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

lmbda = Variable(24)
p = Parameter(nonneg = True)

N = np.array([0, 4, 2, 2, 3, 0, 4, 5, 6, 6, 4, 1, 4, 4, 0, 1, 3, 4, 2, 0, 3, 2, 0, 1])
possible_p = np.array([0.1, 1, 10, 100])

constraints = [lmbda >= 0]
obj = Maximize(-sum(lmbda) + N @ log(lmbda) - p * (sum_squares(diff(lmbda)) + sum_squares(hstack([lmbda[0] - lmbda[23]]))))
prob = Problem(obj, constraints)
possible_lmbda = []
for pp in possible_p:
    p.value = pp
    sol = prob.solve()
    possible_lmbda.append(lmbda.value)
    print (lmbda.value)
    plt.plot(np.arange(24), lmbda.value, label="plot %.1f" %pp)
plt.legend()
plt.savefig("Poisson distribution.png")
plt.show()

N_test = np.array([0, 1, 3, 2, 3, 1, 4, 5, 3, 1, 4, 3, 5, 5, 2, 1, 1, 1, 2, 0, 1, 2, 1, 0])
max = [-100000, 0]
for i in range(4):
    loglikelihood= np.sum(np.log(np.exp(-possible_lmbda[i]) * possible_lmbda[i]**N_test / factorial(N_test)))
    if loglikelihood > max[0]:
        max = [loglikelihood, possible_p[i]]
    print(f"log likelihood = {loglikelihood} for p = { possible_p[i]}")
print(f"max log likelihood = {max[0]} and p is {max[1]}")