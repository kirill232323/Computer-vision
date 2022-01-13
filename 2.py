import numpy as np, matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)
    image[i, i, :] = [r, g, b]

for i in range(size-1):
    j = 0
    while j != i:
        j+=1
        if i+j < size:
            image[i+j, i-j], image[i+j-1, i-j], image[i+j, i-j+1]  = image[i, i], image[i, i], image[i, i]
            image[i-j, i+j], image[i-j+1, i+j], image[i-j, i+j-1]  = image[i, i], image[i, i], image[i, i]
image[size-1, 0], image[0, size-1]= image[size-2, 1], image[1, size-2]


plt.figure(1)
plt.imshow(image)
plt.show()