# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time 
import pyautogui   

time.sleep(1)

#Login VPN  
pyautogui.moveTo(460, 1050, duration = 1)
pyautogui.click()
pyautogui.moveTo(100, 100, duration = 1)
pyautogui.click()
time.sleep(1)

#Get OneTimePassword
pyautogui.moveTo(510, 1050, duration = 1)
pyautogui.click()
pyautogui.moveTo(510, 1050, duration = 1)
pyautogui.click()
pyautogui.moveTo(510, 1050, duration = 1)
pyautogui.click()
pyautogui.moveTo(510, 1050, duration = 1)
pyautogui.click()

#Insert Onetime Password
pyautogui.moveTo(560, 1050, duration = 1)
pyautogui.click()

#Open Teams
pyautogui.moveTo(610, 1050, duration = 1)
pyautogui.click()

#Open chrome for hours sheet
pyautogui.moveTo(660, 1050, duration = 1)
pyautogui.click()

#Open notepad++
pyautogui.moveTo(710, 1050, duration = 1)
pyautogui.click()
#pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
#pyautogui.click() # Click the mouse at its current location.
#pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
#pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
#pyautogui.doubleClick() # Double click the mouse at the
#pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
#pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
#pyautogui.press('esc') # Simulate pressing the Escape key.
#pyautogui.keyDown('shift')
#pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
#pyautogui.keyUp('shift')
#pyautogui.hotkey('ctrl', 'c')
#pyautogui.alert('This is an alert box.')
#pyautogui.confirm('Shall I proceed?')
#pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
#pyautogui.prompt('What is your name?')
#pyautogui.password('Enter password (text will be hidden)')