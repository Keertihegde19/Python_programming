s = input("Enter a string: ")
if s == "":
    print("String not empty")
else:
    words = s.split()
    print("Number of words:", len(words))