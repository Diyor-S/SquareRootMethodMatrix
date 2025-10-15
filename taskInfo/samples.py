"""
Variant number is 18, based on that we get:

NoU - number of unknowns

Matrix A, represents coefficients:
A = [
    [a11, a12, a13, a14, a15],
    [a21, a22, a23, a24, a25],
    [a31, a32, a33, a34, a35],
    [a41, a42, a43, a44, a45],
    [a51, a52, a53, a54, a55],
]

X - the vector we are looking for. Directly related to NoU (the number of unknows) that we should find.
B - column vector, results we obtain based on the x.

    Also solved for the 3x3 in IndependentWork, also gave True

    print_initial_state(A_3, B_3)

    X = calculate_matrix(A_3, B_3)
    print(f"My solution:\n{np.around(X, decimals=16)}")

    X_official = np.linalg.solve(A_3, B_3)
    is_solution_correct = np.allclose(X, X_official)

    print(f"Official Solution:\n{X_official}")
    print(f"Your Solution Matches Official: {is_solution_correct}")


"""