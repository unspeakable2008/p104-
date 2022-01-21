from  collections import Counter
import csv
with open ("height-weight.csv",newline = "")as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for I in range (len(fileData)):
    num = fileData[I][2]
    newData.append(float(num))
n = len(newData)
data = Counter(newData)
getMode = dict(data)
mode = []
mode1 = []
mode2 = []
for a,v in getMode.items():
    a = float(a)
    if 90<a<100:
        if v == max(list(data.values())):
            mode.append(a)
    elif 110<a<125:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 125<a<145:
        if v == max(list(data.values())):
            mode2.append(a)
print(mode)
print(mode1)
print(mode2)
if len(mode)>len(mode1) and len(mode2):
    print(mode)
elif len(mode1)>len(mode2) and len(mode):
    print(mode1)
elif len(mode2)>len(mode1) and len(mode):
    print(mode2)
