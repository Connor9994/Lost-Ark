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
MoveTime = time.time() - 5

Healing = 1
Fighting = 0
Moving = 0

# creating tkinter window
base = Tk()
#screen's length and width in pixels
height= base.winfo_screenheight() #During coding: 1920
width= base.winfo_screenwidth()   #During coding: 1080

while True:
    #Escape Code Button
    if keyboard.is_pressed('['):
        break

    try:
        image = pyautogui.screenshot()
        image.save("Screen.png")
        #minimapImage = pyautogui.screenshot(region=(1578, 42,312,270))
        #minimapImage.save("Minimap.png")
        Chaos_Dungeon = cv2.imread("Chaos_Dungeon.png")
        Leave = cv2.imread("Leave.png")
        #OK = cv2.imread("OK.png")
        #OK_Big = cv2.imread("OK_Big.png")
        Matchmaking = cv2.imread("Matchmaking.png")
        Accept = cv2.imread("Accept.png")
        #Ally3 = cv2.imread("3.png")
        Screen = cv2.imread("Screen.png")
        #Minimap = cv2.imread("Minimap.png")
        Full = cv2.imread("Small_Image2.png")
        Empty = cv2.imread("Small_Image.png")
        NextArea = cv2.imread("NextArea.png")

        res1 = cv2.matchTemplate(Screen, Chaos_Dungeon, cv2.TM_CCOEFF_NORMED)
        res2 = cv2.matchTemplate(Screen, Leave, cv2.TM_CCOEFF_NORMED)
        #res3 = cv2.matchTemplate(Screen, OK, cv2.TM_CCOEFF_NORMED)
        #res4 = cv2.matchTemplate(Screen, OK_Big, cv2.TM_CCOEFF_NORMED)
        res5 = cv2.matchTemplate(Screen, Matchmaking, cv2.TM_CCOEFF_NORMED)
        res6 = cv2.matchTemplate(Screen, Accept, cv2.TM_CCOEFF_NORMED)

        #res7 = cv2.matchTemplate(Minimap, Ally3, cv2.TM_CCOEFF_NORMED)

        res11 = cv2.matchTemplate(Screen, Full, cv2.TM_CCOEFF_NORMED)
        res12 = cv2.matchTemplate(Screen, Empty, cv2.TM_CCOEFF_NORMED)
        res13 = cv2.matchTemplate(Screen, NextArea, cv2.TM_CCOEFF_NORMED)

        threshold = .8
        loc1 = np.where(res1 >= threshold)
        loc2 = np.where(res2 >= threshold)
        #loc3 = np.where(res3 >= threshold)
        #loc4 = np.where(res4 >= threshold)
        loc5 = np.where(res5 >= threshold)
        loc6 = np.where(res6 >= threshold)

        #loc7 = np.where(res7 >= .45)

        loc11 = np.where(res11 >= threshold)
        loc12 = np.where(res12 >= threshold)
        loc13 = np.where(res13 >= threshold)
        TotalX = 0
        TotalY = 0
        Length = 0

        BadX = 0
        BadY = 0
        BadLength = 0 

        breakout = 0
        TargetsX = []
        TargetsY = []

        #Leave Dungeon
        First = 1 
        for pt in zip(*loc13[::-1]):
            if First == 1:
                Fighting = 1
                First = 0
                #Decline
                autoit.mouse_click("left",round(0.526*width), round(0.577*height))
                time.sleep(0.25)
                #Leave
                autoit.mouse_click("left",round(0.069*width), round(0.27*height))
                #Yes
                autoit.mouse_click("left",round(0.473*width), round(0.545*height))

        #Accept
        First = 1 
        for pt in zip(*loc6[::-1]):
            if First == 1:
                Fighting = 1
                First = 0
                autoit.mouse_click("left",round(0.469*width), round(0.575*height))

        #Healthbar Full
        for pt in zip(*loc11[::-1]):
            if (pt[1] < (height-20)):
                w, h = Full.shape[:-1]
                cv2.rectangle(Screen, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 1)
                BadX = BadX + pt[0]
                BadY = BadY + pt[1]
                BadLength = BadLength + 1
                Fighting = 1

        #Healthbar Empty
        for pt in zip(*loc12[::-1]):
            if (pt[1] < (height-20)):
                w, h = Empty.shape[:-1]
                cv2.rectangle(Screen, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 1)
                BadX = BadX + pt[0]
                BadY = BadY + pt[1]
                BadLength = BadLength + 1
                Fighting = 1

        #Chaos_Dungeon
        First = 1 
        for pt in zip(*loc1[::-1]):
            if First == 1:
                First = 0
                autoit.mouse_click("left",pt[0],pt[1]+200)

        #Matchmaking
        First = 1    
        for pt in zip(*loc5[::-1]):
            if First == 1:
                autoit.mouse_click("left",435, 367)
                First = 0
                autoit.mouse_click("left",pt[0],pt[1])
                Fighting = 1
                time.sleep(1)
        
        #OK
        #First = 1 
        #for pt in zip(*loc3[::-1]):
            #if First == 1:
                #First = 0
                #Fighting = 0
                #autoit.mouse_click("left",pt[0],pt[1])

        #First = 1    
        #OK_Big
        #for pt in zip(*loc4[::-1]):
            #if First == 1:
                #First = 0
                #autoit.mouse_click("left",pt[0],pt[1])
                #time.sleep(1)
                #autoit.mouse_click("left",203, 298)
                #time.sleep(1)
                #autoit.mouse_click("left",904, 594)

        #Ally Triangle 3
        #for pt in zip(*loc7[::-1]):
            #print("1 Found")
            #w, h = Ally3.shape[:-1]
            #cv2.rectangle(Minimap, pt, (pt[0] + h, pt[1] + w), (255, 0, 0), 1)
            #TotalX = TotalX + pt[0]
            #TotalY = TotalY + pt[1]
            #Length = Length  + 1
            #Moving = 1

        cv2.imwrite('result.png', Screen)
        #cv2.imwrite('resultMinimap.png', Minimap)
    except Exception as e:
        print("0 Detected")
        print(e)

    HighX = 0.088*width
    LowX = 0.075*width
    HighY = 0.118*height
    LowY = 0.131*height

    if (Moving == 1):
        if (Length != 0):
            if (time.time() - MoveTime > 5):
                if (TotalY/Length > LowY):
                    if (TotalX/Length > HighX):
                        #Walk down right
                        autoit.mouse_move(1221, 808,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                    elif (TotalX/Length < HighX and TotalX/Length > LowX):
                        #Walk down
                        autoit.mouse_move(963, 600,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                    elif (TotalX/Length < LowX):
                        #Walk down left
                        autoit.mouse_move(500, 600,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                elif (TotalY/Length < LowY and TotalY/Length > HighY):
                    if (TotalX/Length > HighX):
                        #Move Right
                        autoit.mouse_move(1267, 525 ,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                    elif (TotalX/Length < HighX and TotalX/Length > LowX):
                        #Don't Move
                        time.sleep(0.01)
                    elif (TotalX/Length < LowX): 
                        #Move Left
                        autoit.mouse_move(694, 508 ,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")    
                elif (TotalY/Length < HighY):
                    if (TotalX/Length > HighX):
                        #Walk up right
                        autoit.mouse_move(1200, 350 ,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                    elif (TotalX/Length < HighX and TotalX/Length > LowX):
                        #Walk up
                        autoit.mouse_move(949, 297,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                    elif (TotalX/Length < LowX):
                        #Walk up left
                        autoit.mouse_move(724, 268,10)
                        autoit.mouse_down("left")
                        time.sleep(1.00)
                        autoit.mouse_up("left")
                MoveTime = time.time()
                continue


    start = time.time()    
    if (Healing == 1):
        while True:
            try:
                #Found red
                coords = autoit.pixel_search(round(0.411*width), round(0.888*height), 5, 5, 0x860202)
                newtime = time.time()
                delta = newtime - start
                if (delta < 0.25):
                    break
            except:
                #Failed to find red
                newtime = time.time()
                delta = newtime - start
                if (delta > 0.25):
                    autoit.send("{F1}")
                    break

    if (Fighting == 1):                
        if (BadLength != 0):
            if (time.time() - LastA > 23*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                time.sleep(0.5)
                autoit.send("a")
                LastA = time.time()
                time.sleep(1.5)
                continue
        if (BadLength != 0):
            if (time.time() - LastS > 23*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                autoit.send("{s down}")
                time.sleep(1.35)
                autoit.send("{s up}")
                LastS = time.time()
                time.sleep(1.5)
                continue
        if (BadLength != 0):
            if (time.time() - LastF > 21*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                autoit.send("f")
                LastF = time.time()
                time.sleep(1.5)
                continue

        if (BadLength != 0):
            if (time.time() - LastD > 31*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
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

        if (BadLength != 0):
            if (time.time() - LastQ > 31*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("q")
                time.sleep(2.5)
                autoit.send("z")
                time.sleep(0.5)
                LastQ = time.time()
                continue

        if (BadLength != 0):
            if (time.time() - LastW > 25*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("w")
                time.sleep(1.5)
                autoit.send("z")
                time.sleep(0.5)
                LastW = time.time()
                continue
    
        if (BadLength != 0):
            if (time.time() - LastE > 29*.95):
                autoit.mouse_move(round(BadX/BadLength),round(BadY/BadLength),10)
                autoit.send("x")
                time.sleep(1)
                autoit.send("e")
                time.sleep(1.5)
                autoit.send("z")
                time.sleep(0.5)
                LastE = time.time()
                continue