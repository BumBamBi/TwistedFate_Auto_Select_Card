import keyboard
import pyautogui
import time 
import math

while(1):
    # 추후에 컨트롤w로 변경
    if keyboard.is_pressed('ctrl+v'):  
        start = time.time()
        break


print(round((time.time() - start),1))

i = 0
while(1):
    if ((round((time.time() - start),1))%0.5 == 0):
        time.sleep(0.5)
        i = (i + 1)%3

    # if press z
    #   


# keyboard.press('w')start