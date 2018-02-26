import os
# os.system('time python ./data/train/extractor2.py')
os.system('time python tagcheck4.py ./data/train/listtrain.csv')
os.system('time python preprocessing.py')
os.system('time python feature_distance_from_verb.py train')

# os.system('time python ./data/test/extractor2.py')
os.system('time python tagcheck4.py ./data/test/listtest.csv')
os.system('time python preprocessing.py')
os.system('time python feature_distance_from_verb.py test')
