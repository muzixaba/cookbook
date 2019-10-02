#=======================
# View images from files
#=======================
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img2 = mpimg.imread('/path/to/image.png')
plt.imshow(img2)