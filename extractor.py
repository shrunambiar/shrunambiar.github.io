import glob
import pandas


def words(data):
    lineStream = iter(data)
    for line in lineStream:
        for word in line.split():
            yield word

list=[]

for filename in glob.iglob('*.txt'):
     with open(filename, 'r') as myself:
         for word in words(myself):
             list.append(word)

i=0
n=len(list)-1

while(i<n):
    list.append(list[i]+ " " +list[i+1])
    i=i+1

i=0
while(i<n-1):
    list.append(list[i]+ " " +list[i+1]+" " +list[i+2])
    i=i+1


df = pandas.DataFrame(data={"All-Words": list})
df.to_csv("list.csv", sep=',',index=False)
