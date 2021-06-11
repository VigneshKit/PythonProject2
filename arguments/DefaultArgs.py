
def student_details(id=0, name='Batch 9 Student', age=0):
#Assigning default values to the paramters if possibly arguments may not be supplied by the caller
    print('Id: ', id, 'Name: ', name, 'Age: ', age)

student_details()
student_details(200, 'Serevath',16)
student_details(age = 16, name= 'Kimhour',id=1000)