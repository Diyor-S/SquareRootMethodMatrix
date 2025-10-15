from numpy.typing import NDArray
import numpy as np

np.set_printoptions(precision=8, suppress=False, linewidth=150)


def print_initial_state(A: NDArray[np.float64], B: NDArray[np.float64]) -> None:
    print("Square Root Method or Cheolesky Decomposition:")
    print("For the given Matrix A:")
    print(np.around(A, decimals=4))
    print("\nFor the given Matrix B:")
    print(np.around(B, decimals=4))
