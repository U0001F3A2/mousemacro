import pyautogui, win32gui

cursorpos = win32gui.GetCursorPos()
print(cursorpos)
pyautogui.mouseDown(None,None,'left')
pyautogui.mouseUp(None,None,'left')

print(cursorpos[0])
print(cursorpos[1])
print(cursorpos[1:])

def main():
    pass