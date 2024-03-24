# Create students that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average...
class Students:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.average = (marks1 + marks2 + marks3 / 3)


s1 = Students("Sayantan Golder", 100, 100, 100)
s2 = Students("Haranath Saha", 99, 99, 99)
s3 = Students("Sayan Das", 98, 98, 98)

print("The average marks of", s1.name, "is: ", s1.average)
print("The average marks of", s2.name, "is: ", s2.average)
print("The average marks of", s3.name, "is: ", s3.average)

                    # OR

class students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
            return sum/3


s1 = students("Sayantan Golder", [100, 100, 100])
s2 = students("Haranath Saha", [99, 99, 99])
s3 = students("Sayan Das", [98, 98, 98])

print("The average marks of", s1.name, "is: ", s1.get_average())
print("The average marks of", s2.name, "is: ", s2.get_average())
print("The average marks of", s3.name, "is: ", s3.get_average())
