#strings

s = "DASdasfas"
print(type(s))


#booleans
yes = True
print(type(yes))

no = False
print(type(no))

alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d") #adds a d to the end of the array
print(alpha_list)

#tples, ordered pairs

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
    alpha_tuple[2] = "d" #bad code
except TypeError:
    print("No adding elements to tuples")
print(alpha_tuple)