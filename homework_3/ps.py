import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology as mrg

image = np.load('C:/ps.npy.txt')
plt.figure(figsize=(8,6), dpi=100)
plt.imshow(image[100:300, 200:400])

mask1 = np.ones((4,6)) # ࡮

mask2 = np.ones((4,6)) # ப
mask2[:2,2:4] = 0

mask3 = np.flip(mask2) # п

mask4 = np.transpose(mask2) # ɔ
mask5 = np.transpose(mask3) # c

masks = np.array([mask1, mask2, mask3, mask4, mask5])

result = []

for i in range(5):
    image_new = mrg.binary_hit_or_miss(image, masks[i])
    result.append(np.sum(image_new))

symbols = ['࡮','ப','п','ɔ','c']
for i in range(len(result)):
    print(result[i],'-',symbols[i])
print(np.sum(result),'- all')
