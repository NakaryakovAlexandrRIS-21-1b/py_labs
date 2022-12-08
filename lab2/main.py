from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, res, Sum, Average, random_sum')

Sum[X] = ((1 + X) * X) / 2
print("Sum 1..888888: ")
print(Sum[888888] == X)

Average[X] = (X + 1) / 2
print("Average 1..888888: ")
print(Average[888888] == X)

rand_numbers = [random.choice(range(888888)) for i in range(100)]
(res["random_sum"] == sum_(Z, for_each=Z)) <= Z.in_(rand_numbers)
print("Random sum: ")
print(res["random_sum"] == X)

# Медиана
print("Median: ")
print(rand_numbers[50])
