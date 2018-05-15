class Math:
    def __init__(self,a,b,c):
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)
    def add(self):
        return self.a+self.b+self.c
    def sub(self):
        return self.a-self.b-self.c
if __name__ == '__main__':
    print(Math.a)