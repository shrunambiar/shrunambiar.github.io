import os
os.system('python ./data/train/extractor2.py')
os.system('python tagcheck4.py ./data/train/listtrain.csv')
os.system('python preprocessing.py')
os.system('python feature_distance_from_verb.py train')

os.system('python ./data/test/extractor2.py')
os.system('python tagcheck4.py ./data/test/listtest.csv')
os.system('python preprocessing.py')
os.system('python feature_distance_from_verb.py test')
