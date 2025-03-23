#Hein San, U2421569C, T9 (LA1)
input = int(input("Input n: "))
for i in range(input):
    if i == 0:
        for n in range(input):
            print ("*", end=' ')
    elif i == (input-1):
        print("\n")
        for b in range(input):
            print ("*", end=' ')
    else:
        print("\n")
        for d in range(input):
            if d == 0:
                print ("*", end=' ')
            elif d == (input-1):
                print ("*", end=' ')
            else:
                print (" ", end=" ")
