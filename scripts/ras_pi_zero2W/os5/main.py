# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:22:43 2024

@author: admin
"""

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
    draw0=Draw(height=screen.height,width=screen.width)
    draw1=Draw(height=screen.height,width=screen.width)
    draw2=Draw(height=screen.height,width=screen.width)
    
    
    '''
    PLEASE RESPECT THE SYNTAX FOR GPIO PIN ASSIGHMENT
    '''
    camera=Camera()
    button=Button(pin=3)
    molette=RotaryEncoder(clk_pin=board.D27, dt_pin=board.D22)
    
    # Initialize the menu
    menu = Menu(screen, draw0,draw1,draw2,molette, button,camera)
    
    '''
    CHANGE THESE ACCORDING TO YOUR SYSTEM
    '''
    
    
    # Add menu items
    menu.add_item("1 min",wfps=10,dimensions=(800,448),char='@ W I D E  V G A ',mode= 'S L O W  M O T I O N')
    menu.add_item("5 min",wfps=22,dimensions=(800,600),char='@ S U P E R   V G A ',mode='N O R M A L')
    menu.add_item("30 min",wfps=28,dimensions=(800,448),char='@ W I D E  V G A ',mode='E C O  -  N O R M A L')

    menu.add_item("1 h",wfps=100,dimensions=(1920,1080),char='@ F U L L  H D' ,mode=' T I M E - L A P S E ')

    menu.add_item("3 h",wfps=600,dimensions=(1280,720),char='@ H D',mode='E C O  -  T I M E - L A P S E ')
    
    
    menu.menu_0()
    menu.menu_1()
    menu.menu_3()

    
    # Start the menu control loop
    while True:
        menu.menu_control()
        
    
if __name__ == "__main__":
    print('we are on')
    main()
