numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    for k in range(2, numbers[i]):
        if numbers[i] % k == 0:
            is_prime = False
            break
    if is_prime and numbers[i]!=1:
        primes.append(numbers[i])
    elif is_prime == False and numbers[i]!=1:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)