import modules._start as starter

starter.clear_console()

# Loading image
from skimage import io

photo = io.imread(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Swallow-tailed_bee-eater_%28Merops_hirundineus_chrysolaimus%29.jpg/480px-Swallow-tailed_bee-eater_%28Merops_hirundineus_chrysolaimus%29.jpg'
)

# Reshaping to 2d array
import numpy as np

photo = np.array(photo, dtype=np.float64) / 255

w, h, d = original_shape = tuple(photo.shape)
image_array = np.reshape(photo, (w * h, d))

from pandas import DataFrame

pixels = DataFrame(image_array, columns=['Red', 'Green', 'Blue'])


# Adding color code column
def hex_encode(rgb):
    r = int(rgb[0] * 255)
    g = int(rgb[1] * 255)
    b = int(rgb[2] * 255)
    return '#%02x%02x%02x60' % (r, g, b)


pixels['color'] = [hex_encode(p) for p in image_array]
pixels_sample = pixels.sample(frac=0.05)

# Clustering
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10).fit(pixels_sample[['Red', 'Green', 'Blue']])
plt.imshow([kmeans.cluster_centers_
            ]).get_figure().savefig("bird-cluster-centers")

# Prediction by centers
labels = kmeans.predict(pixels[['Red', 'Green', 'Blue']])

reduced = np.array([kmeans.cluster_centers_[p]
                    for p in labels]).reshape(original_shape)

f, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(18, 9))
axs[0].imshow(photo)
axs[0].set_title('Original')
axs[1].imshow(reduced)
axs[1].set_title('RGB Clustered')

axs[0].get_figure().savefig('bird-rgb-clustered')