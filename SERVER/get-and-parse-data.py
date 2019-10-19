import requests

modis6 = requests.get("https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_SouthEast_Asia_24h.csv")
modis6 = modis6.content
print(modis6)
jsonfile = open("output-modis6.json", "w")
modis6 = modis6.decode("utf-8")
splitModis6 = modis6.split("\n")

for i in splitModis6:
    print(str(i))
