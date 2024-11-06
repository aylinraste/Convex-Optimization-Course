from cvxpy import *

x = Variable()
y = Variable()

constraints = [x >= 0, y >= 0]

obj = Minimize(square(inv_pos(geo_mean(hstack([x, y])))))

prob = Problem(obj, constraints)
print(prob.is_dcp())
sol = prob.solve()
print(sol)
