from core import (
    symmetrize,
    cheolesky_factorization,
    forward_substitution,
    backward_substitution,
    calculate_determinant_of_symmetrized_A,
)
from utils.symmetry_check import is_symmetric, is_positive_definite


def _calculation_handler(func):
    def wrapper(A, B):
        if not is_symmetric(A) and not is_positive_definite(A):
            symmetrized_A, mod_B = symmetrize(A, B)
        else:
            symmetrized_A, mod_B = A, B

        return func(symmetrized_A, mod_B), symmetrized_A

    return wrapper


@_calculation_handler
def calculate_matrix(A, B):
    S = cheolesky_factorization(A)
    det_A = calculate_determinant_of_symmetrized_A(S)
    Y = forward_substitution(S, B)
    X = backward_substitution(S, Y)
    return X, det_A
