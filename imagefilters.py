#https://github.com/Machine-Learning-Tokyo/DL-workshop-series/blob/master/Part%20I%20-%20Convolution%20Operations/ConvKernels.ipynb
from cv2 import filter2D
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
import requests
from io import BytesIO
url = 'https://fr.mathworks.com/matlabcentral/answers/uploaded_files/20770/lenaTest3.jpg'
img = Image.open(BytesIO(requests.get(url).content))

img = np.array(img)
plt.axis('off')
plt.imshow(img, cmap='gray')
plt.show()

identity = [0, 0, 0,
            0, 1, 0,
            0, 0, 0]

edge1 = [1, 0, -1,
         0, 0, 0,
         -1, 0, 0]

edge2 = [0,  1, 0,
         1, -4, 1,
         0,  1, 0]

edge3 = [-1, -1, -1,
         -1,  8, -1,
         -1, -1, -1]

sharpen = [ 0, -1,  0,
           -1,  5, -1,
            0, -1,  0]

box_blur = [1, 1, 1,
            1, 1, 1,
            1, 1, 1]
box_blur = [1/9 * i for i in box_blur]

gaussian_blur1 = [1, 2, 1,
                  2, 4, 2,
                  1, 2, 1]
gaussian_blur1 = [1/16 * i for i in gaussian_blur1]

gaussian_blur2 = [1,  4,  6,  4, 1,
                  4, 16, 24, 16, 4,
                  6, 24, 36, 24, 6,
                  4, 16, 24, 16, 4,
                  1,  4,  6,  4, 1,]
gaussian_blur2 = [1/256 * i for i in gaussian_blur2]

horizontal_lines = [-1, -1, -1,
                     2,  2,  2,
                    -1, -1, -1]

vertical_lines = [-1, 2, -1,
                  -1, 2, -1,
                  -1, 2, -1]

kernel = np.array(box_blur)
filtered = filter2D(img, 0, kernel)

f, ax = plt.subplots(1, 2, figsize=(12, 12))
ax[0].imshow(img, cmap = 'gray')
ax[0].set_title("original")
ax[0].axis('off')
ax[1].imshow(filtered, cmap = 'gray')
ax[1].set_title("filtered")
ax[1].axis('off')
plt.show()

