# -----------------------------------------------------------# 
# Test script for generic list in python
#
# (C) 2020, LABANI SAID, France
# 
# @: labani.said@outlook.com
# -----------------------------------------------------------

from List import *
from Student import *


# Students database
StudentsData = ['Jean,LeBois,13.58,Grenoble',
                'Mark,Dassault, 10.20,Lyon',
                'Isebelle,Monier, 07.50,Marseille',
                'Victor,Guembetta, 09.80,Lyon',
                'Juliette,LeBois, 16.50,Lille']

#Students list of type student
Students = List[Student]([Student(student.split(',')[0],
                                  student.split(',')[1],
                                  student.split(',')[2],
                                  student.split(',')[3])
                          for student in StudentsData])

#Search for students who have Isebelle as firstname
print('Students with Isebelle as firstName: ',Students['FirstName=Isebelle'])

#Search for students who have the family name LeBois
print('FamilyName=LeBois: ',Students['FamilyName=LeBois'])

#Search for students who live in Lyon
print('Students adresse as Lyon: ',Students['Adresse=Lyon'])

#Search for students who passed their exams
print('Graduated students: ',Students['Graduated=True'])

#Search for students who failed their exams
print('Not Graduated students: ',Students['Graduated=False'])