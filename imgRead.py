from matplotlib import pyplot as plt

from skimage import io, filters

path = 'C:\\Users\\ervin.pora\\Pictures\\ImgFiltering\\'
img_catndog = io.imread(path+'catndog.jpg', True)
img_giraffes = io.imread(path+'giraffes.jpg', True)
img_shark = io.imread(path+'shark.jpg', True)
img_tiger = io.imread(path+'tiger.jpg', True)

img1 = filters.roberts(img_catndog)
img2 = filters.sobel(img_giraffes)
img3 = filters.scharr(img_shark)
img4 = filters.prewitt(img_tiger)

fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax = axes.ravel()

ax[0].imshow(img1)
ax[0].set_title("Roberts")

ax[1].imshow(img2)
ax[1].set_title("Sobel")

ax[2].imshow(img3)
ax[2].set_title("Scharr")

ax[3].imshow(img4)
ax[3].set_title("Prewitt")

for a in ax.ravel():
    a.axis('off')

fig.tight_layout()
plt.show()
