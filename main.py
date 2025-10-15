from global_v import A, B  # A_3, B_3
from utils import print_initial_state, calculate_matrix

import numpy as np


def _main():
    print_initial_state(A, B)

    X = calculate_matrix(A, B)
    print(f"My solution:\n{np.around(X, decimals=16)}")

    X_official = np.linalg.solve(A, B)
    is_solution_correct = np.allclose(X, X_official)

    print(f"Official Solution:\n{X_official}")
    print(f"Your Solution Matches Official: {is_solution_correct}")



