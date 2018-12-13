import pyautogui, pywinauto, pyhooked, time, threading, datetime, sys, random

#
# cursorpos = win32gui.GetCursorPos()
# print(cursorpos)
# pyautogui.mouseDown(None, None, 'left')
# pyautogui.mouseUp(None, None, 'left')
#
# print(cursorpos[0])
# print(cursorpos[1])
# print(cursorpos[1:])
start_time = datetime.datetime.now()
activity_tracker = []

def handle_event(args):
    current_time = datetime.datetime.now()
    delta = current_time - start_time
    time = delta.seconds + delta.microseconds/1000000

    if isinstance(args, pyhooked.KeyboardEvent):
        print(args.key_code)
        if args.current_key == 'A' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print("Ctrl + A was pressed")
        elif args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            myhook.unhook_mouse()
            myhook.unhook_keyboard()
            myhook.stop()
            print('Quitting.')


    if isinstance(args, pyhooked.MouseEvent):
        if args.event_type == "key down":
            x, y = pyautogui.position()
            try:
                print(time)
                print("("+ str(x) + ", " + str(y) + ")" + "  " + str(time-activity_tracker[-1][1]))
            except IndexError as e:
                print("(" + str(x) + ", " + str(y) + ")" + "  " + str(time))

            if len(activity_tracker)==0:
                activity_tracker.append([(x, y), time])
            else:
                activity_tracker.append([(x, y), time])


def wait():
    time.sleep(10)
    myhook.unhook_mouse()
    return

# mythread = threading.Thread(target=wait)
# mythread.daemon=True

print(1)
myhook = pyhooked.Hook()
myhook.handler = handle_event
print(1)
myhook.hook(keyboard=True, mouse=True)
# activity_tracker = activity_tracker[:len(activity_tracker)-2]
print(1)
print(activity_tracker)
# mythread.start()

def rand_mouse_coord(coordinate):
    x_original = coordinate[0]
    y_original = coordinate[1]
    x = random.randint(x_original - 10, x_original + 10)
    y = random.randint(y_original - 10, y_original + 10)
    return (x,y)

def rand_time(time):
    if time < 10:
        mult = random.randint(0,100)
    else:
        mult = random.randint(0,30)
    return time * ( 1 + mult/50)

while True:
    new_activity_list = []
    for i in range(len(activity_tracker)):
        if i != 0:
            new_activity_list.append([rand_mouse_coord(activity_tracker[i][0]), rand_time(activity_tracker[i][1] - activity_tracker[i-1][1])])
        else:
            new_activity_list.append( [rand_mouse_coord(activity_tracker[i][0]), 0])
    print(new_activity_list)
    for activity in new_activity_list:
        move_duration = random.randint(1, 4) / 10
        time.sleep(activity[1])
        pyautogui.moveTo(activity[0][0], activity[0][1])
        pyautogui.click()
    time.sleep(random.randint(1, 120))