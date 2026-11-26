s = input("Enter the main string: ")
sub = input("Enter the substring: ")

if not s.strip():
    print("Main string cannot be empty")

elif not sub:
    print("Substring cannot be empty")

else:
    pos = int(input("Enter the position: "))

    if 0 <= pos <= len(s):
        result = s[:pos] + sub + s[pos:]
        print("Result:", result)
    else:
        print("Invalid position")