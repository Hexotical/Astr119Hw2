import numpy as np

i = 10
print(type(i)) #prints data type of i, should be an int

a_i = np.zeros(i, dtype = int) #make an array of ints
print(type(a_i))
print(type(a_i[0]))

x = 110.02

print(type(x))

y = 1.19e2
print(type(y))

z = np.zeros(i,dtype = float) #float array
print(type(z)) #returns a nd array
print(type(z[0])) #returns a floiat