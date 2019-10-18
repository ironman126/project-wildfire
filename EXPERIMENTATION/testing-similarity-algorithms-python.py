from math import *
import time
def percentage(x):
    return (str(x * 100) + "%")

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)

def average(array):
    average = 0
    for i in array:
        average = average + i

    average = average / len(array)
    return average


wildfireDataset = [[1, 5, 4, 60], [3, 3, 7, 45], [2, 6, 3, 75], [2, 4, 8, 90], [1, 3, 7, 100], [1, 6, 3, 30], [4, 10, 4, 90], [1, 4, 5, 50], [3, 7, 6, 62], [1, 5, 4, 60]]

currentDataset = []

while True:
    if len(currentDataset) > 3:
        break
    currentInput = int(input("Add to dataset:"))
    currentDataset.append(currentInput)

results = []
for fire in wildfireDataset:
    similarity = cosine_similarity(currentDataset, fire)
    results.append(similarity)
    time.sleep(0.05)
    print(similarity)

print("AVERAGE:")
print(percentage(average(results)))
