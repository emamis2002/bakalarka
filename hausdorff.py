import numpy as np
from scipy.ndimage import distance_transform_edt
from PIL import Image

image = Image.open('bin_img.png').convert('L')
image = image.point(lambda p: 255 if p<255 else 0)
data = np.asarray(image)
image2 = Image.open('bin_img_extra.png').convert('L')
image2 = image2.point(lambda p: 255 if p<255 else 0)
data2 = np.asarray(image2)

#na oba obrazky aplikujeme edt
img_transf = distance_transform_edt(data)
img_transf2 = distance_transform_edt(data2)

#pre kazdy pixel vypocitame rozdiel priradenych dvoch vzdialenosti
final = []
for x in range(len(img_transf)):
    for y in range(len(img_transf[0])):
        final.append(abs(img_transf[x][y] - img_transf2[x][y]))

#hausdorff je definovany ako max z takych rozdielov
print(max(final))
