total = 0
for num in range(2, 200):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        total += num

print("Sum of prime numbers below 200:", total)
