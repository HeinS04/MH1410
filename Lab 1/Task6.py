#Hein San, U2421569C, T9 (LA1)
class myList(list):
    def power(self, x):
        for i in range(len(self)):
            self[i] = self[i] ** x
B = myList()
for i in range(5):
    B.append(i)

print(B)  
B.power(2)
print(B)  
B.reverse()
print(B) 