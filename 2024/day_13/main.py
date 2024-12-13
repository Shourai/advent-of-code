import re
import numpy as np

with open("./input", "r") as f:
    data = f.read()
    data = re.findall(r"\d+", data)
    data = list(map(int, data))

# [[94,22], [34,67]] * [x, y] = [8400, 5400]

tokens = 0
for i in range(0, len(data), 6):
    a, b, c, d, x, y = data[i : i + 6]
    A = np.array([[a, c], [b, d]])
    B = np.array([x + 10000000000000, y + 10000000000000])
    S = np.linalg.solve(A, B).round()
    if all(np.matmul(A, S) == B):
        tokens += S[0] * 3 + S[1]

print(tokens)
