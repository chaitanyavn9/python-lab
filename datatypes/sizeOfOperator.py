import sys

a = 10
b = 10.5
c = 20.12345
d = 'A'

print("Size of Different Data Types")
print("----------------------------")

print("Size of int    :", sys.getsizeof(a), "bytes")
print("Size of float  :", sys.getsizeof(b), "bytes")
print("Size of double :", sys.getsizeof(c), "bytes")
print("Size of string :", sys.getsizeof(d), "bytes")