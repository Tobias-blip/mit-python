import pyautogui, time
time.sleep(5) 
f = open("html.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
