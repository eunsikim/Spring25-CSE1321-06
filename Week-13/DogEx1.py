class Dog:
    idCount = 1

    # Construtor
    def __init__ (self, _name="Alice", _weight=100, _rabid=True):
        self.name = _name
        self.weight = _weight
        self.rabid = _rabid
        self.id = Dog.idCount
        Dog.idCount += 1

    def eat(self, food):
        self.weight += food

        print(f"{self.name} now weighs {self.weight} lbs.")

    def growl(self):
        print(f"{self.name} says grr.")

def main():
    d1 = Dog("Joy", 100, False)
    print(f"d1.id = {d1.id}\tDog.idCount = {d1.idCount}")
    d2 = Dog("Fido", 50, True)
    print(f"d2.id = {d2.id}\tDog.idCount = {d2.idCount}")
    d3 = Dog("Bob", 30, False)
    print(f"d3.id = {d3.id}\tDog.idCount = {d3.idCount}")
    d4 = Dog()
    print(f"d4.id = {d4.id}\tDog.idCount = {d4.idCount}")

    # print()

    # d3.eat(70)


if __name__ == "__main__":
    main()

