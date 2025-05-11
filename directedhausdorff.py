import numpy as np
from PIL import Image
from scipy.spatial.distance import directed_hausdorff

image = Image.open('bin_img.png').convert('L')
image2 = Image.open('bin_img2.png').convert('L')

image = image.point(lambda p: 0 if p<255 else 255)
image2 = image2.point(lambda p: 0 if p<255 else 255)

data = np.asarray(image)
data2 = np.asarray(image2)

#zistenie suradnic tych pixelov, ktorym je priradena hodnota 255
koord1 = np.column_stack(np.where(data==255))
koord2 = np.column_stack(np.where(data2==255))

a = directed_hausdorff(koord1,koord2)
#vzdialenost
print(a[0])
#suradnice bodov z oboch obrazkov, z ktorych je vzdialenost vypocitana
print(a[1:])
b = directed_hausdorff(koord2,koord1)
print(b[0])
print(b[1:])

print(koord1[a[1:][0]])
print(koord2[a[1:][1]])

print(koord2[b[1:][0]])
print(koord1[b[1:][1]])

