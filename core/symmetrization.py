from numpy.typing import NDArray
import numpy as np


def symmetrize(A: NDArray[np.float64], B: NDArray[np.float64]) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """

    :param A: Matrix A
    :param B: Vector results B matrix
    :return: A_mod = A transposed product to A matrix, A transposed product to B matrix
    """
    A_mod = A.T @ A
    B_mod = A.T @ B
    return A_mod, B_mod
