# Square Root Method Solver (Cholesky Decomposition)

## 1. Task Overview

This program is an implementation of the **Square Root Method** (also called the Cholesky method)
to solve a system of $n=5$ Linear Algebraic Equations (SLAE).

* **Task Source:** Independent Work №1.
* **Variant Number:** V = 18.
* **Goal:** To find the solution vector $X$, the determinant of $A$, and the symmetrized matrix $\overline{A}$ for the given $5 \times 5$ system.
* **Language/Libraries:** Python with NumPy.

---

## 2. Theoretical Basis

### Method Conditions and Symmetrization

The Square Root Method is an exact method designed for solving symmetric, positive definite systems.

The coefficient matrix $A$ for the given $5 \times 5$ problem (with $V=18$) is **non-symmetric**, meaning it does not meet the necessary conditions for direct application[cite: 15]. [cite_start]Therefore, the program first applies **System Symmetrization**[cite: 41]:

The original system $AX=B$ is transformed into the modified system $\overline{A}X = \overline{B}$ by multiplying by the transpose $A^T$:
$$\overline{A} = A^{T}A, \quad \overline{B} = A^{T}B \text{}$$
The resulting matrix $\overline{A}$ is guaranteed to be symmetric and positive definite, allowing the Square Root Method to be applied.

### Algorithm Flow
The algorithm solves the resulting system $\overline{A}X = \overline{B}$ by decomposing $\overline{A} = S^T S$, where $S$ is an upper triangular matrix[cite: 19, 21]:
1.  **Factorization:** Find the elements of $S$ using the recursive formulas derived from $S^T S = \overline{A}$.
2.  **Forward Substitution:** Solve the system $S^T Y = \overline{B}$ for the intermediate vector $Y$].
3.  **Backward Substitution:** Solve the system $SX = Y$ for the final solution vector $X$.

---

## 3. System Solved (V=18)

The program uses the following matrices derived from the formulas in the assignment document:

### A. Symbolic System
The program starts with the symbolic $5 \times 5$ system:

$$
\begin{cases}
(V+1)x_1+ (V+2)x_2 - Vx_3 + 4Vx_4 - Vx_5 = 4V^2 + 6V + 4 \\
(V+4)x_1 - 2Vx_2 + 3Vx_3 - Vx_4 + 4Vx_5 = 5V^2 + 24V + 16 \\
(V+2)x_1 + (V+4)x_2 - (V+1)x_3 + (V+1)x_4 - (V+3)x_5 = V^2 + 3V \\
(V+3)x_1 + (V+5)x_2 - (V+1)x_3 + (V+2)x_4 - (V+4)x_5 = V^2 + 5V + 3 \\
Vx_1 + (V+1)x_2 + (V+2)x_3 + (V+3)x_4 + (V+4)x_5 = 5V^2 + 20V + 17
\end{cases}
$$

### B. Input Matrices (V=18)

**Coefficient Matrix A:**
$$
A = \begin{pmatrix}
19 & 20 & -18 & 72 & -18 \\
22 & -36 & 54 & -18 & 72 \\
20 & 22 & -19 & 19 & -21 \\
21 & 23 & -19 & 20 & -22 \\
18 & 19 & 20 & 21 & 22
\end{pmatrix}
$$

**Free Term Vector B:**
$$
B = \begin{pmatrix}
1408 \\
2068 \\
378 \\
417 \\
1997
\end{pmatrix}
$$

---

## 4. Program Output Requirements

The program generates the following results:

1.  **Symmetrized Matrix A** ($\overline{A} = A^T A$)
2.  **Determinant of A** ($\det(A)$)
3.  **Solution Vector X** ($X$)
