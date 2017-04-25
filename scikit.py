from skimage import io, filters

img = io.imread('images/Moai.jpg', True)
fsi = filters.scharr(img)

io.imshow(fsi)
io.show()
