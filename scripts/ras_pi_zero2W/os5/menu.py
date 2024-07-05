
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:31:42 2024

@author: admin
"""
"""
You will need to modify the positions depending on your screen size
"""
import subprocess

class Menu:
    def __init__(self, screen, draw0, draw1, draw2, molette, button, camera):
        self.screen = screen  # Initialize the screen object
        self.draw0 = draw0    # Drawing object for menu 0
        self.draw1 = draw1    # Drawing object for menu 1
        self.draw2 = draw2    # Drawing object for menu 2 and 3
        self.button = button  # Button object
        self.molette = molette  # Rotary encoder object
        self.camera = camera  # Camera object
        
        self.items = []  # List to store menu items
        self.position = []  # List to store item positions
        self.char = []  # List to store characters
        self.wfps = []  # List to store frames per second settings
        self.dimensions = []  # List to store dimensions
        self.modes = []  # List to store modes
        
        self.temp = 0  # Temporary variable for index comparison
        self.current_index = 1  # Initialize the current index

        self.height = screen.height  # Screen height
        self.width = screen.width  # Screen width

    def add_item(self, name, wfps, dimensions, char, mode):
        self.items.append(name)  # Add item name to items list
        self.wfps.append(wfps)  # Add frames per second setting to wfps list
        self.dimensions.append(dimensions)  # Add dimensions to dimensions list
        self.char.append(char)  # Add character to char list
        self.modes.append(mode)  # Add mode to modes list
        
    def menu_0(self):
        self.draw0.clear_img()  # Clear the image
        self.position = self.draw0.draw_arc_with_text(xy=(17, 40, 147, 135), start=180, end=0, text_list=self.items)
        # Draw arc with text
        self.items.append('C A M   V I E W')  # Append 'C A M V I E W' to items
        self.position.append((80, 90))  # Append position for 'C A M V I E W'
        
        self.draw0.draw_msg('(5400 Img/min)', (40, 115))  # Draw message for 5400 images per minute
        self.draw0.draw_msg('(10 Img/min)', (124, 115))  # Draw message for 10 images per minute
        self.draw0.draw_msg('V I D E O', (80, 64))  # Draw 'VIDEO' message
        self.draw0.draw_msg('C A M   V I E W', (80, 90))  # Draw 'C A M V I E W' message

        self.screen.disp_img(self.draw0.rtrn_img())  # Display the image on screen

    def control_menu_0(self):
        self.molette.set_pos(self.current_index)  # Set the current index position on the molette
        '''uncomment this if you want to test the time taken by the function to be executed'''
        # start=time.time()
        self.current_index = self.molette.update()  # Update the current index
        # react=time.time()-start

        if self.temp != self.current_index:  # If the index has changed
            self.current_index = max(0, self.current_index)  # Ensure the index is within bounds
            self.current_index = min(self.current_index, len(self.items) - 1)
            for i in range(len(self.items)):  # Loop through items
                if i == self.current_index:
                    self.draw0.bound_mssg(self.items[i], self.position[i], color='white')  # Highlight selected item
                else:
                    self.draw0.bound_mssg(self.items[i], self.position[i], color='red')  # Unhighlight other items

            self.screen.disp_img(self.draw0.rtrn_img())  # Display the updated image on screen

            # print('react = ',react)
            # print('current index=',self.current_index)
            # print('temp=',self.temp)
            # print('mollette=',self.molette.position)
            self.temp = self.current_index  # Update the temp index
    
    def menu_1(self):
        self.draw1.clear_img()  # Clear the image with black background
        self.draw1.draw_msg('S H U T T I N G  D O W N', (80, 64))  # Draw shutdown message

    def control_menu_1(self):
        self.screen.disp_img(self.draw1.rtrn_img())  # Display the image on screen
        print("Initiating shutdown...")
        subprocess.call(['sudo', 'shutdown', '-h', 'now'])  # Initiate system shutdown
        self.draw1.draw.rectangle([0, 0, self.height, self.width], fill=(0,0,0))  # Clear the image with black background
        self.screen.disp_img(self.draw1.rtrn_img())
        
    def menu_2(self):
        pass  # Placeholder for menu 2 implementation
    
    def control_menu_2(self):
        frame = self.camera.rtrn_frames()  # Get the camera frames
        if frame is not None:
            frame = self.draw2.convert(frame)  # Convert the frame to PIL format
            self.screen.disp_img(frame)  # Display the frame on screen
    
    def menu_3(self):
        self.draw2.clear_img()  # Clear the image
        self.draw2.draw_msg('R E C O R D I N G  !', (80, 64))  # Draw recording message
    
    def control_menu_3(self):
        frame = self.camera.rtrn_frames()  # Get the camera frames
        if frame is not None:
            self.camera.save_frames(frame)  # Save the frames
    
    def menu_control(self):
        '''uncomment this if you want to test the time taken by the function to be executed'''
        # start=time.time()
        self.control_menu_0()  # Control the main menu
        # react=time.time()-start
        # print('reactivity=',react)
        state = self.button.get_State()  # Get the button state
        if state[1]:
            self.control_menu_1()  # If button 1 is pressed, control menu 1

        elif self.current_index < 5 and state[0]:
            # self.draw1.clear_img()
            i = int(self.current_index)  # Get the current index as integer
            self.camera.init_capture()  # Initialize camera capture
            self.camera.create_file()  # Create a file to save the video
            self.camera.set_rec_settings(wfps=self.wfps[i], dimensions=self.dimensions[i])  # Set recording settings
            self.draw2.draw.rectangle((20, 75, 155, 120), fill=(255, 0, 0))  # Draw a red rectangle
            self.draw2.draw_msg(message=self.char[i], position=(80, 80))  # Draw character message
            self.draw2.draw.rectangle((20, 5, 155, 55), fill=(255, 0, 0))  # Draw another red rectangle
            self.draw2.draw_msg(message=self.modes[i], position=(80, 35))  # Draw mode message
            
            self.screen.disp_img(self.draw2.rtrn_img())  # Display the image on screen
            
            while True:
                state = self.button.get_State()  # Get the button state
                self.control_menu_3()  # Control menu 3 (recording)
                if state[0] or state[1]:
                    self.camera.turn_off()  # Turn off the camera
                    self.temp = 100  # Reset the temp index
                    break
                
        elif self.current_index > 4 and state[0]:
            self.camera.init_capture()  # Initialize camera capture
            while True:
                state = self.button.get_State()  # Get the button state
                self.control_menu_2()  # Control menu 2 (camera view)
                if state[0] or state[1]:
                    self.camera.turn_off()  # Turn off the camera
                    self.temp = 100  # Reset the temp index
                    break
     
        # time.sleep(0.001)