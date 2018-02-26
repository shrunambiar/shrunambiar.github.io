import glob
import pandas


def words(data):
    lineStream = iter(data)
    for line in lineStream:
        for word in line.split():
            yield word

list=[]
filename_list=[]
n_gram=[]

for filename in glob.iglob('*.txt'):
     with open(filename, 'r') as myself:
         for word in words(myself):
             list.append(word)
             filename_list.append(filename)
             n_gram.append(1)

i=0
n=len(list)-1

while(i<n):
    list.append(list[i]+ " " +list[i+1])
    filename_list.append(filename)
    n_gram.append(2)
    i=i+1

i=0
while(i<n-1):
    list.append(list[i]+ " " +list[i+1]+" " +list[i+2])
    filename_list.append(filename)
    n_gram.append(3)
    i=i+1






df = pandas.DataFrame(data={"All-Words": list, "filename": filename_list,"n-gram": n_gram})
df.to_csv("list.csv", sep=',',index=False)
