import numpy as np

def similarity_transform_3x3(A):
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Create the diagonal matrix of eigenvalues
    D = np.diag(eigenvalues)

    # Create the matrix of eigenvectors
    P = eigenvectors

    # Round the results to the nearest integer
    P = np.round(P).astype(int)
    D = np.round(D).astype(int)

    return P, D

# Example usage
A = np.array([[6, -6, 5], [14, -13, 10], [7, -6, 4]])
P, D = similarity_transform_3x3(A)

print("Matrix P:")
print(P)
print("Diagonal matrix D:")
print(D)