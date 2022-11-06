import cv2
import os
import glob
from PIL import Image

def tratar_imagens(pasta_origem, pasta_destino='ajeitado'):
    arquivos = glob.glob(f"{pasta_origem}/*")
    
    #primeiro tratamento, aplicar o methodo nas imagens e salvar na pasta
    for arquivo in arquivos:
        imagem = cv2.imread(arquivo)

        #transformando a imagem em escala de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

        _, img_tratada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
        nome_arq = os.path.basename(arquivo)
        cv2.imwrite(f'{pasta_destino}/{nome_arq}', img_tratada)
    
    #segundo tratamento, fazer a imagem intensificar as letras e clarear o fundo
    arquivos = glob.glob(f"{pasta_destino}/*")
    for arquivo in arquivos:
        imagem = Image.open(arquivo)
        imagem = imagem.convert("P")
        imagem2 = Image.new("P", imagem.size, (255, 255, 255))

        for x in range(imagem.size[1]):
            for y in range(imagem.size[0]):
                cor_pixel = imagem.getpixel((y,x))
                if cor_pixel < 115:
                    imagem2.putpixel((y,x), (0, 0, 0))
        nome_arq = os.path.basename(arquivo)
        imagem2.save(f'{pasta_destino}/{nome_arq}')

    #terceiro tratamento

if __name__ == "__main__":
    tratar_imagens('bdcaptcha')