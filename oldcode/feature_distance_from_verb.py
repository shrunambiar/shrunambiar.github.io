import pandas as pd
import string

df = pd.read_csv('lowercase cropped.csv')
df.insert(len(df.columns), "PRE_DIST_VERB", 100)
df.insert(len(df.columns), "POST_DIST_VERB",100)
df.insert(len(df.columns), "PRE_DIST_STOPWORD",100)
df.insert(len(df.columns), "POST_DIST_STOPWORD",100)
df.insert(len(df.columns), "PrecedingTitle", False)
df.insert(len(df.columns), "Apostrophe", False)
df.insert(len(df.columns), "PRE_DIST_FROM_THE", False)
df.insert(len(df.columns), "PRE_DIST_FROM_POSITION", 100)
df.insert(len(df.columns), "NEGATIVE_FEATURE", False)
df.insert(len(df.columns), "POSITIVE_FEATURE", False)
df.insert(len(df.columns), "Surrounding_Caps", False)
df.insert(len(df.columns), "POST_IS_PREPOSITION", False)
df.insert(len(df.columns), "POST_IS_SPEAK_VERB", False)
df.insert(len(df.columns), "RELATIONSHIP", False)

f = open('./other_text_files/verbs4.txt')
g = open('./other_text_files/stopwords.txt')
prep=open('./other_text_files/prepositions.txt')

def checkPrecedingPrefix(instance):
    l = instance.split(" ")
    # n = len(l)

    prefixes = ['Mr.', 'Mrs.', 'Dr.', 'Ms.', 'Sir.', 'Jr.', 'Sr.', 'Lord', 'Prince', 'Princess']

    # Positions=['Leader','Secretary','Prime Minister','Officer','Archbishop','Major','Chancellor','Minister','MEP', 'Officer','Spokesperson', 'Sheriff', 'Reporter', 'Sergent', 'General','Queen','Lieutenant','Colonel','Commander','Captain','Private','Specialist','Staff','Master','Brigadier','Airman','Seaman','Minister','Admiral','Deputy','MP', 'President', 'Vice president','Governor', 'Chair','Director','Controller','Inspector','Assistant','Priest','Professor','Principal','Lady','Viceroy','Vicar']


    if l[0] in prefixes or (l[0] + ".") in prefixes:
        return True
    return False

def checkSucceedingApostrophe(instance):
    l = instance.split(" ")
    # n = len(l)

    val = l[-1]

    if val[-1] == "\'" or val[-2:] == "\'s":
        return True

    return False

#------------------------------


verbs = f.read().split()
stopwords = g.read().split()
prepositions=prep.read().split()


for j in range(len(df)):
    sfile = open(df.loc[j]['filename'])
    ls = sfile.read().split()
    start = df.loc[j]['start']
    end = df.loc[j]['end']
    instance = df.loc[j]["All-Words"]


    if start>5:
        prestring = ls[start-5:start]
        if '.' in prestring:
            prestring = prestring[prestring.index('.')+1:]
    else:
        prestring = ls[0:start]
        if '.' in prestring:
            prestring = prestring[prestring.index('.')+1:]
    if end< len(ls)-5:
        postring = ls[end+1:end + 5]
        if '.' in postring:
            postring = postring[0:postring.index('.')]
    else:
        postring = ls[end+1:len(ls)-1]
        if '.' in postring:
            postring = postring[0:postring.index('.')]

    if start>1:
        preword = ls[start-1:start]
    else:
        preword = ls[0:start]


    if end< (len(ls)-1):
        postword=ls[end+1]
    else:
        postword= ""


    for i in postring:
        if i in verbs:
            df.at[j,"POST_DIST_VERB"]=postring.index(i)
            break


    if postword in prepositions
        df.at[j,"POST_IS_PREPOSITION]=True


    articles = ['The', 'the.', 'a', 'A', 'an', 'An']
    if preword in articles:
        df.at[j,"PRE_DIST_FROM_THE"]= True
        break

    speakwords = ['said', 'says', 'told', 'tells', 'commented', 'stated', 'reported','called', 'addressed','argued','exclaimed']
    if postword in speakwords:
        df.at[j,"POST_IS_SPEAK_VERB"]= True
        break

    relationships = ['father', 'mother', 'son', 'daughter', 'child', 'nephew', 'niece','uncle', 'aunt','granfather','grandmother','lover','husband','wife','advisor','teacher']
    if postword in relationships:
        df.at[j,"RELATIONSHIP"]= True
        break

    for k in prestring:
        if k in verbs:
            df.at[j,"PRE_DIST_VERB"]=len(prestring)- prestring.index(k)

    for i in postring:
        if i in stopwords:
            df.at[j, "POST_DIST_STOPWORD"] = postring.index(i)
            break
    for k in prestring:
        if k in stopwords:
            df.at[j,"PRE_DIST_STOPWORD"]=len(prestring)- prestring.index(k)

    for k in prestring:
        Positions=['Leader','Secretary','Prime Minister','Officer','Archbishop','Major','Chancellor','Minister','MEP',
                   'Officer','Spokesperson', 'Sheriff', 'Reporter', 'Sergent', 'General','Queen','Lieutenant','Colonel',
                   'Commander','Captain','Private','Specialist','Staff','Master','Brigadier','Airman','Seaman','Minister',
                   'Admiral','Deputy','MP', 'President', 'Vice president','Governor', 'Chair','Director','Controller',
                   'Inspector','Assistant','Priest','Professor','Principal','Lady','Viceroy','Vicar', 'Spokesman',
                   'Spokeswoman', 'Attorney', 'Pope', 'Reverend', 'Cardinal', 'Chief', 'Gen', 'Chairman', 'Judge']

        if k in Positions:
            df.at[j,"PRE_DIST_FROM_POSITION"]=len(prestring)- prestring.index(k)
            break
    loc_words = ['at', 'in', 'nearby', 'on', 'a']

    for k in prestring:
        if k in loc_words:
            df.at[j,"NEGATIVE_FEATURE"] = True

    positive_list = ['himself', 'herself', 'who']
    for k in postring:
        if k in positive_list:
            df.at[j, "POSITIVE_FEATURE"] = True

    if(len(prestring)>0):
        if prestring[len(prestring)-1][0] in string.ascii_uppercase:
                df.at[j,"Surrounding_Caps"] = True
    if(len(postring)>0):
        if postring [0][0] in string.ascii_uppercase:
                df.at[j, "Surrounding_Caps"] = True

    prefix = checkPrecedingPrefix(instance)
    df.at[j, "PrecedingTitle"] = prefix
    apostrophe = checkSucceedingApostrophe(instance)
    df.at[j, "Apostrophe"] = apostrophe

print "Writing feature DIST_VERB to file"

df.to_csv("distancetoverb.csv", sep=',', index=False)
