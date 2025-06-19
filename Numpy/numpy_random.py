import numpy as np

number = np.random.randint(100)
print(f"A random number in range of 100: {number}")

rand_array = np.random.randint(100, size = (4, 4)) # Creates 4*4 array with random values
print(f"\nA 4*4 array of random values:\n{rand_array}")

# you can set a range too like so:
# np.random.randint(90, 100, size = (4, 4))

rand_choice = np.random.choice([2, 4, 6, 8, 10])
print(f"\n{rand_choice}")
