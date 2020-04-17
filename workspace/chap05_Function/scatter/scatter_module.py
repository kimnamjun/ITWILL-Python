from statistics import mean, variance, stdev # 통계 함수
from math import sqrt # 수학 함수


def avg(dataset):
    return mean(dataset)


def var_std(dataset):
    avg = mean(dataset)
    diff = [(x - avg) ** 2 for x in dataset]
    diff_sum = sum(diff)
    var = diff_sum / (len(dataset) - 1)
    std = sqrt(var)
    return var, std
