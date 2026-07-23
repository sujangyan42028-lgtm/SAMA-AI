import pyautogui

pyautogui.FAILSAFE = True

def click(x, y):
    pyautogui.click(x, y)
    return "Clicked."

def move(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    return "Mouse moved."

def write(text):
    pyautogui.write(text, interval=0.05)
    return "Typing completed."