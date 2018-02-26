import os

os.chdir('data/train/')
os.system('python tokenizer.py')
os.chdir('../..')

os.chdir('data/test/')
os.system('python tokenizer.py')
os.chdir('../..')

os.system('python labeller.py ./data/train/Tokenized_train.csv')
os.system('python preprocessing.py labelled_data.csv')
os.system('python generate_features.py preprocessed_data_train.csv')

os.system('python preprocessing.py ./data/train/Tokenized_test.csv.csv')
os.system('python generate_features.py preprocessed_data_train.csv')
