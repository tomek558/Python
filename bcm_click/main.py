from tkinter import *
import pyautogui
import time


def clicker():
    #print(pyautogui.position())
    time.sleep(0.5)
    pyautogui.moveTo(397,551)
    pyautogui.doubleClick()
    pyautogui.click(1023,709)
    pyautogui.click(830,740)
    pyautogui.click(379,769)
    pyautogui.doubleClick(426,885)

window = Tk()
window.title('kliker')
window.geometry("200x100")

click_button = Button(window, text="Start", command=clicker)
click_button.place(relx=0.5, rely=0.5, anchor=CENTER)
window.mainloop()

#prosty kliker którego zrobiłem przy zdalnej pracy, wykorzystywałem go w menagerze paczek inpost





