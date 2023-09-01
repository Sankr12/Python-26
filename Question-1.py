# Write a python script to multiple 2, 3 or 4 numbers with a single multiply method in class using method overloading

class multiply:
    def multiple(self,a,b=1,c=1,d=1):   # Method Overloading 
        return a*b*c*d



c1 = multiply()

print(c1.multiple(2,3,4,5))