# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:31:42 2024

@author: admin
"""

class Menu:
    def __init__(self, screen,draw0,draw1,draw2,molette,button,camera):
        self.screen = screen
        self.draw0 = draw0
        self.draw1=draw1
        self.draw2=draw2
        self.items = []
        self.position=[]
        self.temp=0
        self.current_index = 0
        self.selected_item = None
        self.button=button
        self.molette=molette
        self.camera=camera
        self.wfps=30
        self.cfps=30
        self.speeds=[0.25,0.5,1,2,4]
        self.speed_index=2#1x
        self.height=screen.height
        self.width=screen.width

    def add_item(self, name,position):
        self.items.append(name)
        self.position.append(position)  
        
        
    def menu_0(self):
        
        self.draw0.clear_img()
        self.draw0.draw_icons()
        
        for i in range (len(self.items)):
            self.draw0.draw_msg(self.items[i],self.position[i])
            
        self.screen.disp_img(self.draw0.rtrn_img())
        
        #return self.draw0.rtrn_img()
            
   
    def control_menu_0(self):
        
        self.molette.set_pos(self.current_index) 
        self.current_index=max(0,self.molette.update())
        self.current_index=min(len(self.items)-1,self.current_index)
        
        
        #rectangle_position = (current_position[0] -40, current_position[1]-5, current_position[0]-35 , current_position[1] )
        #self.draw.clear_img()
        #self.draw0.draw.rectangle((self.position[0][0] -40, self.position[0][1]-5, self.position[len(self.items)-1][0]-35 , self.position[len(self.items)-1][1]),fill=(255, 0, 0) )
        #self.draw0.draw.rectangle(rectangle_position, fill=(255, 255, 255))
        #self.screen.disp_img(self.draw0.rtrn_img())
        #image=self.draw.rtrn_img()
        tmp_ind=int(self.current_index)
        for i in range (len(self.items)):
            if i == tmp_ind:
                self.draw0.bound_mssg(self.items[i],self.position[i],color='white')
            else :
                self.draw0.bound_mssg(self.items[i],self.position[i],color='red')

        
        if self.temp!=self.current_index:
            self.screen.disp_img(self.draw0.rtrn_img())

            print('current index=',self.current_index)
            print('temp=',self.temp)
            print('mollette=',self.molette.position)
            self.temp=self.current_index
    
    
    def menu_1(self):
        self.draw1.clear_img()
        #self.draw1.draw_msg(self.items[0],(80,20))
        self.draw1.draw_msg('faster',(120,100))
        self.draw1.draw_msg('slower',(40,100))
        #return self.draw1.rtrn_img()
        for i in range(len(self.speeds)):
           self.draw1.draw_msg(f'{self.speeds[i]}x',(int(31*(i+1)),64)) 
        
    def control_menu_1(self):
        #self.molette.set_pos(self.wfps)
        self.molette.set_pos(self.speed_index)
        #self.wfps=max(0,self.molette.update())
        #self.draw1.draw.rectangle((0, 64, 160 , 69),fill=(255, 0, 0) )
        #self.draw1.draw.rectangle((50+self.wfps, 64, 55+self.wfps , 69),fill=(255, 255, 255) )
        #self.draw1.draw_msg(f'={self.fps}',(120,64))
        
        self.speed_index=max(0,self.molette.update())
        self.speed_index=min(len(self.speeds)-1,self.speed_index)
        self.wfps=self.speeds[int(self.speed_index)]*self.cfps
        
        current_speed = self.speeds[int(self.speed_index)]
        #current_item=self.items[int(self.current_index)]
        tmp_ind=int(self.speed_index)
        
        for i in range (len(self.speeds)):
            if i == tmp_ind:
                self.draw1.bound_mssg(f'{self.speeds[i]}x',(int(31*(i+1)),64),color='white')
            else :
                self.draw1.bound_mssg(f'{self.speeds[i]}x',(int(31*(i+1)),64),color='red')
        
        
        if self.temp!=self.speed_index:
            self.screen.disp_img(self.draw1.rtrn_img())
            print(self.wfps)
            self.temp=self.speed_index
        
   
   
    def menu_2(self):
        pass
    
    
    def control_menu_2(self):
        frame=self.camera.rtrn_frames()
        
        if frame is not None:
            frame=self.draw2.convert(frame)
            self.screen.disp_img(frame)
            
        
    
    
    
    def menu_3(self):
        self.draw2.clear_img()
        self.draw2.draw_msg('Recording !',(80,64))
    
    
    
    def control_menu_3(self):
        frame=self.camera.rtrn_frames()
        if frame is not None :
            self.camera.save_frames(frame)
        
    
    def menu_control(self):
        self.control_menu_0()
        
        if self.current_index==0 and self.button.get_State()[0] :
            #self.draw1.clear_img()
            while True :
                self.control_menu_1()
                if self.button.get_State()[0]:
                    break
                
        elif self.current_index==1 and self.button.get_State()[0] :
            self.camera.init_capture()
            while True :
                self.control_menu_2()
                if self.button.get_State()[0]:
                    self.camera.turn_off()
                    break
                
        elif self.current_index==2 and self.button.get_State()[0] :
            self.camera.init_capture()
            self.camera.create_file()
            self.camera.set_rec_settings(w_fps=self.wfps)
            self.screen.disp_img(self.draw2.rtrn_img())
            
            while True :
                self.control_menu_3()
                if self.button.get_State()[0]:
                    self.camera.turn_off()
                    break

        
    
    
            

    
