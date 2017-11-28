from collections import Counter

from sklearn.cluster import KMeans


def make_k_means(n_clusters, data):
    if n_clusters == -1:
        n_clusters = len(Counter([i[1] for i in data]))
    k_means = KMeans(n_clusters=n_clusters)
    a = k_means.fit(data)
    centrx = k_means.cluster_centers_
    return k_means, n_clusters
