import pyautogui as py
import time


def writing_sec_name():
   # Now entering text in the box
    py.press('B')
    py.press('C')
    py.press('S')
    py.press('-')
    py.press('5')
    py.press('B')


def Selecting_and_opening_menu():
    time.sleep(2)
    py.hotkey('ctrl', 'a')

    # conditional formatting coordinates are (557,74)
    py.moveTo(557, 74)
    py.click()

    # highlight cell rules coordinates are (554,115)
    py.moveTo(554, 115)
    py.click()

    # text that contains coordinates are (795,293)
    py.sleep(1)
    py.moveTo(795, 293)
    py.click()
    writing_sec_name()


def Conditional_Formating_conditions():

    # Selecting modifiction menu coordinates are (565,492)
    py.moveTo(565, 492)
    py.click()

    # custom format coordinates are (532.586)
    py.moveTo(532, 586)
    py.click()

    # selecing the Fill Tab coordinates are (351,229)
    py.moveTo(351, 229)
    py.click()

    # red color coordiantes are (223,428)
    py.moveTo(332, 304)
    py.click()

    # the okay button coordinates are (576,681)
    py.moveTo(576, 681)
    py.click()

    # the other okay button coordinates are (566,524)
    py.moveTo(566, 524)
    py.click()
    py.click()


def highlight():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday']
    for i in days:
        print("Highlighting "+i+" currently.")
        # clikcing on the document
        py.click(497, 522)
        Selecting_and_opening_menu()
        Conditional_Formating_conditions()
        py.hotkey('ctrl', 'pagedown')
    print("Now saving the work done...")
    time.sleep(1)
    py.hotkey('ctrl', 's')
    print("Closing the file...")
    time.sleep(1)
    py.hotkey('alt', 'f4')


highlight()
