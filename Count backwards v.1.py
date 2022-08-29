'''
Created by: Bohuslav Juráš
Contact: Bohuslav.juras@seznam.cz
For: Singh Neeraj / Accenture
Applying for position: Test Automation Engineer
First task - "Count backwards"
This program will print range of numbers from 100 to 0 with step -1. If number can be divided by number 5 instead of
printing number itself program will print "Agile". If number can be divided by number 3 instead of printing number
itself program will print "Software". If number can be divided by both instead of printing number itself program will
print "Testing"
'''

for count in range(100, 0, -1):
    if count % 3 == 0 and count % 5 == 0:
        print("Testing")
    elif count % 5 == 0:
        print("Agile")
    elif count % 3 == 0:
        print("Software")
    else:
        print(count)