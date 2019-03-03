def count_primes(n):
    if n <= 3:
        return n-1

    primes = 2

    for num in range(4, n+1):
        is_prime = True
        for num2 in range(2, num):
            if num % num2 == 0:
                is_prime = False
                break
        if is_prime is True:
            print(num)
            primes += 1
    return primes


print(count_primes(100))

