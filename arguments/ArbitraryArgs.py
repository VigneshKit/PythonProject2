def student_details(*args): # When you are unaware of the number of arguments passed use Arbitrary arguments in Python
    # for item in args:
    #     print(item)
    # print('*'*10)
    print(args)

def test(age, name):
    print(age, name)

student_details(120,'Leapheng', 16)
student_details(121,'Sophat')
student_details()

