def main():
    s1 = "hello"
    s2 = "ollex"

    s1_index = 0
    s2_index = len(s2) - 1

    while True:
        if s1_index == len(s1) - 1 or s2_index == 0 and s1[s1_index] == s2[s2_index]:
            print("They are the same")
            break
        elif s1_index > len(s1) - 1 or s2_index < 0:
            print("They are not the same")
            break

        if s1[s1_index] != s2[s2_index]:
            print("They are not the same")
            break

        s1_index += 1
        s2_index -= 1
    




if __name__ == "__main__":
    main()