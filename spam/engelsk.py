import pyautogui, time
time.sleep(5) 
f = open("engelsktxt.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("backspace")
    pyautogui.press("space")