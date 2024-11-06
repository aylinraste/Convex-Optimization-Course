from cvxpy import *
from disks_data import *
from numpy import linalg as LA

C = Variable((n,2))
R = Variable(n)

constraints = [R >= 0, R[:k] == Rgiven, C[:k, :] == Cgiven]
for i in range(len(Gindexes)):
    constraints += [norm(C[Gindexes[i,0], : ] - C[Gindexes[i,1], : ]) <= R[Gindexes[i,0]] + R[Gindexes[i,1]]]

area_obj = np.pi * Minimize(sum_squares(R))
perimeter_obj = 2 * np.pi * Minimize(sum(R))

area_prob = Problem(area_obj, constraints)
perimeter_prob = Problem(perimeter_obj, constraints)

area_sol = area_prob.solve()
print("optimal area is:" , area_sol)
plot_disks(C.value, R.value, Gindexes, name = "areas")

perimeter_sol = perimeter_prob.solve()
print("optimal perimeter is:" , perimeter_sol)
plot_disks(C.value, R.value, Gindexes, name = "perimeters")

