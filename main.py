from global_v import A, B  # A_3, B_3
from utils import print_initial_state, calculate_matrix

import numpy as np


def _main():
    print_initial_state(A, B)

    (X, det_A), symmetrized_A = calculate_matrix(A, B)
    print("\n\nMy solution: \n")
    print(f"Symmetrized Matrix A:\n{np.around(symmetrized_A, decimals=16)}")
    print(f"Determinant of Symmetrized A:\n{np.around(det_A, decimals=16)}")
    print(f"Final Result X:\n{np.around(X, decimals=16)}")

    X_official = np.linalg.solve(A, B)
    det_A_official = np.linalg.det(symmetrized_A)
    det_A_official_orig = np.linalg.det(A)
    is_solution_correct = np.allclose(X, X_official)

    print("\n\nOfficial solution:")
    print(f"Determinant of symmetrized A:\n{det_A_official}")
    print(f"Determinant of original Matrix A:\n{det_A_official_orig}")
    print(f"Solution for X:\n{X_official}")
    print(f"\tDoes Solution Match Official: {is_solution_correct}")



