from functools import reduce
import csv

with open("COVID-19_Assistance.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))

def to_dictionary(keys, values):
	dictionary = {}
	for i in range(len(keys)):
		dictionary[keys[i]] = values[i]
	return dictionary

dataset = list(map(lambda x: to_dictionary(keys, x), dataset))

grants = list(map(lambda x: round(int(x['Amount']), 2), dataset))
sum_of_grants = round(reduce(lambda x, y: x + y, grants), 2)
average_grant = round(sum_of_grants / len(grants), 2)

print("Sum of grants:", sum_of_grants,"\nCount of Assistance:",len(grants),"\nAverage Assistance:", average_grant)