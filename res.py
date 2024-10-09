import random

random_numbers = [random.randint(1, 100) for _ in range(100)]
random_numbers_string = ",".join(map(str, random_numbers))

print(random_numbers_string)
