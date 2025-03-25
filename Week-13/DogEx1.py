class Dog:
    # Construtor
    def __init__ (self, _name="Alice", _weight=100, _rabid=True):
        self.name = _name
        self.weight = _weight
        self.rabid = _rabid

    def eat(self, food):
        self.weight += food

        print(f"{self.name} now weighs {self.weight} lbs.")

    def growl(self):
        print(f"{self.name} says grr.")

def main():
    d1 = Dog("Joy", 100, False)
    d2 = Dog("Fido", 50, True)
    d3 = Dog("Bob", 30, False)
    d4 = Dog()

    print(d1.name)
    print(d2.name)
    print(d3.name)
    print(d4.name)

    print()

    d3.eat(70)


if __name__ == "__main__":
    main()

