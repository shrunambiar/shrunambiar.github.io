Sequence of run commands to run code :






1. python run-all.py command_line_arg

    -train : will run on a 2/3rd 1/3rd split on training data and generate 2 csv files accordingly containing features

    -test : will run on entire dataset with test set of 100 docs as test and set of 200 docs as training set and generate 2 csv files accordingly containing features








2. python classify.py

    Will model a classifier based on training csv file and will run that on testing csv file. Will print precision and recall before and after applying post-processing rules.
