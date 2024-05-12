import random

class Clue:
    def __init__(self):
        self.characters = ["Miss Scarlet", "Colonel Mustard", "Mrs. White", "Mr. Green"]
        self.weapons = ["Candlestick", "Knife", "Lead Pipe", "Revolver"]
        self.locations = ["Kitchen", "Ballroom", "Conservatory", "Dining Room"]
        self.solution = {
            "character": random.choice(self.characters),
            "weapon": random.choice(self.weapons),
            "location": random.choice(self.locations)
        }

    def play(self):
        print("¡Bienvenido a Clue!")
        print("Te encuentras en una noche oscura y tormentosa en la Mansión Blackwood.")
        print("Un grito desgarrador rompe el silencio, seguido por el sonido de pasos que se alejan.")
        print("Corres hacia la habitación donde se escuchó el grito y encuentras el cuerpo sin vida de Mr. Blackwood.")
        print("Los sospechosos son: Miss Scarlet, Colonel Mustard, Mrs. White, Mr. Green")
        print("Las armas posibles son: Candlestick, Knife, Lead Pipe, Revolver")
        print("Los lugares posibles son: Kitchen, Ballroom, Conservatory, Dining Room")
        print("¡Puedes hacer preguntas para deducir quién es el asesino, con qué arma y en qué lugar!\n")

        while True:
            suspect = input("¿Pregúntale al investigador privado quién es el asesino?: ")
            weapon = input("¿Pregúntale al investigador privado qué arma se utilizó para cometer el crimen?: ")
            location = input("¿Pregúntale al investigador privado en qué parte de la mansión ocurrió el asesinato?: ")

            if suspect in self.characters and weapon in self.weapons and location in self.locations:
                if suspect == self.solution["character"] and weapon == self.solution["weapon"] and location == self.solution["location"]:
                    print("\n¡Felicidades! Has resuelto el misterio y atrapado al asesino.")
                    print("La solución era:")
                    print(f"Sospechoso: {self.solution['character']}")
                    print(f"Arma: {self.solution['weapon']}")
                    print(f"Lugar: {self.solution['location']}")
                    print("\nLa justicia ha sido servida en la Mansión Blackwood.")
                    break
                else:
                    print("\nEsa no es la respuesta correcta. Sigue investigando...\n")
            else:
                print("\nAlgo no está bien con las preguntas. Asegúrate de usar las opciones correctas.\n")

if __name__ == "__main__":
    game = Clue()
    game.play()
