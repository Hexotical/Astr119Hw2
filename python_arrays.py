x = [0.0, 3.0, 5.0, 2.5, 3.7] #woo arrays
print(type(x))

#remove element 3
x.pop(2)
print(x)

#remove element equal to 2.5
x.remove(2.5)
print(x)

#add an alement to end, appending
x.append(1.2)
print(x)

#copy
y = x.copy()
print(y)

#how many elements are 0
print(y.count(0.0))

#print index of value 3.7
print(y.index(3.7))

#sort
y.sort()
print(y)

#reverse list
y.reverse()
print(y)

#clear an array
y.clear()
print(y)