De entre todo el codigo basura de mi compu, algunos destacan por su factor artistico. Estuve probando algunos algoritmos de procesamiento de imagenes que hice hace unos años, y debo decir que safan... 

Éste algoritmo en particular, que le puse de nombre _bit swap_, es muy boludo pero queda lindo; 

La idea es tomar una imagen RGB y cambiar de lugar el bit mas significativo con el menos significativo en cada canal para cada pixel.

Por ejemplo, si un pixel tiene el valor (255, 1, 1), entonces como 255 en binario es 11111111, cambiando el LSB (Least significant bit) por el MSB (Most significant bit) queda igual. Por otro lado 1 en binario es 00000001, y cambiando el LSB con el MSB queda 10000000 que es 128. Entonces el pixel final termina siendo (255, 128, 128).


Original             |  Bit Swap
:-------------------------:|:-------------------------:
![](data/image2.jpg) | ![](data/output_swap2.png)
![](data/image3.png) | ![](data/output_swap3.png)
![](data/image4.jpg) | ![](data/output_swap4.png)
![](data/image1.jpg) | ![](data/output_swap1.png)
