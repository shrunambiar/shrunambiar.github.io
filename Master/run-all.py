import os

os.chdir('data/train/')
os.system('python tokenizer.py')
os.chdir('../..')

os.chdir('data/test/')
os.system('python tokenizer.py')
os.chdir('../..')

os.system('python labeller.py ./data/train/Tokenized_train.csv train')
os.system('python preprocessing.py labelled_data_train.csv')
os.system('python generate_features.py preprocessed_data_train.csv')

os.system('python labeller.py ./data/test/Tokenized_test.csv test')
os.system('python preprocessing.py labelled_data_test.csv')
os.system('python generate_features.py preprocessed_data_test.csv')
