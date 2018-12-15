import pyautogui
import time
import random


class Macro(object):
    def __init__(self, exe):
        self.exe = exe
        pass

    def start_macro(self):
        Macro.locate_and_click("pics/combat.png")
        Macro.locate_and_click("pics/huntingrabbit.png")
        Macro.locate_and_click("pics/saintelmore.png")
        Macro.locate_and_click("pics/normal_combat.png")
        cc_x, cc_y = Macro.locate_and_click("pics/saintelmore_cc.png")
        Macro.locate_and_click("pics/decide.png")
        Macro.locate_and_click("pics/mission_start.png")
        Macro.random_click(cc_x, cc_y)

    def start_mission(self):
        pass
        # for turn in self.exe:
        #     self.execute(turn)

    @staticmethod
    def execute(turn):
        x, y = pyautogui.locateCenterOnScreen("pics/planned_mode.png")
        x, y = Macro.vary_random(x, y)
        pyautogui.moveTo(x, y, 0.5)

    @staticmethod
    def wait_plan():
        found = False
        while not found:
            found = Macro.cont_find("pics/planned_mode.png")
            time.sleep(1)
        return

    @staticmethod
    def cont_find(img):
        found = False
        while not found:
            img2 = pyautogui.screenshot()
            found = pyautogui.locate(img, img2)

        return found

    @staticmethod
    def vary_random(x, y):
        rx = random.randint(-5, 5) + x
        ry = random.randint(-5, 5) + y

        return rx, ry

    @staticmethod
    def random_click(x, y):
        rx, ry = Macro.vary_random(x, y)
        pyautogui.click(rx, ry)

    @staticmethod
    def locate_and_click(img):
        found = False
        while not found:
            found = pyautogui.locateCenterOnScreen(img)
        x, y = found
        x, y = Macro.vary_random(x,y)
        pyautogui.click(x,y)
        return found


if __name__ == "__main__":
    time.sleep(1)
    mac = Macro("")
    mac.start_macro()