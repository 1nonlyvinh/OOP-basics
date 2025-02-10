import random 

class Character: 
    #class atributes
    hair_color = ["Blonde", "Brown", "Ginger", "Black"]
    sizes = ["Tiny", "Medium", "Large"]
    height = ["Short", "Average", "Tall"]
    dominant_hand = ["Right", "Left"]

    #Constructor

    def __init__(self): 
        self.generate_character()

#This is a method (function)
    def generate_character(): 
        self.hair_color = random.choice(Character.hair_color) 
        self.sizes = random.choice(Character.sizes)
        self.height = random.choice(Character.height)
        self.dominant_hand = random.choice(Character.dominant_hand)
        self.description = (
            f"Your Character has {self.hair_color} hair, "
            f"is {self.sizes} in size, and height is, "
            f"is {self.height}, and has a dominant hand of, "
            f"{self.dominant_hand}."
        )
    def __str__(self):
        return self.description

char1 = Character()
char2 = Character()

print(char1)
print(char2)