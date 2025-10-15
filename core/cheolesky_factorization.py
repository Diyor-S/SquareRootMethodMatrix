from numpy.typing import NDArray
import numpy as np


def cheolesky_factorization(A_mod: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    :param A_mod: Matrix A
    :return: New, easier to solve matrix S, such that S * S.T = A
    """

    rows = A_mod.shape[0]
    columns = A_mod.shape[1]
    S = np.zeros((rows, rows), dtype=float)

    # Formula: s_ii = sqrt(a_ii - sum_{k=0}^{i-1} s_ki^2)

    for i in range(rows):
        sum_of_args_for_i_i = np.sum(S[:i, i]**2)
        is_sqrt_allowed = A_mod[i, i] - sum_of_args_for_i_i

        if is_sqrt_allowed < 0:
            raise ValueError("Not positive definite")
        S[i, i] = np.sqrt(is_sqrt_allowed)

        for j in range(i + 1, columns):
            sum_of_args_for_i_j = np.sum(S[:i, i]*S[:i, j])
            S[i, j] = (A_mod[i, j] - sum_of_args_for_i_j) / S[i, i]

    return S
