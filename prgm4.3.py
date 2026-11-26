try:
    s = input("Enter a string: ")

    if not s:
        raise ValueError("String cannot be empty")

    rev = s[::-1]

    if s == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)
