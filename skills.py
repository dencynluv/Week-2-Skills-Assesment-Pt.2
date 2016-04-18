# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

1. Encapsulation
2. Abstraction
3. Polymorphism

# Explain each concept.

Encapsulation - Keeps everything together and organized under each class. 
Abstraction - Hides information and details you dont need.
Polymorphism - Has multiple forms, an interchangebility of components.

# 1. What is a class?

A class is a template for instantiating instances (creating objects). 
Within a class you can define attributes and methods. 

# 2. What is an instance attribute?

An instance attribute is a characteristic/property/data of that particular instance. 

# 3. What is a method?

A method is like a function that allows you to create a behavior for your instance
wihtin its class. It runs when you call it with an instance. 

# 4. What is an instance in object orientation?

An instance is an individual object. A particular string or file.

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.

A class attribute is a characteristic/data owned by the class itself. 
An instance attribute is directly owned by the instance.

If I wanted to instanciate multiple instances with the same base attributes I would use class attributes.
Because when an instance is instanciated any class attributes that are set are automatically 
part of that instance. 

If I wanted to give more individuality to the instances instanciated I would use instance attributes.
This would allow me to add different attributes without having to add them to my class directly and 
it would not change any of the other instances. 

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes"""

        self.f_name = first_name
        self.l_name = last_name
        self.address = address
        # self.info()

    # def info(self):
    #     print self.f_name, self.l_name, self.address


class Question(Student):

    self.question = question
    self.correct_answer = correct_answer


class Exam(Student):

    def __init__(exam_type, questions):
        self.exam_type = exam_type



























