from core import (
    symmetrize,
    cheolesky_factorization,
    forward_substitution,
    backward_substitution,
)
from utils.symmetry_check import is_symmetric, is_positive_definite


def _calculation_handler(func):
    def wrapper(A, B):
        if not is_symmetric(A) and not is_positive_definite(A):
            symmetrized_A, mod_B = symmetrize(A, B)
        else:
            symmetrized_A, mod_B = A, B

        return func(symmetrized_A, mod_B)

    return wrapper


@_calculation_handler
def calculate_matrix(symmetrized_A, mod_B):
    S = cheolesky_factorization(symmetrized_A)
    Y = forward_substitution(S, mod_B)
    X = backward_substitution(S, Y)
    return X
