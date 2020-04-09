import csv
path = 'C:/Users/user/Desktop/Digit_Recognizer/'

with open(f'{path}train.csv') as csvfile:
    train = csv.reader(csvfile)
    # for line in train:
    #     print(line)
    train_list = list(train)
