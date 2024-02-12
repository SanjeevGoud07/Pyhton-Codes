def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check if n is divisible by any number from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
n = int(input())  # Generate prime numbers up to 50
prime_numbers = generate_primes(n)
print("Prime numbers up to", n, "are:", prime_numbers)
