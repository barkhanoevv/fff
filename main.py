import pyautogui
import time
from pynput.keyboard import *


delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def main():

    lis = Listener(on_press=on_press)
    lis.start()

    while running:
        if not pause:
            pyautogui.click(x=32, y=182)
            time.sleep(1)
            pyautogui.click(x=1403, y=465)
            time.sleep(1)
            pyautogui.click(x=1269, y=549)
    lis.stop()

if __name__ == "__main__":
    main()











    #pyautogui.FAILSAFE = False
    #time.sleep(3)
    #1.Point(x=32, y=182)
    # 1.Point(x=1403, y=465)
    # 1.Point(x=1269, y=549)
    #xy = pyautogui.position()
    #print (xy)



