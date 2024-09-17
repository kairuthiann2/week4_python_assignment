class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introducing(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and i am {self.gender}.")

# Create an instance of the person class
person_instance = Person("Victor", 28, "Male")

# Call the introding method to display the persons information
person_instance.introducing()