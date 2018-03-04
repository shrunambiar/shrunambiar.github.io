import glob
import pandas


def words(data):
    lineStream = iter(data)
    for line in lineStream:
        for word in line.split():
            yield word

def get_all_list(typeoffile):
    list=[]
    filename_list=[]
    n_gram=[]
    start=[]
    end=[]
    # print glob.iglob("./*.txt")
    for filename in glob.iglob("*.txt"):
         print filename
         with open(filename, 'r') as myself:
             index=0
             for word in words(myself):
                 if word[-1] == "," or word[-1] == ":" or word[-1] == ".":
                     word = word[:-1]
                 word = word.replace("\"", "")
                 #word = word.replace("\'", "")
                 if len(word) == 0:
                     continue
                 list.append(word)
                 filename_list.append("./data/" + typeoffile +"/" + filename)
                 # print "./data/" + typeoffile +"/" + filename
                 n_gram.append(1)
                 start.append(index)
                 end.append(index)
                 index+=1
    i=0
    n=len(list)-1

    while(i<n):
        list.append(list[i]+ " " +list[i+1])
        filename_list.append(filename_list[i])
        n_gram.append(2)
        start.append(start[i])
        end.append(start[i]+1)
        i=i+1

    i=0
    while(i<n-1):
        list.append(list[i]+ " " +list[i+1]+" " +list[i+2])
        filename_list.append(filename_list[i])
        n_gram.append(3)
        start.append(start[i])
        end.append(start[i]+2)
        i=i+1
    return list,filename_list,n_gram,start,end


def print_to_csv(typeoffile):
    print typeoffile
    list=[]
    filename_list=[]
    n_gram=[]
    start=[]
    end=[]
    list,filename_list,n_gram,start,end=get_all_list(typeoffile)
    df = pandas.DataFrame(data={"All-Words": list, "filename": filename_list,"n-gram": n_gram, "start": start, "end":end})
    print typeoffile
    df.to_csv("Tokenized_" + typeoffile + ".csv", sep=',',index=False)

# if __name__ == '__main__':
    # print_to_csv("cleanfiles")
print_to_csv("train")
