def student_details(**args):
    # for key,value in args.items():
    #     print(key,' = ', value)
    print(args.get('id'), args.get('name'), args.get('age'))

student_details(id=200, name='Sreylin', age = 16)
student_details(name='Sovann', id=3000)