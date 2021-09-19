# naming convention is pascal, capitolize first letter of class name to do it correctly
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point()
point.x = 10
point.y = 20
print(point.x)
point.draw()

# example of an error.
# completely different objects. Will error.
# point2 = Point()
# print(point2.x)

# solve this problem above by using a constructer
class Point2:
    # function or object thats called once a new Point is initilized
    def __init__(self, x, y):
        # self is the refrence to the current object in memory. 
        self.x = x
        self.y = y

# so 
point3 = Point2(10, 20)
print(point.x)

# note, self should be parameter of every thing
class Person:
    def __init__(self, personname):
        self.personname = personname
    def name(self):
        print(self.personname)
    def talk(self):
        print(f"{self.personname}: Hi!")

person = Person("John")
person.name()
person.talk()

# inheritence
class SomeClass:
    def walk(self):
        print("walk")

class OtherClass(SomeClass):
    pass # needed so it compiles

something = OtherClass()
something.walk()
# helps us to stop repeating ourselves within classes. Iz gud