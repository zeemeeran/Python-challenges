import random
import math

def rand_stream():
    while True:
        yield random.random()

print(rand_stream)
print(math.ceil(next(rand_stream()) * 100))