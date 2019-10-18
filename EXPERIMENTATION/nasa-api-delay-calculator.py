import time
import requests
from math import *

def percentage(x):
    return (str(x * 100) + "%")

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)

r = requests.get("https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_SouthEast_Asia_24h.csv")

take1 = r.content

while True:
    time.sleep(1)
    r2 = requests.get("https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_SouthEast_Asia_24h.csv")
    loop = r2.content

    if cosine_similarity(loop, take1) < 1:
        print("Change-preliminary")
        take2 = r2.content
        print(str(time.time()))
        break

while True:
    time.sleep(1)
    r3 = requests.get("https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_SouthEast_Asia_24h.csv")
    loop = r3.content

    if cosine_similarity(loop, take2) < 1:
        take2 = r3.content
        print("Change-ending")
        print(str(time.time()))
        break
    


