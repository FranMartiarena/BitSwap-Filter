import cv2
import os

# Parámetros
image_folder = "bitswap_frames"
output_video = "bitswap2.mp4"
fps = 10

# Leer primera imagen para obtener tamaño
first_frame = cv2.imread(os.path.join(image_folder, "0.png"))
height, width, _ = first_frame.shape

# Crear writer de video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Escribir frames en orden
for i in range(101):
    img_path = os.path.join(image_folder, f"{i}.png")
    frame = cv2.imread(img_path)
    video.write(frame)

video.release()
