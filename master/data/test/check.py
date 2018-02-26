import glob

def words(data):
    lineStream = iter(data)
    for line in lineStream:
        for word in line.split():
            yield word

for filename in glob.iglob("./*.txt"):
     with open(filename, 'r') as myself:
         openindex=0
         closeindex=0
         for word in words(myself):
             if "<n>" in word:
                 openindex += 1
                 if word[0:3] != "<n>":
                     print "POSITION of <n>", word, filename
                     continue
             if "</n>" in word:
                 closeindex += 1
                 if word[-4:] != "</n>" and word[-1] != "," and word[-1] != ".":
                     print "POSITION of </n>", word, filename
                     continue

         if openindex != closeindex:
             print "MISMATCH COUNT", filename
