try:
    s = input("Enter a string: ")

    if not s.strip():
        raise ValueError("String cannot be empty")

    rev = s[::-1]

    if s == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

except ValueError as e:
    print("Error message:", e)
