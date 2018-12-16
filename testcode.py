import pyautogui
import time


while 1:
    time.sleep(1)
    print(pyautogui.locateCenterOnScreen("pics/enemy_pod.png"))
    print(pyautogui.locateCenterOnScreen("pics/enemy_pod_left.png"))