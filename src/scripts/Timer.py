'''
Created on Apr 30, 2018

@author: robby
'''
from src.scripts.globals import Globals

class Timer:
    
    def __init__(self, interval = 1):
        self.interval = interval
        self.Value = 0
        self.LastInt = 0
        self.Active = False
        self.OnNext = None
    
    def Update(self):
        if self.Active:
            self.Value += Globals.deltatime / self.interval
            if int(self.Value) != int(self.LastInt):
                self.LastInt = int(self.Value)
                if self.OnNext != None:
                    self.OnNext()  
    
    def Start(self):
        self.Active = True
        
    def Pause(self):      
        self.Active = False
    
    def Stop(self):
        self.Reset()
        self.Active = False
    
    def Reset(self):
        self.Value = 0
        self.LastInt = 0
        self.Active = True