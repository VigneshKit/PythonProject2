num = int(input('Input a number:'))

i=1
sum=0
while i<=num:
    sum+=i # sum = sum + i
    i+=1

    if i == 1000:
        break

print('Sum = ', sum)