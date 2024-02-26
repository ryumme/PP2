def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [12, 25, 31, 44, 53, 67, 79, 88, 97]
prime = list(filter(lambda x: is_prime(x), numbers))

print(prime)