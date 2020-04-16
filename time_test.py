#import win32com.client #pip install pywin32 if not installed
#import math
import time
#import PySimpleGUI as sg
#import pygame as pg
#from pywintypes import com_error

## [Attribute error:](https://stackoverflow.com/questions/54781947/attributeerror-datetime-time-object-has-no-attribute-time)

# Figure out how to print out time differences in Python:

if __name__ == '__main__':
    print('in main')
    import math
    import time as t
    x = math.inf
    counter = 0
    start=t.time()
    print(start)
    # while True:
    #     print('in-loop')
    #     print(f"start: {start} ")
    #     # not resetting
    #     if t.time() - start >= 59:
    #         counter = 0
    #     # get time
    #     start = t.time()
    #     counter +=1
    #     # see where its at
    #     print(f"counter: {counter}")

