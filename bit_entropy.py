import numpy as np
from PIL import Image

img = Image.open("image.png").convert("RGB")
arr = np.array(img, dtype=np.uint8)

def bitplane_entropy(arr):
    entropies = []
    for k in range(8):
        plane = (arr >> k) & 1
        p1 = plane.mean()
        p0 = 1 - p1
        if p0 == 0 or p1 == 0:
            H = 0.0
        else:
            H = -(p0*np.log2(p0) + p1*np.log2(p1))
        entropies.append(H)
    return entropies

ent = bitplane_entropy(arr)
for k, H in enumerate(ent):
    print(f"Bit {k}: entropía = {H:.3f}")
