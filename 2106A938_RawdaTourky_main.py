# Import the classes
from classes import Patient, InstantPatient, RegularPatient

# Create a Patient object to see the TypeError that occurs
try:
    patient=Patient('ahmed','mohamed','20202022')
except TypeError:
    print(TypeError, 'You can not create an object from an abstract class')


# Assign objects of the concrete classes RegularPatient and InstantPatient to variables
patient1= RegularPatient('rawda','tourky','150119529',40)
print(patient1)
print('payment',patient1.payment())
print('------------------------')
patient2=InstantPatient('hana','ahmet','2672874',30,5)
print(patient2)
print('payment:',patient2.payment())

# Place the objects into a list, iterating through the list and displaying its string representation and payments
patient3=InstantPatient('hana','taher','2672874',70,5)
patient4= RegularPatient('sana','kareem','150119529',90)
patients = []
patients.append(patient1)
patients.append(patient2)
patients.append(patient3)
patients.append(patient4)

for p in patients:
    print(p)
    print(p.payment())
    print('-----------------------------')