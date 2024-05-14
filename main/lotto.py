import random

def generate_unique_numbers():
    return random.sample(range(0, 10), 6)

unique_numbers = generate_unique_numbers()
# unique_numbers.sort()
print(unique_numbers)