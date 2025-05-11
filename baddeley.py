import numpy as np
from scipy.ndimage import distance_transform_edt
from PIL import Image

image = Image.open('bin_img.png').convert('L')
image = image.point(lambda p: 255 if p < 255 else 0)
data = np.asarray(image)
image2 = Image.open('bin_img_extra.png').convert('L')
image2 = image2.point(lambda p: 255 if p < 255 else 0)
data2 = np.asarray(image2)

img_transf = distance_transform_edt(data)
img_transf2 = distance_transform_edt(data2)

#pre kazdy pixel vypocitame rozdiel priradenych 2 vzdialenosti
#a v absolutnej hodnote scitame vsetky pretoze alfa = 1
suma = 0
for x in range(len(img_transf)):
    for y in range(len(img_transf[0])):
        suma += abs(img_transf[x][y] - img_transf2[x][y])

print(suma/(len(img_transf)*len(img_transf[0])))

#baddeley je definovany ako podiel sumy a poctu vsetkych pixelov obrazka
#nasledne umocnenych na 1/alfa

        
    
