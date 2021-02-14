# -----------------------------------------------------------# 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: said.labani@ens.paris.sacaly.fr
# -----------------------------------------------------------
import pandas as pd
from Automate import *


def LoadExcelData2List(aExcelPath):  
    '''
    @param self
    '''
    """  Load an convert excel data to list of automata object   
    Parameters
    ----------
    aExcelPath : string
        Path of the Excel file.

    Returns
    -------
    AutomateList : List<Automate>
        A list of automata object.

    """    
    
    
    ExcelData = pd.ExcelFile('DataBase.xlsx')  
    AutomateList,AutomataNameList = list(),set()
    sheet = ExcelData.parse('State')
    
    for AutomataName in ExcelData.parse('Automate').itertuples():
        AutomataNameList.add(AutomataName.__getattribute__('Nom_Automate'))

    for AutomateNom in AutomataNameList:
        StatesList = ''
        EtatsInitiales  = ''
        EtatsFinales    = ''
        Markedstates    = ''
        
        for State in ExcelData.parse("State").itertuples():
            if State.__getattribute__('Nom_Automate') == AutomateNom:
                StatesList += f'{State.__getattribute__("Nom_State")},'            
                if State.__getattribute__('Initial') == True:
                    EtatsInitiales += f'{State.__getattribute__("Nom_State")},'
                if State.__getattribute__('Final') == True:
                    EtatsFinales += f'{State.__getattribute__("Nom_State")},'
                if State.__getattribute__('Marked') == True:
                    Markedstates += f'{State.__getattribute__("Nom_State")},'                
                
        StatesList     = StatesList[:-1]  
        EtatsInitiales = EtatsInitiales[:-1] 
        EtatsFinales   = EtatsFinales[:-1] 
        Markedstates   = Markedstates[:-1]  
        
        Alphabet = ''
        for Symbol in ExcelData.parse("Symbol").itertuples():
            if Symbol.__getattribute__('Automate_Name') == AutomateNom:
                Alphabet += f'{Symbol.__getattribute__("Symbol_Name")},'
                
        Alphabet=Alphabet[:-1]
        Transitions = []
        for Transition in ExcelData.parse("Transitions").itertuples():
            if Transition.__getattribute__('Name_Automate') == AutomateNom:
                Transitions.append(f'{Transition.__getattribute__("Begin_Transition")}'
                                  + f',{Transition.__getattribute__("Transition_Symbole")}'
                                  +f',{Transition.__getattribute__("Transition_End")}')
                
        AutomateList.append(Automate(AutomateNom
                                                ,StatesList
                                                ,Alphabet
                                                ,Transitions
                                                ,EtatsInitiales
                                                ,EtatsFinales
                                                ,Markedstates))

    return AutomateList
                

