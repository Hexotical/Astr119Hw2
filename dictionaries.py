example_dict = {
    "class"         : "astr119",
    "prof"          : "Brant",
    "awesomeness"   : 10,
    "TA's"          : "Yao Tang, Ricardo Yarza"
}

print(type(example_dict))

#keys lead to values, get the corresponding value of a key

course = example_dict["class"]
print(course)

#change a value to spinal tap
example_dict["awesomeness"] += 1 #turn it up to 11

print(example_dict)

#print dictionary by element
for x in example_dict.keys():
    print(x, example_dict[x])