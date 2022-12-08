from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, res, Sum, Average, random_sum')

# Сумма арифметической  прогрессии Sn = ((a1+an)*n)/2 = ((1+888888)*888888)/2
Sum[X] = ((1 + X) * X) / 2
print("Sum 1..888888: ")
print(Sum[888888] == X)

# Среднее арифметической  прогрессии (888888+1)/2
Average[X] = (X + 1) / 2
print("Average 1..888888: ")
print(Average[888888] == X)

# Сумма рандомных случайных чисел от 1 до 888888
rand_numbers = [random.choice(range(888888)) for i in range(100)]
(res["random_sum"] == sum_(Z, for_each=Z)) <= Z.in_(rand_numbers)
print("Random sum: ")
print(res["random_sum"] == X)

# Медиана
print("Median: ")
print(rand_numbers[50])