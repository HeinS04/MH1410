#Hein San, U2421569C, T9 (LA1)
input = int(input("Input n: "))
def f(x):
    check = None
    check1 = None
    sum = 0
    if x>0:
        for i in range(x):
            check = i/11
            check1 = i/17
            if check.is_integer() == True:
                sum = sum + i
            elif check1.is_integer() == True:
                sum = sum + i
    return int(sum)
x = f(input)
print(x)
