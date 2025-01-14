# Write a program that asks the users weight (in pounds) and 
# prints out how much the user would weigh on the moon.

# Note: Your moon weight is 16.5% of your Earth weight
def main():
    earthWeight = int(input("What is your earth weight?(lbs): "))
    conversion = 16.5 / 100
    moonWeight = earthWeight * conversion

    print(moonWeight)
    
	

if __name__ == "__main__":
	main()

