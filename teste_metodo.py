import cv2
from PIL import Image

#TESTANDO QUAL MÉTODO VAI SER O MELHOR PARA CONVERTER O CAPTCHA
metodos = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

imagem = cv2.imread("bdcaptcha/telanova0.png")

#transformando a imagem em escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

i = 0
for metodo in metodos:
    _, img_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU)
    cv2.imwrite(f'teste_metodo/img_tratada{i}.png', img_tratada)
    i += 1

imagem = Image.open("teste_metodo/img_tratada2.png")
imagem = imagem.convert("P")
imagem2 = Image.new("P", imagem.size, (255, 255, 255))

for x in range(imagem.size[1]):
    for y in range(imagem.size[0]):
        cor_pixel = imagem.getpixel((y,x))
        if cor_pixel < 115:
            imagem2.putpixel((y,x), (0, 0, 0))
imagem2.save('teste_metodo/imagemfinal.png')