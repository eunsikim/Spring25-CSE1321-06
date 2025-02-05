def main():
    # For this approach, we will use a
    # flag variable which will determine
    # whether to either if the loop should 
    # terminate or keep iterating.

    # The initial value of this flag will be
    # `False` as in "we have not yet 
    # authenticated the user"
    auth = False

    # While `auth` is false we keep looping
    while not auth:
        username = input("Username: ")
        password = input("Password: ")

        if username != "admin" or password != "password123":
            print("Invalid Login")
        else:
            # If the user has been successfully
            # authenticated, we set this flag 
            # to `True`
            auth = True
            
        print()


    print("Login successful")
    

if __name__ == "__main__":
    main()