class Person:
    def __init__(self, first_name, middle_name, second_name):
        self.first_name = first_name
        self.middle_name = first_name
        self.second_name = second_name


p1 = Person("Cher", "Lloyd")
print(p1.first_name + p1.middle_name + p1.second_name)
