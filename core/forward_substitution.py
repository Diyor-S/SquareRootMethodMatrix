from numpy.typing import NDArray
import numpy as np


def forward_substitution(S: NDArray[np.float64], B: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    S.T*Y=B

    :param S: Matrix S
    :param B: Matrix B, vector results of the equation
    :return: Matrix Y, intermediate vector to find final X
    """
    S_T = S.T
    rows = S_T.shape[0]
    Y = np.zeros(shape=(rows, 1), dtype=float)
    j = 0

    for i in range(rows):
        sum_of_args_for_Y = np.sum(S_T[i, :i] * Y[:i, j])

        Y[i, j] = (B[i, j] - sum_of_args_for_Y) / S_T[i, i]

    return Y
