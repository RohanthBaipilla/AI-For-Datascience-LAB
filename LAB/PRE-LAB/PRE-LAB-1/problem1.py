import numpy as np

cost = np.array([[19, 30, 50, 10], [70, 30, 40, 60], [40, 8, 70, 20]])
supply = np.array([7, 9, 18])
demand = np.array([5, 8, 7, 4])

def row_minima(cost_matrix):
    allocation = np.zeros_like(cost_matrix)
    for i in range(allocation.shape[0]):
        j = np.argmin(cost_matrix[i])
        allocation[i][j] = supply[i] if supply[i] < demand[j] else demand[j]
        demand[j] -= allocation[i][j]
        supply[i] -= allocation[i][j]
    return allocation

allocation = row_minima(cost)
# print(allocation)