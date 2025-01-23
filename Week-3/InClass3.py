def main():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "password123":
        print("Success")
    else:
        if username != "admin":
            print("Wrong username")
        elif password != "password123":
            print("Wrong password")

if __name__ == "__main__":
    main()