from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
import numpy as np


def make_plot(k_means, X, y, n_clusters):
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)  # 156 colors max
    for i, la in enumerate(k_means.labels_):
        if la > 155: #
            la = la - np.round(la/155, 0) * 155
        plt.scatter(float(X[i]), float(y[i]), color=colors.items()[la][0], linewidths=0.1)

    plt.xlabel("Community Area")
    plt.xticks([i for i in xrange(1, 78, 2)])
    plt.ylabel("Description crimea")
    plt.title("Clusters val: "+str(n_clusters))

    plt.savefig("reports/plot.pdf")
    plt.show()
