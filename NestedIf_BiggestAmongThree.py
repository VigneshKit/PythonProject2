a,b,c = int(input("Input first numbers")), int(input("Input Second Number")), int(input("Input third number"))
# a = int(a)
# b = int(b)
# c = int(c)

if a>b:
    if a>c:
        print(a,' Is greater')
    else:
        print(c,' Is greater')
elif b>c:
    print(b,' Is greater')
else:
    print(c,' Is greater')