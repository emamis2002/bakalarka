from scipy.spatial import cKDTree
import numpy as np
from PIL import Image

image = Image.open('bin_img.png').convert('L')
image = image.point(lambda p: 0 if p<255 else 255)
data = np.asarray(image)

def dowa(matrix,n):
    coords = np.column_stack(np.where(matrix==255))
    kdtree = cKDTree(coords)
    total_weight = sum(range(1, n + 1))  
    weights = np.array([(n - i) / total_weight for i in range(n)])
    coords_all = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
    new = np.zeros_like(matrix, dtype = float)
    distances, indices = kdtree.query(coords_all, k=n)
    i=0
    for x in coords_all:
        #normalizujeme vzdialenosti
        distances[i] = (distances[i]-distances[i].min())/(distances[i].max()-distances[i].min())
        #nahradenie sucinu za min
        new[x[0]][x[1]] = sum(min(a,b) for a,b in zip(weights,distances[i]))
        i+=1
    newnew = np.uint8(255 * (new - new.min()) / (new.max() - new.min()))
    im = Image.fromarray(newnew)  
    im.save('owdt_min.png')

dowa(data,500)
