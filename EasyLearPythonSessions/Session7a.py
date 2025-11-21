class pet:

    def __init__(self, name: str, breed :str):
        self.name = name
        self.breed = breed
        # self.person = person

    def bark(self):
        print(f"pets name is {self.name} and its breed is {self.breed}")

    def greet(self, person):
        print(f"{self.name} greets {person} with a wag of tail")


vijay_pet = pet(name="snoopy",breed="labrador")


vijay_pet.bark()
vijay_pet.greet("vijay")

# poorna_pet = pet()

# poorna_pet.bark("tiger","german sheperd")
# poorna_pet.greet("tiger","poorna")