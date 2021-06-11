# def sumofcollection(*num): # Tuple=> Immutable
#     for i in num:
#         for j in i:
#             print(j)
#         print('*'*10)
#
# list = [500,800,50,25,45]
# dict = {123:"Kimhour", 134: "Sereyvann", 145: "Ratanak"}
# sumofcollection(list, dict)

def sumofcollection(list_num):
    return sum(list_num)

result = sumofcollection([50,60,100,85,65])

def ret_collection_from_fn(ran):
    list = []
    for i in range(ran):
        list.append(i)
    return '\n'.join(map(str,list))
    # return list
print(ret_collection_from_fn(5))


def fetchrecords():
    listOfUsers = {123:"Kimhour", 134: "Sereyvann", 145: "Ratanak"}
    return listOfUsers

print(fetchrecords())