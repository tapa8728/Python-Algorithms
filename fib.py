# Matrix Multiplication  -  Tanvi Parikh

def matmult(A,B):
  # multiplies 2x2 matrix
  def val(i,j):
    return A[i][0]*B[0][j] + A[i][1]*B[1][j]
  return (
    (val(0,0), val(0,1)),
    (val(1,0), val(1,1)),
  )

def matrix_power(A,n):
  if n == 0:
    return ( (1, 0), (0,1) )
  if n%2 == 1:
    return matmult(A, matrix_power(A,n-1))
  else:
      root = matrix_power(A,n/2)
      return matmult(root,root)

def fibo_matrix(n):
  M = ( (0, 1), (1,1) )
  return matrix_power(M,n)[0][1]

n = input("Enter a number ")
x = fibo_matrix(n)
print x

