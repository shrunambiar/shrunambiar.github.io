import os
import sys

if sys.argv[1] == "train":
    os.chdir('data/training_split/train/')
    os.system('python tokenizer.py')
    os.chdir('../../..')

    os.chdir('data/training_split/test/')
    os.system('python tokenizer.py')
    os.chdir('../../..')

    os.system('python labeller.py ./data/training_split/train/Tokenized_train.csv train')
    os.system('python preprocessing.py labelled_data_train.csv')
    os.system('python generate_features.py preprocessed_data_train.csv')

    os.system('python labeller.py ./data/training_split/test/Tokenized_test.csv test')
    os.system('python preprocessing.py labelled_data_test.csv')
    os.system('python generate_features.py preprocessed_data_test.csv')
elif sys.argv[1] == "test":
    os.chdir('data/corpus_split/train/')
    os.system('python tokenizer.py')
    os.chdir('../../..')

    os.chdir('data/corpus_split/test/')
    os.system('python tokenizer.py')
    os.chdir('../../..')

    os.system('python labeller.py ./data/corpus_split/train/Tokenized_train.csv train')
    os.system('python preprocessing.py labelled_data_train.csv')
    os.system('python generate_features.py preprocessed_data_train.csv')

    os.system('python labeller.py ./data/corpus_split/test/Tokenized_test.csv test')
    os.system('python preprocessing.py labelled_data_test.csv')
    os.system('python generate_features.py preprocessed_data_test.csv')
