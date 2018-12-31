import pyautogui
import time
import random


class Macro(object):
    def __init__(self, exe):
        self.exe = exe
        pass

    def start_0_2(self):
        laclick = Macro.locate_and_click
        rand_click = Macro.random_click
        laclick("pics/combat.png")
        if pyautogui.locateOnScreen("pics/0-2/field_0.png"):
            laclick("pics/0-2/field_0.png")
        laclick("pics/0-2/0-2.png")
        laclick("pics/0-2/normal_combat.png")

        ccx, ccy = laclick("pics/0-2/cc.png")
        laclick("pics/decide.png")
        laclick("pics/0-2/heliport.png")
        laclick("pics/decide.png")
        rand_click(ccx + 500, ccy + 300)

        #mission go!
        time.sleep(3)
        while not pyautogui.locateOnScreen("pics/plan_white.png"):
            Macro.random_sleep()
            continue
        p_x, p_y = Macro.cont_find("pics/0-2/neutral_pad.png")

        p1_x, p1_y = p_x - 150, p_y + 150

        p2_x, p2_y = p_x - 310, p_y + 55

        p3_x, p3_y = p_x - 270, p_y - 153

        laclick("pics/plan_white.png")
        rand_click(p1_x, p1_y)
        rand_click(p2_x, p2_y)
        rand_click(p3_x, p3_y)
        laclick("pics/plan_execute.png")
        Macro.wait_plan()

        laclick("pics/0-2/cc2.png")
        laclick("pics/decide.png")
        laclick("pics/turn_end2.png")
        Macro.wait_turn()

        # turn 2
        time.sleep(3)
        while not pyautogui.locateOnScreen("pics/plan_white.png"):
            Macro.random_sleep()
            continue
        exx, exy = Macro.cont_find("pics/0-2/ex.png")

        p1_x, p1_y = exx + 235, exy + 320
        p2_x, p2_y = exx + 2, exy + 250
        p3_x, p3_y = exx + 118, exy + 121
        p4_x, p4_y = exx + 249, exy + 30
        p5_x, p5_y = exx + 510, exy + 13
        p6_x, p6_y = exx + 713, exy + 41
        laclick("pics/plan_white.png")
        rand_click(p1_x, p1_y)
        rand_click(p2_x, p2_y)
        rand_click(p3_x, p3_y)
        rand_click(p4_x, p4_y)
        rand_click(p5_x, p5_y)
        rand_click(p6_x, p6_y)
        laclick("pics/plan_execute.png")
        Macro.wait_plan()

        laclick("pics/turn_end.png")
        Macro.end_and_return()
        Macro.repair()
        Macro.recycle()

    @staticmethod
    def start_saintelmore():
        laclick = Macro.locate_and_click
        rand_click = Macro.random_click
        laclick("pics/combat.png")
        laclick("pics/saintelmore/huntingrabbit.png")
        laclick("pics/saintelmore/saintelmore.png")
        laclick("pics/normal_combat.png")
        cc_x, cc_y = laclick("pics/saintelmore/saintelmore_cc.png")
        laclick("pics/decide.png")
        # laclick("pics/mission_start.png")
        rand_click(cc_x + 300, cc_y + 200)
        # turn 1
        time.sleep(3)
        while not pyautogui.locateOnScreen("pics/plan_white.png"):
            Macro.random_sleep()
            continue
        h_x, h_y = Macro.cont_find("pics/saintelmore/saintelmore_heliport_neutral.png")

        # command center
        cc_x, cc_y = h_x -220, h_y + 70

        # first move pod
        cc1_x, cc1_y = h_x - 230, h_y - 145

        # second move pod
        cc2_x, cc2_y = h_x - 335, h_y + 10

        # third move pod
        cc3_x, cc3_y = h_x - 500, h_y - 45
        laclick("pics/plan_white.png")
        rand_click(cc_x, cc_y)
        rand_click(cc1_x, cc1_y)
        laclick("pics/plan_execute.png")
        Macro.wait_plan()

        # udpate helipad
        h_x, h_y = Macro.cont_find(["pics/saintelmore/saintelmore_heliport_neutral2.png",
                                    "pics/saintelmore/saintelmore_heliport_neutral3.png"])

        # command center
        cc_x, cc_y = h_x -220, h_y + 70
        rand_click(cc_x, cc_y)
        laclick("pics/decide.png")
        laclick("pics/turn_end.png")
        Macro.wait_turn()

        # turn 2
        time.sleep(5)
        # update helipad location
        h_x, h_y = Macro.cont_find(["pics/saintelmore/saintelmore_heliport_neutral2.png",
                                    "pics/saintelmore/saintelmore_heliport_neutral3.png"])

        # command center
        cc_x, cc_y = h_x -220, h_y + 70

        # first move pod
        cc1_x, cc1_y = h_x - 230, h_y - 145

        # second move pod
        cc2_x, cc2_y = h_x - 335, h_y + 10

        # third move pod
        cc3_x, cc3_y = h_x - 500, h_y - 45

        # fourth move pod
        cc4_x, cc4_y = h_x - 210, h_y - 315

        while pyautogui.locateOnScreen("pics/plan_white.png") and not pyautogui.locateOnScreen("pics/plan_active.png"):
            laclick("pics/plan_white.png")
        rand_click(cc_x, cc_y)
        if pyautogui.locateOnScreen("pics/plan_white.png"):
            laclick("pics/plan_white.png")
        rand_click(cc2_x, cc2_y)
        rand_click(cc3_x, cc3_y)

        rand_click(cc1_x, cc1_y)
        rand_click(cc4_x, cc4_y)
        laclick("pics/plan_execute.png")
        Macro.wait_plan()
        laclick("pics/turn_end.png")
        Macro.wait_turn()

        time.sleep(3)
        epl_x, epl_y = Macro.cont_find("pics/saintelmore/enemy_pod_left.png")
        ep_x, ep_y = epl_x + 50, epl_y + 60

        m_x, m_y = ep_x + 160, ep_y + 270

        m1_x, m1_y = ep_x + 65, ep_y + 120

        m2_x, m2_y = ep_x - 150, ep_y - 70

        while pyautogui.locateOnScreen("pics/plan_white.png") and not pyautogui.locateOnScreen("pics/plan_active.png"):
            laclick("pics/plan_white.png")
        rand_click(m_x, m_y)
        if pyautogui.locateOnScreen("pics/plan_white.png"):
            laclick("pics/plan_white.png")
        rand_click(m1_x, m1_y)
        rand_click(ep_x, ep_y)
        rand_click(m2_x, m2_y)
        laclick("pics/plan_execute.png")
        Macro.wait_plan()
        if pyautogui.locateCenterOnScreen("pics/turn_end2.png"):
            laclick("pics/turn_end2.png")
        else:
            laclick("pics/turn_end.png")

        Macro.end_and_return()
        Macro.recycle()

    @staticmethod
    def repair():
        laclick = Macro.locate_and_click
        laclick("pics/repair.png")
        laclick("pics/add_repair.png")
        p_x, p_y = Macro.cont_find("pics/repair_plus.png")
        for i in range(4):
            Macro.random_click(p_x - 100 + i * 175, p_y + 190)
        laclick("pics/repair_check.png")
        laclick("pics/repair_check2.png")
        while not Macro.test_repair():
            time.sleep(1)
        laclick("pics/return_base.png")

    @staticmethod
    def test_repair():
        return pyautogui.locateOnScreen("pics/repair_iop1.png") and \
               pyautogui.locateOnScreen("pics/repair_iop2.png") and \
               pyautogui.locateOnScreen("pics/repair_slot1_empty.png") and \
               not pyautogui.locateOnScreen("pics/repair_slot_empty_err.png")

    @staticmethod
    def end_and_return():
        Macro.cont_find("pics/mission_end_eval.png")
        pyautogui.click()
        x, y = Macro.cont_find("pics/nox.png")
        while not pyautogui.locateOnScreen("pics/return_base.png"):
            if pyautogui.locateOnScreen("pics/mission_back.png"):
                Macro.locate_and_click("pics/mission_back.png")
                break
            pyautogui.click()
            Macro.random_sleep(2000)
        Macro.locate_and_click("pics/return_base.png")

    @staticmethod
    def recycle():
        laclick = Macro.locate_and_click
        laclick("pics/factory.png")
        laclick("pics/tdoll_retire.png")
        laclick("pics/tdollretire_choose.png")
        laclick("pics/tdollretirechoose_2star.png")
        laclick("pics/tdollretire_decide.png")
        laclick("pics/tdoll_retire_confirm.png")
        laclick("pics/return_base.png")


    def start_mission(self):
        pass
        # for turn in self.exe:
        #     self.execute(turn)

    @staticmethod
    def execute(turn):
        x, y = pyautogui.locateCenterOnScreen("pics/plan_white.png")
        x, y = Macro.vary_random(x, y)
        pyautogui.moveTo(x, y, 0.5)

    @staticmethod
    def wait_plan():
        found = False
        while not found:
            found = pyautogui.locateOnScreen("pics/plan_white.png")
            time.sleep(1)
        return

    @staticmethod
    def wait_turn():
        found = False
        while not found:
            if pyautogui.locateCenterOnScreen("pics/star_battleend.png") or not pyautogui.locateCenterOnScreen("pics/turn.png"):
                pyautogui.click()
            found = pyautogui.locateOnScreen("pics/turn_end.png")
            if not found:
                found = pyautogui.locateOnScreen("pics/turn_end2.png")
        return

    @staticmethod
    def vary_random(x, y):
        rx = random.randint(-5, 5) + x
        ry = random.randint(-5, 5) + y

        return rx, ry

    @staticmethod
    def random_click(x, y, random_sleep=True):
        rx, ry = Macro.vary_random(x, y)
        pyautogui.click(rx, ry)
        if random_sleep:
            Macro.random_sleep()

    @staticmethod
    def locate_and_click(img):
        found = Macro.cont_find(img)
        x, y = found
        x, y = Macro.vary_random(x,y)
        pyautogui.click(x,y)
        return found

    @staticmethod
    def random_sleep(max_time=500):
        t = random.randint(1, max_time)
        t = t / 1000
        time.sleep(t)

    @staticmethod
    def cont_find(img):
        found = False
        while not found:
            screen = pyautogui.screenshot()
            if type(img) is list:
                for i in img:
                    found = pyautogui.locate(i, screen)
                    if found:
                        break
            else:
                found = pyautogui.locate(img, screen)
            print("failed to find ", img)
        found = Macro.convert_to_center(found)
        return found

    @staticmethod
    def convert_to_center(coord):
        return coord[0] + coord[2]/2 , coord[1] + coord[3]/2


if __name__ == "__main__":
    time.sleep(1)
    mac = Macro("")
    while True:
        mac.start_0_2()
