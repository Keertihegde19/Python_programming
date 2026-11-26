s = input("Enter a string: ")
rev = ""
if s == "":
    print("String empty") 
else:
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]

    if s == rev:
        print("Palindrome")
    else:        
        print("Not a Palindrome")
