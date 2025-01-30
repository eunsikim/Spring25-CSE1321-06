import random

def main():
    options = ['rock', 'paper', 'scissors']
    # Computer Choice
    cc = random.choice(options)

    # User Choice
    uc = input("Enter Rock, Paper, or Scissors: ").lower()
    
    # User Choice Validation
    if uc == "rock" or uc == "paper" or uc == "scissors":
        print(f"The computer chose: {cc}")
        if cc == uc:
            print("Its a tie!")
        elif uc == "rock":
            # win
            if cc == "scissors":
                print("You won!")
            # lose
            else:
                print("You lose!")
        elif uc == "paper":
            # win
            if cc == "rock":
                print("You won!")
            # lose
            else:
                print("You lose!")
        elif uc == "scissors":
            # win
            if cc == "paper":
                print("You won!")
            # lose
            else:
                print("You lose!")
    else:
        print("Invalid Option")
    

if __name__ == "__main__":
    main()