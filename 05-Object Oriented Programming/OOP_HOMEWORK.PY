#OBJECT ORIENTED PROGRAMMING HOMEWORK


#PROBLEM 1
#Fill the line class methods to accept coordinates as pair
#of tuples and return the slope and distance fo the line. 

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)   

print(li.distance())

print(li.slope())
print('\n'*3)


#PROBLEM 2
#FILL THE CLASS

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        #formula for volume 3.14*(radius**2)*height
        # return 3.14({self.radius}**2)*(height)
        return self.height*3.14*(self.radius)**2
    def surface_area(self):
        #surface area formula 2(3.14)(r)(h) + 2(3.14)(r**2)
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)


# EXAMPLE OUTPUT
c = Cylinder(4,5)

print(c.volume())
print(c.surface_area())
