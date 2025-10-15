from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from numpy.typing import NDArray
    import numpy as np


def calculate_determinant_of_symmetrized_A(S: "NDArray[np.float64]") -> "NDArray[np.float64]":
    rows = S.shape[0]
    det_S = 1
    for i in range(rows):
        det_S *= S[i, i]

    det_A = det_S**2

    return det_A

