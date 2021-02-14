# -----------------------------------------------------------# 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: labani.said@outlook.com
# -----------------------------------------------------------


class Transition:
    def __init__(self,  aStart=None, aLabel=None, aEnd=None): 
        self.Start = aStart
        self.Label = aLabel
        self.End   = aEnd        
        self.Type  = 'Loop' if aStart.Name in aEnd.Name else 'Direct'
