def main():

    i = 0
    x = 119.0

    for i in range(120):
        if((i%2) == 0):
            x += 3 #adds 3 if remainder 0
        else:
            x -= 5 #subtracts 5 otherwise

    s = "%3.2e" % x #formatting string for 2 decimal places after in sci not

    print(s) #prints the value of x


if __name__ == "__main__":
    main()
