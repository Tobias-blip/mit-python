import pyautogui, time
time.sleep(5) 
f = open("mortxt.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.8)