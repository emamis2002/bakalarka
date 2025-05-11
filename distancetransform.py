import numpy as np
from scipy.ndimage import distance_transform_edt
from scipy.ndimage import distance_transform_cdt
from PIL import Image

#prevedenie RGB obrazku, 3 hodnotoveho na grayscale, 1 hodnotovy
image = Image.open('bin_img.png').convert('L')
#prevedenie na binarny
image = image.point(lambda p: 0 if p<255 else 255)

data = np.asarray(image)

img_transf = distance_transform_edt(data)
img_transf_normalized = np.uint8(255 * (img_transf - img_transf.min()) / (img_transf.max() - img_transf.min()))
im = Image.fromarray(img_transf_normalized)
im.save('dt_euclidean.png')

img_transf = distance_transform_cdt(data, metric="taxicab")
img_transf_normalized = np.uint8(255 * (img_transf - img_transf.min()) / (img_transf.max() - img_transf.min()))
im = Image.fromarray(img_transf_normalized)
im.save('dt_manhattan.png')

img_transf = distance_transform_cdt(data, metric="chessboard")
img_transf_normalized = np.uint8(255 * (img_transf - img_transf.min()) / (img_transf.max() - img_transf.min()))
im = Image.fromarray(img_transf_normalized)
im.save('dt_chessboard.png')
