# Declare a python class called Elevator
# It should variables for current_floor (an integer), destination_floor (an integer), 
# current_weight (a number)

# It should have a constructor which defaults current_floor, 
# and destination_floor to 1, and current_weight to 0.

# It should have a function called move which takes a new destination.  

# Assuming the destination is between 1 and 20, it should print out all 
# the floors from where it is, to where it’s going.  If it’s not a valid floor tell them.

# Create 2 elevators, send one to floor 5, and the other to floor 10

class Elevator:
    def __init__ (self, current_floor = 0, destination_floor = 1, current_weight = 0):
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.current_weight = current_weight
    
    def move(self, destination):
        if 1 <= destination <= 20:
            self.destination_floor = destination

            if self.current_floor > self.destination_floor:
                for x in range(self.current_floor - self.destination_floor):
                    self.current_floor -= 1
                    print(f"Floor #{self.current_floor}")
            elif self.current_floor < self.destination_floor:
                for x in range(self.destination_floor - self.current_floor):
                    self.current_floor += 1
                    print(f"Floor #{self.current_floor}")
        else:
            print("Destination is not valid")

def main():
    elevator_obj = Elevator(1, 0)

    elevator_obj.move(5)
    elevator_obj.move(3)


if __name__ == "__main__":
    main()