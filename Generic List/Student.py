# -----------------------------------------------------------# 
# Student class as object to test generic list 
#
# (C) 2020, LABANI SAID, France
# 
# @: labani.said@outlook.com
# -----------------------------------------------------------

class Student:
    def __init__(self, aFirstName= None, aFamilyName= None, aFinalGrade= None, aAdresse= None):
        self.FirstName   = aFirstName
        self.FamilyName = aFamilyName
        self.FinalGrade   = eval(aFinalGrade)
        self.Graduated  = True if self.FinalGrade >= 10.00 else False
        self.Adresse    = aAdresse
        
    def __str__(self):
        return f'{self.FirstName} {self.FamilyName}'
    def __repr__(self):
        return f'{self.FirstName} {self.FamilyName}'