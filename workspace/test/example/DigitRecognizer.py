import csv
import numpy as np
import pandas as pd
path = 'C:/Users/user/Desktop/Digit_Recognizer/'


class Digit:
    def __init__(self, data):
        self.label = data[0]
        self.pixel = np.array(data[1:]).reshape(28, 28)
        # self.binary_pixel = np.array([0 if int(d) < 100 else 1 for d in data[1:]]).reshape(28, 28)


# with open(f'{path}train.csv') as csvfile:
#     train = csv.reader(csvfile)
#     # for line in train:
#     #     print(line)
#     train_list = list(train)

train = pd.read_csv(f'{path}train.csv', header=0)

print(train)