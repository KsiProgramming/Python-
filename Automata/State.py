# -----------------------------------------------------------# 
# Projet Génération Autoate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: said.labani@ens.paris.sacaly.fr
# -----------------------------------------------------------


class State:
    def __init__(self,  aName=None): 
        self.Name = aName 
        self.Marked = False
        self.Initial = False
        self.Final = False
        self.Father = []
        self.Child = []
        self.Accessible = False
        self.CoAccessible = False
        self.DeadLock = False        
        
    def __repr__(self):
        return self.Name
    
    def __str__(self):
        return self.Name
    
    def __eq__(self,aOtherState):
        return True if self.Name == aOtherState.Name else False
    
    
    
        


