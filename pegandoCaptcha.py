import pyautogui as py
import time as t

t.sleep(3)

for i in range(5):
    img = py.screenshot(region=(301,635, 270, 100))  # esqueda, topo, largura, altura
    img.save(f"bdcaptcha\\imagem{i}.png")
    py.press("F5")
    t.sleep(0.7)