# Make a class named Drone that meets the following requirements:
#

# Create getter and setter methods for the altitude attribute. Your setter method should return an exception if the passed altitude is negative.
# Has a method named ascend that causes the Drone to ascend to a passed altitude change.
# Has an attribute named ascend_count that stores the number of ascents the Drone has done.
# Has a method named fly that returns the Drone’s current altitude.


# In Python, we use double underscore before the attributes name to make them inaccessible/private or to hide them.
class NegativeAltitude( Exception ):
    pass

class Drone:
    def __init__(self, altitude):
        self.__altitude = altitude #not accessible from outside of class
        self.ascend_count = 0
    # getter method - required to surface hidden attributes to outside
    def get_altitude(self):
        return self.__altitude

    # setter method
    def set_altitude(self, altitude):
        if altitude > 0:
            self.__altitude = altitude
        else:
            raise NegativeAltitude

    def ascend(self, altitude_change):
        self.set_altitude(self.get_altitude() + altitude_change)
        if altitude_change > 0:
            self.ascend_count += 1
        print(self.__altitude)

    def fly(self):
        return f'The done is flying at {self.__altitude} feet.' #method returns a string containing this string

d1 = Drone(100)
print(d1.fly())

d1 = Drone(300)
print(d1.fly())

d1.ascend(100)
print(d1.get_altitude())

print(d1.fly())
# print(d1.altitude)

print(d1.ascend_count)
