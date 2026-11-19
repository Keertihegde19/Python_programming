
main = input("Enter main string: ")
sub = input("Enter substring: ")

for i in range(len(main) - len(sub) + 1):
    if main[i:i + len(sub)] == sub:
        print("Substring found at position:", i)
