namesList = ['Sothea','Sovann', 'Kettesak','Piseth','Somphors','Ryuto','Hinayo']
print(namesList)

for name in namesList:
    print(name)

# Dictionary, List, Set, Tuple
userIdAndPassword = { 'Sothea':12345,'Sovann':65498, 'Kettesak':8791453,'Piseth':'' }

# print(userIdAndPassword.values())
# print(userIdAndPassword.keys())
print('*'*10)
for i in userIdAndPassword:
    print(i,'=',userIdAndPassword[i])
print('*'*10)

for key,value in userIdAndPassword.items():
    print(key,' = ',value)

print('*'*10)

for item in userIdAndPassword.items():
    print(item)

print('#'*10)

for i in userIdAndPassword:
    if i == 'Sothea' or i == 'Sovann':
        print(userIdAndPassword[i])

counter = 0
for i in range(len(userIdAndPassword)):
    if i%3==0:
        print(userIdAndPassword.get(i))