from numpy import *
rad = random.rand(4, 4)
mat = mat(rad)
inv = mat.I 
print(inv * mat)
print(eye(4))