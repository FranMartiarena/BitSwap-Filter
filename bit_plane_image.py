import numpy as np
from PIL import Image

# Cargar imagen RGB
img = Image.open("image4.jpg").convert("RGB")
arr = np.array(img, dtype=np.uint8)

channels = ["R", "G", "B"]

for i, ch in enumerate(channels):
    # Extraer LSB del canal i
    lsb = arr[:, :, i] & 1          # 0 o 1

    # Convertir a imagen visible (0 negro, 255 blanco)
    lsb_img = (lsb * 255).astype(np.uint8)

    # Guardar imagen
    Image.fromarray(lsb_img, mode="L").save(f"bitplane4_{ch}.png")
