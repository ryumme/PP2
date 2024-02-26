def filter_prime(st):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    numbers = []
    for st in st.split():
        try:
            num = int(st)
            numbers.append(num)
        except ValueError:
            print("Invalid number: {}".format(st))
        
    prime_numbers = [num for num in numbers if is_prime(num)]

    return prime_numbers

numbers = str(input())
prime_numbers = filter_prime(numbers)
print(prime_numbers)