from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('https://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii','ignore')
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
# for row in csvReader:
#     print('The album "'+row[0]+'" was released in '+str(row[1]))

dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)