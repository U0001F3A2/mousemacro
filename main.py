import pyautogui
import time

class Macro(object):
    def __init__(self, exec):
        self.exec = exec
        pass

    @staticmethod
    def wait_plan():
        found = False
        while not found:
            found = Macro.cont_find("pics/planned_mode.jpg")
            time.sleep(1)
        return

    @staticmethod
    def cont_find(img):
        found = False
        while not found:
            img2 = pyautogui.screenshot()
            found = pyautogui.locate(img, img2)

        return found
