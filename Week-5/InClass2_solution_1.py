def main():
    # Only 3 attempts
    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")

        
        if username != "admin" or password != "password123":
            if attempt == 2:
                print("Login terminated")
            else:
                print("Invalid Login, try again")
        else:
            print("Login successful")
            break
            
        print()


    
    

if __name__ == "__main__":
    main()