import modules._start as starter

starter.clear_console()

from pandas import DataFrame
from sklearn.datasets import make_blobs

data, true_lables = make_blobs(n_samples=500, centers=4, random_state=6)

points = DataFrame(data, columns=['x1', 'x2'])
plot = points.plot.scatter('x1', 'x2')

plot.get_figure().savefig("clustering-blob")

# KMean
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4).fit(points)
kmeans_cluster_centers = DataFrame(kmeans.cluster_centers_,
                                   columns=['x1', 'x2'])

print(kmeans_cluster_centers)

plot = points.plot.scatter('x1', 'x2')
kmeans_cluster_centers.plot.scatter('x1',
                                    'x2',
                                    ax=plot,
                                    c='yellow',
                                    s=100,
                                    marker='*')
plot.get_figure().savefig('clustering-blob-kmean-centers')

plot = points.plot.scatter('x1',
                           'x2',
                           c=kmeans.labels_,
                           colormap='Dark2',
                           colorbar=False)
plot.get_figure().savefig('clustering-blob-kmean-centers-colored')

print(f'inertia: {kmeans.inertia_}')