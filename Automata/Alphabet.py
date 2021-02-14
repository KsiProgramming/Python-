# -----------------------------------------------------------# 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: said.labani@ens.paris.sacaly.fr
# -----------------------------------------------------------

class Alphabet:
    
    def __init__(self,  aValue=None): 
        self.Value = aValue
        
    def __repr__(self):
        return self.Value
    
    def __str__(self):
        return self.Value