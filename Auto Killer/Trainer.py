import tkinter
import autoit
import time
import pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import os
from tkinter import *

LastQ = time.time() - 31
LastW = time.time() - 25
LastE = time.time() - 29

LastA = time.time() - 23
LastS = time.time() - 23
LastF = time.time() - 21
LastD = time.time() - 31

Repair = time.time()

Healing = 1

# creating tkinter window
base = Tk()
#screen's length and width in pixels
height= base.winfo_screenheight() #During coding: 1920
width= base.winfo_screenwidth()   #During coding: 1080

while True:
    #Escape Code Button
    if keyboard.is_pressed('['):
        break

    image = pyautogui.screenshot()
    try:
        image.save("Screen.png")
        HealthbarEmpty = cv2.imread("Small_Image.png")
        HealthbarFull = cv2.imread("Small_Image2.png")
        BaseRessurect = cv2.imread("Base_ressurect.png")
        LoginEvent = cv2.imread("Login_Event.png")

        Screen = cv2.imread("Screen.png")
        res1 = cv2.matchTemplate(Screen, HealthbarEmpty, cv2.TM_CCOEFF_NORMED)
        res2 = cv2.matchTemplate(Screen, HealthbarFull, cv2.TM_CCOEFF_NORMED)
        res3 = cv2.matchTemplate(Screen, BaseRessurect, cv2.TM_CCOEFF_NORMED)
        res4 = cv2.matchTemplate(Screen, LoginEvent, cv2.TM_CCOEFF_NORMED)
        w, h = HealthbarFull.shape[:-1]
        threshold = .6
        loc1 = np.where(res1 >= threshold)
        loc2 = np.where(res2 >= threshold)
        loc3 = np.where(res3 >= threshold)
        loc4 = np.where(res4 >= .8)
        TotalX = 0
        TotalY = 0
        Length = 0
        breakout = 0
        TargetsX = []
        TargetsY = []

        #Login_Event 5am close out
        First = 1
        for pt in zip(*loc4[::-1]):
            if First == 1:
                autoit.mouse_click("left",1569, 72)
                First = 0
        #Healthbar Empty
        for pt in zip(*loc1[::-1]):
            if (pt[1] < (height-10)):
                cv2.rectangle(Screen, pt, (pt[0] + h, pt[1] + w), (255, 0, 0), 1)
                TotalX = TotalX + pt[0]
                TotalY = TotalY + pt[1] + 100
                Length = Length + 1
                TargetsX.append(pt[0])
                TargetsY.append(pt[1]+100)
        #Healthbar Full
        for pt in zip(*loc2[::-1]):
            if (pt[1] < (height-10)):
                cv2.rectangle(Screen, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 1)
                TotalX = TotalX + pt[0]
                TotalY = TotalY + pt[1] + 100
                Length = Length + 1
                TargetsX.append(pt[0])
                TargetsY.append(pt[1]+100)
        First = 1
        for pt in zip(*loc3[::-1]):
            if First == 1:
                Healing = 1
                First = 0
                print("You are dead")
                time.sleep(5)
                autoit.mouse_click("left",pt[0],pt[1])
                time.sleep(10)
                autoit.send("9")
                time.sleep(20)
                autoit.send("g")
                time.sleep(2)
                autoit.mouse_click("left",round(0.558*width),round(0.396*height))
                time.sleep(1)
                autoit.send("{Esc}")
                time.sleep(2)
                autoit.mouse_click("left",round(0.895*width),round(0.312*height))
                time.sleep(1)
                autoit.mouse_click("left",round(0.767*width),round(0.471*height))
                time.sleep(1)
                autoit.mouse_click("left",round(0.471*width),round(0.600*height))
                time.sleep(5)

        if (breakout == 1):
            #os.system("shutdown /s /t 1")
            break

        print("Average X: " + str(TotalX/Length)) 
        print("Average Y: " + str(TotalY/Length))     
        cv2.imwrite('result.png', Screen)
    except Exception as e:
        print("0 Detected")
        print(e)
        autoit.mouse_move(round(0.546*width),round(0.462*height),10)

    if (time.time() - Repair > 7200):
        Repair = time.time()
        Healing = 0
        autoit.tooltip("Stopped Healing", 0, 0)
        continue

    start = time.time()    
    if (Healing == 1):
        while True:
            try:
                #Found red
                coords = autoit.pixel_search(round(0.411*width), round(0.888*height), 5, 5, 0x860202)
                newtime = time.time()
                delta = newtime - start
                if (delta < 0.1):
                    break
            except:
                #Failed to find red
                newtime = time.time()
                delta = newtime - start
                if (delta > 0.1):
                    autoit.send("{F1}")
                    break

    if (Length != 0):
        if (time.time() - LastA > 23*.95):
            autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
            time.sleep(0.5)
            autoit.send("a")
            LastA = time.time()
            time.sleep(1.5)
            continue
    
    if (Length != 0):
        if (time.time() - LastS > 23*.95):
            autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
            autoit.send("{s down}")
            time.sleep(1.3)
            autoit.send("{s up}")
            LastS = time.time()
            time.sleep(1.5)
            autoit.mouse_move(540, 144 ,10)
            autoit.mouse_down("left")
            time.sleep(0.5)
            autoit.mouse_up("left")
            continue

    if (Length != 0):
        if (time.time() - LastF > 21*.95):
            autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
            autoit.send("f")
            LastF = time.time()
            time.sleep(1.5)
            continue

    if (Length != 0):
        if (time.time() - LastD > 31*.95):
            autoit.mouse_move(TargetsX[0],TargetsY[0],10)
            autoit.send("d")
            time.sleep(1.5)
            autoit.mouse_click("right")
            time.sleep(1.25)
            autoit.mouse_click("right")
            time.sleep(1.25)
            autoit.mouse_click("right")
            time.sleep(1.25)
            autoit.mouse_click("right")
            LastD = time.time()
            continue

    if (Length != 0):
        if (time.time() - LastQ > 31*.95):
            if (round(TotalX/Length) < 1400):
                autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("q")
                time.sleep(2.5)
                autoit.send("z")
                time.sleep(0.5)
                LastQ = time.time()
                continue

    if (Length != 0):
        if (time.time() - LastW > 25*.95):
            if (round(TotalX/Length) < 1400):
                autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("w")
                time.sleep(1.5)
                autoit.send("z")
                time.sleep(0.5)
                LastW = time.time()
                continue
    
    if (Length != 0):
        if (time.time() - LastE > 29*.95):
            if (round(TotalX/Length) < 1400):
                autoit.mouse_move(round(TotalX/Length),round(TotalY/Length),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("e")
                time.sleep(1.5)
                autoit.send("z")
                time.sleep(0.5)
                LastE = time.time()
                continue