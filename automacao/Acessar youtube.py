import pyautogui as pa


pa.PAUSE = 1

# Entrar no Chrome
pa.press("win")
pa.write("chrome")
pa.press("enter")

# Entrar no Youtube
pa.write("https://www.youtube.com/@netenho1")
pa.press("enter")

import time as t

# Escolher vídeo mais novo
t.sleep(2)
pa.click(x=553, y=888)
t.sleep(8)
print(pa.position())

