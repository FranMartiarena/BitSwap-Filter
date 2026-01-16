import numpy as np
from PIL import Image
i=0
for p in np.arange(0.0, 1.001, 0.01):  # probabilidad de invertir el MSB

    img = Image.open("image2.jpg").convert("RGB")
    arr = np.array(img, dtype=np.uint8)

    # Máscara Bernoulli(p)
    mask = (np.random.rand(*arr.shape) < p).astype(np.uint8)

    # Invertir MSB solo donde mask == 1
    arr_prob = arr ^ (mask * 128)

    img_out = Image.fromarray(arr_prob, mode="RGB")
    img_out.save(f"bitswap_frames/{i}.png")
    print(f"guardada imagen con p={p}")
    i+=1