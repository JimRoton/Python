import os

class animal:
    def __init__(self, color: str = "Unkown") -> None:
        self.color = color

    def get_color(self) -> str:
        return self.color
    
    def speak(self):
        return "I can't speak, I'm deaf.\nI only know that one sentance and this sentance explaining it."
    
class dog(animal):
    def __init__(self, color: str) -> None:
        super().__init__(color)        

    def speak(self) -> str:
        return "bark!"

class cat(animal):
    def __init__(self, color: str) -> None:
        super().__init__(color)

    def speak(self):
        return "meow!"

class fish(animal):
    pass

def main():
    d = dog("brown")
    c = cat("orange")
    f = fish()

    print(f"The dog says: {d.speak()}")
    print(f"The dog is: {d.color}")
    
    print(f"The cat says: {c.speak()}")
    print(f"The cat is: {c.color}")

    print(f"The fish says: {f.speak()}")
    print(f"The fish is: {f.color}")

os.system("clear")
main()