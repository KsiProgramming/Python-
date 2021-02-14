# ----------------------------------------------------------- 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: labani.said@outlook.com
# -----------------------------------------------------------

from Automate import *




NomAutomate     = "AF_p05_Acc_CoAcc"
Etats           = '0,1,2,3,4,5,6'
Alphabets       = 'a,b,g'
Transitions     = [('0,a,1'),('1,b,2'),('2,g,0'),
                   ('1,a,3'),('1,g,5'),('6,b,2'),
                   ('6,a,3'),('3,b,4'),('4,a,3'),
                   ('4,g,4')]
EtatsInitiales  = '0'
EtatsFinales    = '2'
Markedstates    = '2'
 
Automa = Automate(NomAutomate, Etats
                             , Alphabets
                             , Transitions
                             , EtatsInitiales
                             , EtatsFinales,Markedstates)


#Display Decsription of Automata
Automa.DataTable()
#Display Structural Analysis of Automata
Automa.StructuralAnalysis()
#Display Create Graph of Automata
Automa.PrintGraph
#Display Create Graph of Automata
Automa.ExportGraph()
#Display Create Graph of Automata
Automa.Standard.PrintGraph
#Display Graph of Standard Automata
Automa.Standard.ExportGraph()
#Display Fire Graph of Automata
Automa.FireGraph
      
#Check word on last automata

''' Rejected String'''
Rejectedword = ['a','b','a','b','b','a','a','a'] 
Automa.CheckWord(Rejectedword)

''' Accepted String'''
Acceptedword = ['a','a','b','g','g','g','g','g','g']
Automa.CheckWord(Acceptedword)



