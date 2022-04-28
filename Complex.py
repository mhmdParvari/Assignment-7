class Complex:
    def __init__(self,real_part,imaginary_part):
        self.real=real_part
        self.image=imaginary_part

    def show(self):
        if self.real!=0:
            print(self.real,end='')
        if self.image!=0:
            if self.image>0 and self.real!=0: print('+',end='')
            print(self.image,end='')
            print('i',end='')
        if self.real==0 and self.image==0: print(self.real,end='')
        print('\n',end='')

    def __add__(self,comp2):
        return Complex(self.real+comp2.real,self.image+comp2.image)

    def __sub__(self,comp2):
        return Complex(self.real-comp2.real,self.image-comp2.image)

    def __mul__(self,comp2):
        return Complex(self.real*comp2.real-self.image*comp2.image,self.real*comp2.image+self.image*comp2.real)

#Sample:
a=Complex(2,1)
b=Complex(3,6)
(a*b).show()
Complex(2,0).show()
        
