import glob
import pandas


def words(data):
    lineStream = iter(data)
    for line in lineStream:
        for word in line.split():
            yield word

list_of_one_gram=[]
list_of_two_gram=[]
for filename in glob.iglob('*.txt'):
     with open(filename, 'r') as myself:
         for word in words(myself):
             list_of_one_gram.append(word)
i=0
n=len(list_of_one_gram)-1
while(i<n):
    list_of_two_gram.append(list_of_one_gram[i]+ " " +list_of_one_gram[i+1])
    i=i+1


df = pandas.DataFrame(data={"1-gram": list_of_one_gram})
df.to_csv("list_one.csv", sep=',',index=False)

df = pandas.DataFrame(data={"2-gram": list_of_two_gram})
df.to_csv("list_two.csv", sep=',',index=False)
