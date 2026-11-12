
import numpy as np

# Read two matrices from user
n = int(input("Enter matrix size: "))

print("Enter first matrix:")
A = np.array([list(map(float, input().split())) for i in range(n)])

print("Enter second matrix:")
B = np.array([list(map(float, input().split())) for i in range(n)])

# 1. Dot Product
print("Dot Product:")
print(np.dot(A, B))

# 2. Transpose
print("Transpose of first matrix:")
print(A.T)

print("Transpose of second matrix:")
print(B.T)

# 3. Trace
print("Trace of first matrix:", np.trace(A))
print("Trace of second matrix:", np.trace(B))

# 4. Rank
print("Rank of first matrix:", np.linalg.matrix_rank(A))
print("Rank of second matrix:", np.linalg.matrix_rank(B))

# 5. Determinant
print("Determinant of first matrix:", np.linalg.det(A))
print("Determinant of second matrix:", np.linalg.det(B))

# 6. Inverse
print("Inverse of first matrix:")
if np.linalg.det(A) != 0:
    print(np.linalg.inv(A))
else:
    print("Inverse does not exist")

print("Inverse of second matrix:")
if np.linalg.det(B) != 0:
    print(np.linalg.inv(B))
else:
    print("Inverse does not exist")

# 7. Eigenvalues and Eigenvectors
print("Eigenvalues of first matrix:")
print(np.linalg.eig(A)[0])

print("Eigenvectors of first matrix:")
print(np.linalg.eig(A)[1])

print("Eigenvalues of second matrix:")
print(np.linalg.eig(B)[0])

print("Eigenvectors of second matrix:")
print(np.linalg.eig(B)[1])
