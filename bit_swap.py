import numpy as np
from PIL import Image

# Cargar imagen
img = Image.open("image4.jpg").convert("RGB")
arr = np.array(img, dtype=np.uint8)

# Extraer bits
msb = (arr >> 7) & 1          # bit 7
lsb = arr & 1                # bit 0

# Limpiar MSB y LSB
arr_cleared = arr & 0b01111110

# Insertar bits intercambiados
arr_swapped = arr_cleared | (lsb << 7) | msb

# Volver a imagen
img_out = Image.fromarray(arr_swapped, mode="RGB")
img_out.save("output_swap4.png")
