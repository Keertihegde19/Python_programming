main = input("Enter main string: ")
sub = input("Enter substring: ")

if main == "" or sub == "":
    print("String empty") 
else:
    for i in range(len(main) - len(sub) + 1):
        if main[i:i + len(sub)] == sub:
            print("Substring found at position:", i)
