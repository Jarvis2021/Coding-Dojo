# # 1.Update Values in Dictionaries and Lists
#     # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x = [ [5,2,3], [10,8,9] ]
# def changeofListValue(x):
#     x[1][0] = 15
#     return x
# print(changeofListValue(x))
#
#     # Change the last_name of the first student from 'Jordan' to 'Bryant'
#
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
#
# def changeDictValue1(students):
#     students[0]['last_name'] = 'Bryant'
#     return students
#
# print(changeDictValue1(students))
#
#     # In the sports_directory, change 'Messi' to 'Andres'
#
# sports_directory = { 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#                     'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
#
# def changeDictValue2(sports_directory):
#         sports_directory['soccer'][0] = 'Andres'
#         return sports_directory
#
# print(changeDictValue2(sports_directory))
#
#
#     # Change the value 20 in z to 30
#
# z = [ {'x': 10, 'y': 20} ]
#
#
# def ChangeDictValue3(z):
#     z[0]['y'] = 30
#     return z
#
# print(ChangeDictValue3(z))
#
#
#
# # 2. Iterate Through a List of Dictionaries
#
#
# students1 = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
#
# def iterateDictionary(students1):
#     for i in range (0,len(students1)):
#         # print (students1[i])
#         print "first-name - " + students1[i]['first_name'] + ", " + "last-name - " + students1[i]['last_name']
#
# iterateDictionary(students1)
#
#
# # 3.Get Values From a List of Dictionaries
#
# def iterateDictionary2(x,y):
#     for i in range (0,len(y)):
#         print(y[i][x])
#
#
# iterateDictionary2('first_name',students1)
# iterateDictionary2('last_name',students1)
#
#
#
# # 4. Iterate Through a Dictionary with List Values
#
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
#
# def printInfo(x):
#     print len(x['locations']) ,"LOCATIONS"
#     for i in range (0,len(x['locations'])):
#         print x['locations'][i]
#
#     print len(x['instructors']) ,"INSTRUCTORS"
#     for i in range (0,len(x['instructors'])):
#         print x['instructors'][i]
#
# printInfo(dojo)



def calculateSq(n):
    return n*n
numbers = (2, 3, 4, 5)
result = map( calculateSq, numbers)
print(result)
