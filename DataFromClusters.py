import matplotlib.pyplot as plt
import numpy as np


def get_data_clusters(k_means, X, y):
    data_cluster = dict()
    for i, la in enumerate(k_means.labels_):# la - cluster
        if la in data_cluster:
            data_cluster[la].append([X[i], y[i]])
        else:
            data_cluster[la] = [X[i], y[i]]

    data = []
    for i in range(len(data_cluster)):
        if i == 0 or i == 1:
            continue
        data.append(data_cluster[i])
    return data
