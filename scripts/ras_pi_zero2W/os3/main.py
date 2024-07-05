# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:22:43 2024

@author: admin
"""
import cv2 as cv
from datetime import datetime
import os
import time
from button import Button
from rotary_encoder import RotaryEncoder
from screen import Screen
from draw import Draw
from menu import Menu
from camera import Camera
import board



    
def main():
    # Initialize the screen, draw, molette, and button
    screen = Screen()
    draw0=Draw(user_id="user 123",height=screen.height,width=screen.width)
    draw1=Draw(user_id="user 123",height=screen.height,width=screen.width)
    draw2=Draw(user_id="user 123",height=screen.height,width=screen.width)
    camera=Camera()
    button=Button(pin=4)
    molette=RotaryEncoder(clk_pin=board.D27, dt_pin=board.D22)
    
    # Initialize the menu
    menu = Menu(screen, draw0,draw1,draw2, molette, button,camera)
    
    # Add menu items
    menu.add_item("C A M E R A    S P E E D", (80, 50))
    menu.add_item("C A L I B R A T E   P O S I T I O N ", (80, 70))
    menu.add_item("R E C O R D", (80, 90))
    menu.menu_0()
    menu.menu_1()
    menu.menu_3()
    #draw.clear_img()

    
    # Start the menu control loop
    while True:
        menu.menu_control()
        
    
if __name__ == "__main__":
    print('we are on')
    main()