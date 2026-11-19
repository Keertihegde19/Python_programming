days=int(input("Enter a number of days: "))
if days == 0:
        print("Book is returned on time")
elif days <= 5:
        fine = days * 0.5
        print("Fine=Rs.",fine)
elif days <= 10:
        fine = days * 1
        print("Fine=Rs.",fine)
elif days <= 30:
        fine = days * 5
        print("Fine=Rs.",fine)
else:
        print("Membership is Cancelled")