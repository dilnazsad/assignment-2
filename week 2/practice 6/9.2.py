import numpy as np

r = np.array([10, 20, 30, 40, 50, 60])
p = np.array([70, 80, 90, 100, 110, 120])

for i in range(3, len(r)):
    p[i], r[i] = r[i], p[i]

print(r, p)
