# Topics
#   - Other Data Structures: List review, Dictionaries, Tuples, Combining them
#   - OOP: We've already been using objects, Creating our own class, adding a constructor (with __init__(self, params)),
#          different files, maybe touch on inheritance

names = ["joe", "bob", "melinda"]

names.append("sarah")

print(names[2 + 1])

peoples_ages = {"joe": 14, "bob": 4, "melinda": 40, "sarah": 100}

print(peoples_ages["melinda"])

for key in peoples_ages:
    print(f"key: {key}, age: {peoples_ages[key]}")

# Immutable, so use for things that do not change
hair_colors = ("brown", "black", "pink", "green")

family = {
            "Smith": {
                "emily": {
                    "basic_info": ("woman", "likes pizza"),
                    "kid_names": ["michael", "joe"]
                }
            },
            "Wang": {
                "sarah": "cool"
            }
        }
# How do we access emily's first kid's name?
print(family["Smith"]["emily"]["kid_names"][0])

print("=============================")

from person import Person


class Athlete(Person):
    speed = 0

    def __init__(self, speed, hair_color, eye_color, body_type):
        self.speed = speed
        super().__init__(hair_color, eye_color, body_type)

    def run(self, distance):
        print(f"I am {self.body_type} and have {self.speed} speed for {distance} meters!")


joe = Person("brown", "blue", "thin")
joe.talk()

sarah = Person("black", "green", "chubby")
sarah.run()
print(sarah.eye_color)

michael = Athlete(10, "brown", "blue", "thin")
michael.run(400)
michael.walk()
