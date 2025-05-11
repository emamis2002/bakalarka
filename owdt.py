from scipy.spatial import cKDTree
import numpy as np
from PIL import Image

image = Image.open('bin_img.png').convert('L')
image = image.point(lambda p: 0 if p<255 else 255)
data = np.asarray(image)

def dowa(matrix,n):
    coords = np.column_stack(np.where(matrix==255))
    #umiestnenie bielych pixelov na zaklade suradnic do stromu
    kdtree = cKDTree(coords)
    #definovanie nasich vah
    total_weight = sum(range(1, n + 1))  
    weights = np.array([(n - i) / total_weight for i in range(n)])
    #suradnice vsetkych pixelov
    coords_all = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
    #vytvorenie novej matice
    new = np.zeros_like(matrix, dtype = float)
    #pridenie n vzdialenosti od n najblizsich bielych pixelov vzostupne, p z Minkowski
    distances, indices = kdtree.query(coords_all, k=n, p=1)
    i=0
    #priradenie kazdemu pixelu skalarny sucin vah a vzdialenosti
    for x in coords_all:
        new[x[0]][x[1]] = np.sum(weights *distances[i])
        i+=1
    newnew = np.uint8(255 * (new - new.min()) / (new.max() - new.min()))
    im = Image.fromarray(newnew)  
    im.save('owdt2_obr_manhattan.png')

dowa(data,1000)
