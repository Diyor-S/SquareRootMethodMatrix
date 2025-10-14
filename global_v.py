import numpy as np
from numpy.typing import NDArray

NoU: int = 5

A: NDArray[np.float64] = np.array([
    [19, 20, -18, 72, -18],
    [22, -36, 54, -18, 72],
    [20, 22, -19, 19, -21],
    [21, 23, -19, 20, -22],
    [18, 19, 20, 21, 22]
], dtype=float)

B: NDArray[np.float64] = np.array([
    [1408],
    [2068],
    [378],
    [417],
    [1997]
])
