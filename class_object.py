#class name person for creating object
class person: 
    def __init__(self, name, age, gender): # Attributes for object {name, age, gender} 
        self.name = name 
        self.age = age
        self.gender = gender

# Method or Behaviour for object
    def walk(self):   
        print(f'{self.name} is walking')
    

    def talk(self):  
        print(f'{self.name} is talking')


p1 = person('AHMED', 25, 'MALE')  # creating object name p1 and assiging attributes
p2 = person('KAZIM', 26, 'MALE')


#creating child class name student fron parent class name person for inheritance.
class student(person):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender) # Inherit properties from parent class.
        self.grade = grade

    def display(self):
        print(f'{self.name} is student')
        print(f'{self.name} is {self.age} years old with {self.grade} grade in class.')

std1 = student('Ali', 22, 'Male', 'B')

std1.display()