# home work  WAP to create a class named Distance which
# has feet and inches as data member . Overload any two operators

class Distance:
    def __init__(self , feet , inches):
        if inches > 12 :
            quot = inches // 12 
            rem = inches % 12 
            
            self.feet = feet + quot
            self.inches = rem
        else:
            self.feet = feet
            self.inches = inches
    
    def __str__(self):
        return f"{self.feet} ft and {self.inches} inches"
    
    def __repr__(self):
        return f"{self.feet} , {self.inches}"
    
    
    def __add__(self, other):
        new_feet = self.feet + other.feet
        new_inches = self.inches + other.inches
    
    def __mul__(self):
        pass

# 1ft = 12 inches

d1 = Distance(3 , 12)
d2 = Distance(4 , 2)

d3 = d1+d2
d4 = d1*4

print(f"The product is {d4} and sum is {d3}")