import glob

for filename in glob.iglob("./*.txt"):
     with open(filename, 'r') as myself:
         openindex=0
         closeindex=0
         for word in words(myself):
             if "<n>" in word:
                 openindex += 1
                 if word[0:3] != "<n>":
                     print "POSITION of <n>", filename
                     continue
             if "</n>" in word:
                 closeindex += 1
                 if word[-4:] != "</n>":
                     print "POSITION of </n>", filename
                     continue

         if openindex != closeindex:
             print "MISMATCH COUNT", filename
