import numpy as np

def matrix_analysis_integer(matrix):
    """
    Analyzes a square matrix and calculates various terms in integer form.

    Args:
        matrix (numpy.ndarray): Input square matrix.

    Returns:
        dict: Dictionary containing S1, S2, S3, characteristic equation, eigenvalues, eigenvectors,
              diagonal matrix, and canonical form.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The input must be a square matrix.")

    n = matrix.shape[0]  # Dimension of the matrix

    # Calculate S1
    S1 = int(matrix[0, 0])

    # Calculate S2
    if n > 1:
        S2 = int(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])
    else:
        S2 = None  # S2 is not defined for 1x1 matrices

    # Calculate S3 (Determinant) and round to nearest integer
    S3 = int(round(np.linalg.det(matrix)))

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    eigenvalues = np.round(eigenvalues).astype(int)
    eigenvectors = np.round(eigenvectors).astype(int)

    # Construct the characteristic equation
    coeffs = np.poly(matrix).round().astype(int)  # Coefficients of the polynomial
    ch_eq_terms = [f"{coeff}*lambda^{n - i}" if n - i > 0 else f"{coeff}" 
                   for i, coeff in enumerate(coeffs) if coeff != 0]
    ch_eq = " + ".join(ch_eq_terms).replace("*lambda^1", "*lambda").replace("*lambda^0", "")

    # Diagonalized matrix (eigenvalues)
    diag_matrix = np.diag(eigenvalues)

    # Canonical form (A = PDP^-1) with integer rounding
    canonical_form = np.round(eigenvectors @ diag_matrix @ np.linalg.inv(eigenvectors)).astype(int)

    # Create result dictionary
    result = {
        "S1": S1,
        "S2": S2,
        "S3 (Determinant)": S3,
        "Characteristic Equation": ch_eq,
        "Eigenvalues": eigenvalues.tolist(),
        "Eigenvectors": eigenvectors.tolist(),
        "Diagonalized Matrix": diag_matrix.astype(int).tolist(),
        "Canonical Form (Reconstructed Matrix)": canonical_form.tolist()
    }
    return result

# Example usage
A = np.array([[6, -2, 2],
              [-2, 3, -1],
              [2, -1, 3]])  # Example 3x3 matrix

results = matrix_analysis_integer(A)

# Display results
for key, value in results.items():
    print(f"{key}:")
    print(value, "\n")
