def isPalindrome(s):
    s_rev = s[::-1]

    if s == s_rev:
        return True
    
    return False

def main():
    s = "hello"

    if isPalindrome(s):
        print("Is Palindrome")
    else:
        print("Is not Palindrome")



if __name__ == "__main__":
    main()