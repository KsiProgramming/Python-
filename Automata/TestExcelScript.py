# -----------------------------------------------------------# 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: said.labani@ens.paris.sacaly.fr
# -----------------------------------------------------------




from Automate import *
from List import *
from LoadExcelData2List import LoadExcelData2List



#Loading And Converting Excel Data To List Of Automata Object
AutomateListe = List[Automate](LoadExcelData2List('DataBase.xlsx'))
            



   
for automate in AutomateListe:
    #Display Decsription of Automata
    automate.DataTable()
    #Display Structural Analysis of Automata
    automate.StructuralAnalysis()    
    
          
#Check word on last automata

''' Rejected String'''
word = ['a','b','a','b','b','a','a','a'] 
automate.CheckWord(word)

''' Accepted String'''
word = ['a','a','b','g','g','g','g','g','g']
automate.CheckWord(word)

