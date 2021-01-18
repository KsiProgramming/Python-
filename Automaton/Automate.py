# -----------------------------------------------------------# 
# Projet Génération Automate
#
# (C) 2020, LABANI SAID, Orsay, France
# 
# @: said.labani@ens.paris.sacaly.fr
# -----------------------------------------------------------

from Transition import *
from State import *
from List import *
from Alphabet import *
class Automate:
    
    def __init__(self, aAutomataName,
                       aStates,
                       aAlphabets,
                       aTransitions, 
                       aInitialStates,
                       aFinalStates,
                       aMarkedStates):
        self.Name = aAutomataName
        self.States = List[State]([State(state) for state in aStates.split(',')])
        self.Alphabets = List[Alphabet]([Alphabet(alphabet) for alphabet in aAlphabets.split(',')])
        self.Transitions = List[Transition]([Transition(self.States.FindFirstOrNone('Name',transition.split(',')[0])
                                                       ,self.Alphabets.FindFirstOrNone('Value',transition.split(',')[1])
                                                       ,self.States.FindFirstOrNone('Name',transition.split(',')[2]))
                                                        for transition in aTransitions])
        self.InitialStates =[self.States.FindFirstOrNone('Name',InitialState) for InitialState in aInitialStates.split(',')]
        self.FinalStates =  [self.States.FindFirstOrNone('Name',FinalState) for FinalState in aFinalStates.split(',')]
        self.MarkedStates = [self.States.FindFirstOrNone('Name',MarkedState) for MarkedState in aMarkedStates.split(',')  ] 
        self.__VisualGraph = None
        self.__SetInitialFinalMarkedStates()
        self.__SetFatherChild()
        self.__SetAccessibility()
        self.__SetCoAccessibility()
        self.__SetBlocking()
        self.AccessiblePart        = self.__GetAccessiblePart()
        self.CoAccessiblePart      = self.__GetCoAccessiblePart()
        self.BlockingPart          = self.__GetBlockingPart()
        self.NonCoAccessiblePart   = self.__GetNonCoAccessiblePart()
        self.CoAndAccessiblePart   = self.__GetCoAndAccessiblePart()        
        #self.__BuildGraphiz()
        
        
    def __str__(self):
        return self.Name
    def __repr__(self):
        return self.Name    
    
    def __SetInitialFinalMarkedStates(self):
        [InitialState.__setattr__('Initial',True) for InitialState in self.InitialStates]
        [FinalState.__setattr__('Final',True)     for FinalState in self.FinalStates]
        [MarkedState.__setattr__('Marked',True)   for MarkedState in self.MarkedStates if MarkedState is not None]
              
    def __SetFatherChild(self):
        for transition in self.Transitions:
            if not transition.Start.Child.__contains__(transition.End):
                transition.Start.Child.append(transition.End)  
            if not transition.End.Father.__contains__(transition.Start):
                transition.End.Father.append(transition.Start)
        
    def IsFather(self, aFather, aState):
        return True if aState.Father.__contains__(aFather) else False        
            
    def IsChild(self, aChild, aState):
        return True if aState.Child.__contains__(aChild) else False   
    
    def IsAccessible(self, aState):
        aState.Accessible = True
        [self.IsAccessible(Child) for Child in aState.Child if not Child.Accessible]
   
    def __SetAccessibility(self):
        [self.IsAccessible(InitialState) for InitialState in self.InitialStates]
        
    def IsCoAccessible(self, aState):
        aState.CoAccessible = True
        [self.IsCoAccessible(Father) for Father in aState.Father if not Father.CoAccessible]
   
    def __SetCoAccessibility(self):
        for MarkedState in self.MarkedStates:
            self.IsCoAccessible(MarkedState)
            
    def __SetBlocking(self):
        [State.__setattr__('DeadLock',True)  for State in self.States if not State.Child]
        
    
    def __GetAccessiblePart(self):
        return self.States['Accessible=True']
    
    def __GetBlockingPart(self):
        return self.States['DeadLock=True']
    
    def __GetCoAccessiblePart(self):
        return self.States['CoAccessible=True']
    
    def GetName(self,aList):
        return [Element.Name for Element in aList]
        
    def __GetNonCoAccessiblePart(self):
        """
        The next instruction line is commented to demonstrate that we can loop 
        throw the states collection searching for non coaccessible states using
        the attribut CoAccessible when it is false, Or we can just use the
        mathematical definition and the buil-in methods of the set object class
        in python, the non co accessible states is the defference states between
        the states collection and the coaccessible states collection
        """        
        #return self.States['CoAccessible=False']
        return sorted(set(self.GetName(self.States)).difference(self.GetName(self.CoAccessiblePart)))  
    
    
    def __GetCoAndAccessiblePart(self):
        return sorted(set(self.GetName(self.AccessiblePart)).intersection(self.GetName(self.CoAccessiblePart)))
    
    def StructuralAnalysis(self):
        print(f'\n *** The structural analysis of automaton {self.Name} ***')
        [print(f'The automaton {self.Name} is Blocking.'), print(f'The blocking states: ',*self.BlockingPart,sep=' ')
         if len(self.BlockingPart) else print(f'The automaton {self.Name} is not blocking.')]
        [print(f'The automaton has {len(self.AccessiblePart)} accessible states:',*self.AccessiblePart,sep=' '),
        print(f'The automaton has {len(self.BlockingPart)} DeadLock states:',*self.BlockingPart,sep=' ' ),
        print(f'The automaton has {len(self.CoAccessiblePart)} coaccessible states:',*self.CoAccessiblePart,sep=' '),
        print(f'The automaton has {len(self.CoAndAccessiblePart)} Co&Accessible states: ',*self.CoAndAccessiblePart,sep=' '),
        print(f'The automaton has {len(self.NonCoAccessiblePart)} NonCoaccessible states:',*self.NonCoAccessiblePart,sep=' ')]
        

    def DataTable(self):
        print(f'\n *** The detailed description of automata {self.Name} States ***')
        DataTable = [{'Name'         :   State.Name, 
                      'Initial'      :   State.Initial, 
                      'Final'        :   State.Final,
                      'Accessible'   :   State.Accessible,
                      'CoAccessible' :   State.CoAccessible,
                      'DeadLock'     :   State.DeadLock} 
                      for State in self.States]
        import pandas
        print(pandas.DataFrame(DataTable))
        DataTable2 = [{'Name'   : State.Name , 
                       'Father' : sorted([Father.Name for Father in State.Father]) ,
                       'Child'  : sorted([Child.Name for Child in State.Child])}
                      for State in self.States]
        print(pandas.DataFrame(DataTable2))  
        
        print(f'\n *** The detailed description of automata {self.Name} Transition ***')
        DataTable = [{'Start' : Transition.Start, 
                      'Label' : Transition.Label, 
                      'End'   : Transition.End,
                      'Type'  : Transition.Type }
                     for Transition in self.Transitions]
        print(pandas.DataFrame(DataTable))
        
        
        
        
    def __BuildGraphiz(self):
        from graphviz import Digraph
        self.__VisualGraph = Digraph(comment=self.Name)

        for state in self.States:
            if state.Marked:
                self.__VisualGraph.node(state.Name, state.Name,shape='doublecircle')
            else:
                self.__VisualGraph.node(state.Name,state.Name)
                
        for InitialeState in self.InitialStates:
            self.__VisualGraph.node(f'Initial{InitialeState.Name}',' ',shape='none')
            self.__VisualGraph.edge(f'Initial{InitialeState.Name}',InitialeState.Name,constraint='true') 
            
    
        for edge in self.Transitions:
            self.__VisualGraph.edge(edge.Start.Name,edge.End.Name, constraint='true',label=edge.Label.Value)

    def GraphView(self):
        from graphviz import Source

        self.__VisualGraph.render(f'GeneratedGraph/{self.Name}.gv', view=False)  # doctest: +SKIP
        f'GeneratedGraph/{self.Name}.pdf'
        print(Source(self.__VisualGraph, filename=f'GeneratedGraph/{self.Name}.gv', format="png").view())