def nth_prime(n):
    if n <= 0:
        return None

    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

        candidate += 1

    return primes[-1]

n = int(input("Enter the value of n: "))
result = nth_prime(n)

if result is not None:
    print(f"The {n}-th prime number is {result}")
else:
    print("Invalid input. Please enter a positive integer.")
