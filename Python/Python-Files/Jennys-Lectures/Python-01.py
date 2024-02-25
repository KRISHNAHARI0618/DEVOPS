# Syntax Error
from sympy import Matrix

X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8,7],[6,5,4],[3,2,1]]

matrix_x = Matrix(X)
matrix_y = Matrix(Y)

result = matrix_x + matrix_y

print(result)

result = [map(sum,zip(*t)) for t in zip(X,Y)]
print(result)

for i in range(len(X[0])):
  print(i)

for i in X[1]:
  print(i)