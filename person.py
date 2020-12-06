class Person:
    # Instance Variables
    hair_color = ""
    eye_color = ""
    body_type = ""

    # Constructor --> assigns instance variables
    def __init__(self, hair_color, eye_color, body_type):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.body_type = body_type

    def walk(self):
        print("walking")

    def run(self):
        print("running")

    def talk(self):
        print(f"My hair color is {self.hair_color}!")