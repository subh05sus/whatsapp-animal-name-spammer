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
    pyautogui.write(a+ " is a "+ items, interval = 0.1)
    pyautogui.press("enter")

