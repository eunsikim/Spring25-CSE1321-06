def main():
    username = input("Username: ")
    password = input("Password: ")

    while username != "admin" or password != "password123":
        print("Invalid Login\n")

        username = input("Username: ")
        password = input("Password: ")

    print("Login successful")
    

if __name__ == "__main__":
    main()