#Hein San, U2421569C, T9 (LA1)
class triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.valid = None
        self.peri = None
    def is_valid(self):
        list = [self.a,self.b,self.c]
        maxval = max(list)
        sum = 0
        for i in range(len(list)):
            if maxval != list[i]:
                sum = sum + list[i]
        if maxval >= sum:
            self.valid = False
        else:
            self.valid = True
    def computeperi(self):
        if self.valid == True:
            self.peri = self.a + self.b + self.c
    def printtriangle(self):
        print(self.a,self.b,self.c,self.valid,self.peri)
triA = triangle(2.1,3.4,5.2)
triA.is_valid()
triA.computeperi()
triA.printtriangle()
trib = triangle(2,3,5)
trib.is_valid()
trib.computeperi()
trib.printtriangle()