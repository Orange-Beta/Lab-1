import random

class Character:
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = 10 + constitution

    def display_stats(self):
        print(f"Character: {self.name}")
        print(f"STR: {self.strength}")
        print(f"DEX: {self.dexterity}")
        print(f"CON: {self.constitution}")
        print(f"INT: {self.intelligence}")
        print(f"WIS: {self.wisdom}")
        print(f"CHA: {self.charisma}")
        print(f"HP: {self.hp}\n")

def roll_dice(sides, rolls=1):
    """Function to roll a dice with specified sides and number of rolls."""
    return [random.randint(1, sides) for _ in range(rolls)]

def create_character():
    """Create a new D&D character with random stats."""
    print("Creating a new character...")
    name = input("Enter character name: ")
    stats = [sum(sorted(roll_dice(6, 4))[1:]) for _ in range(6)]  # Roll 4d6 and drop the lowest
    return Character(name, *stats)

def main():
    print("Welcome to D&D Helper!")
    print("1. Roll a Dice")
    print("2. Create a Character")
    print("3. Quit")

    characters = []

    while True:
        choice = input("Choose an option: ")

        if choice == '1':
            sides = int(input("Enter the number of sides on the dice: "))
            rolls = int(input("Enter the number of rolls: "))
            results = roll_dice(sides, rolls)
            print(f"Results: {results}")

        elif choice == '2':
            character = create_character()
            characters.append(character)
            character.display_stats()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
