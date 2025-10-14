import numpy as np
from numpy.typing import NDArray


def is_symmetric(A: NDArray[np.float64]) -> bool:
    return np.allclose(A, A.T)


def is_positive_definite(A: NDArray[np.float64]) -> bool:
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False
