import numpy as np

def main():
    i =0
    n = 10
    x = 119.0


    y = np.zeros(n, dtype = float) #creates an array filled with zeros with float datatype

    for i in range(n):
        y[i] = 2 * float(i) + 1 #2 * index + 1 values

    for y_element in y:
        print(y_element) #prints out array

if __name__ == "__main__":
    main()
