try: #need to define a else error
    print(a)
except:
    print("a isnt defined")

try:
    print(a)
except NameError: #using specific errors
    print("a not defined nameError")
except:
    print("Not a name error")


#breaks program
print(a)