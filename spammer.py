import time
import pyautogui

animal=[]

a=input("What is the victim name ?: ")
print("Open whatsapp or other messaging app in 5 secs")
time.sleep(2)
vowel = "aeiou"


f = open('animals.txt','r')

for line in f:
    animal.append(line.strip())


def vowelStart(s):
    if(s[0]=="A" or s[0]=="E" or s[0]=="I" or s[0]=="O" or s[0]=="U"):
        return True
    return False

pyautogui.FAILSAFE = False

for items in animal:
    if vowelStart(items):
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
