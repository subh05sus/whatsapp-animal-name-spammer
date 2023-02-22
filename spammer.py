import time
import pyautogui


a=input("What is the victim name ?: ")
print("Open whatsapp or other messaging app in 5 secs")
time.sleep(5)
animal=[]

f = open('animals.txt','r')

for line in f:
    animal.append(line.strip())

for items in animal:
    if items.startswith("a") or items.startswith("e") or items.startswith("i") or items.startswith("o") or items.startswith("u"):
        pyautogui.write(a+ " is an "+ items, interval = 0.1)
    else:
        pyautogui.write(a+ " is a "+ items, interval = 0.1)
    pyautogui.press("enter")

pyautogui.write("Haha, You'll die fool", interval=0.1)
pyautogui.press("enter")
pyautogui.write("NO OFFENCE", interval=0.1)
pyautogui.press("enter")
pyautogui.write("and also sorry for this :)", interval=0.1)
pyautogui.press("enter")