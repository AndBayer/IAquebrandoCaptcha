import cv2
import os
import glob

arquivos = glob.glob('ajeitado/*')
for arquivo in arquivos:
    img = cv2.imread(arquivo) #ler o arquivo
    #transformar em preto e branco, por mais que ja esteja ele le como RGB
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #deixa cinza
    _, nova_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV) #deixa preto e branco

    #encontrar os contornos de cada letra
    contornos, _ = cv2.findContours(nova_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regiao_letras = []

    #filtrar contornos que são de letras e nao apenas marcas na tela
    for contorno in contornos:
        (x, y, largura, altura) = cv2.boundingRect(contorno)
        area = cv2.contourArea(contorno)
        if area > 115:
            regiao_letras.append((x, y, largura ,altura))

    if len(regiao_letras) != 5: #se achar valor != de 5 retangulos ele n vai considerar
        print("AQUI É UM CASO, arquivo: ", arquivo)
        continue
    

    # Desenhar os contornos e separar as letras em arquivos individuais

    img_final = cv2.merge([img] * 3)
    i = 0
    for retangulo in regiao_letras:
        x, y, largura, altura = retangulo
        img_letra = img[y-2:y+altura+2, x-2:x+largura+2]
        nome_arquivo = os.path.basename(arquivo).replace(".png", f"letra{i}.png")
        cv2.imwrite(f'letras/{nome_arquivo}', img_letra)
        cv2.rectangle(img_final, (x-2,y-2),(x+largura+2, y+altura+2) ,(255, 0, 0), 1)
        i += 1
    nome_arquivo = os.path.basename(arquivo)
    cv2.imwrite(f"identificado/{nome_arquivo}", img_final)


