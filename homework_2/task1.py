import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [250, 60, 100]
color2 = [0, 90, 150]

v = np.linspace(0, 1, image.shape[0] * 2 - 1)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        
        t0 = v[i + j]
        r = lerp(color1[0], color2[0], t0)
        g = lerp(color1[1], color2[1], t0)
        b = lerp(color1[2], color2[2], t0)
        image[j, i, :] = [r, g, b]

plt.figure(1)
plt.imshow(image)
plt.show()
