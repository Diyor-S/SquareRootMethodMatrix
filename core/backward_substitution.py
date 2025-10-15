from numpy.typing import NDArray
import numpy as np


def backward_substitution(S: NDArray[np.float64], Y: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    S*x=B

    :param S: Matrix S
    :param Y: Matrix Y
    :return:
    """
    rows = S.shape[0]
    columns = S.shape[1]
    X = np.zeros(shape=(rows, 1), dtype=float)
    j = 0

    for i in range(rows - 1, -1, -1):
        sum_of_args_for_X = np.sum(S[i, i+1:columns] * X[i+1:rows, j])

        X[i, j] = (Y[i, j] - sum_of_args_for_X) / S[i, i]

    return X
