# myList = [1, 2, 3, 4]
# myDictionary = {
#     "first_name" : "Kevin",
#     "last_name" : "Evangelista",
#     "isStudent" : "True",
#     "isInstructor" : "False"
# }
# result = myDictionary["last_name"]
# print(result)      ### or
# print(myDictionary["first_name"])
# if result != None:
#     print(f"key was found {result}")
# else:
#     print(f"key was not found {result}")
# myDictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
### HOW TO CHANGE THE VALUE IN DICTIONARY
# print(myDictionary)
# myDictionary["hello"] = "Digital Crafts" 
# print(myDictionary)
##### HOW TO ADD VALUE IN DICTIONARY
# print(myDictionary)
# myDictionary["school"] = "University of Houston" 
# print(myDictionary)
##### PRINTS THE VALUES prints the values (the second element after the colon)
# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# results = my_dictionary.values()
# print(results)
##### PRINTS THE KEYS (first element before colon)
# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# keys = my_dictionary.keys()
# print(keys)
##### ITERATING
# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# results = my_dictionary.items()
# print(results)
# #### f = short for format
# for key, value in my_dictionary.items():
#     print (f"my key is {key} my value is {value}")
#     ###### or
#     # print(key)
#     # print(value)
# isItThere = "hello" in myDictionary
# print(isItThere)
# #### adding if and elseifs to dictionary
# if "hello" in myDictionary:
#     print("found")
# else:
#     print("not found")
##### NESTING
# contactList = [{
#     "first_name" : "Kevin",
#     "last_name" : "Evangelista",
#     "email" : "kevin.evangelista11@gmail.com",
#     "phone" : "281-330-8004",
# }, {
#     "first_name" : "Michael",
#     "last_name" : "Jordan",
#     "email" : "michaeljordan@jordan.com",
#     "phone" : "232-323-2323",
# }, {
#     "first_name" : "Kyrie",
#     "last_name" : "Irving",
#     "email" : "kirving@irving.com",
#     "phone" : "111-111-1111",
# }]
# result = contactList[0]["email"]
# result = contactList[1]["first_name"]
# print(result)
##### NUMBER INSIDE [] IS ORDER IN NESTING INDECES
##### SECOND ITEM = VALUE
##### ADDING DICTIONARY TO NESTING
# contactList = [{
#     "first_name" : "Kevin",
#     "last_name" : "Evangelista",
#     "email" : "kevin.evangelista11@gmail.com",
#     "phone" : "281-330-8004",
# }, {
#     "first_name" : "Michael",
#     "last_name" : "Jordan",
#     "email" : "michaeljordan@jordan.com",
#     "phone" : "232-323-2323",
# }, {
#     "first_name" : "Kyrie",
#     "last_name" : "Irving",
#     "email" : "kirving@irving.com",
#     "phone" : {
#         "work" : "111-111-1111",
#         "home" : "222-222-2222"
#     }
# }]
# result = contactList[0]["email"]
# result = contactList[1]["first_name"]
# ##### HOW TO GET A VALUE IN A DICTIONARY WITHIN NESTING
# result = contactList[2]["phone"]["work"]
# print(result)
# while True:
#     try:
#         x = int(input("enter in a number >>"))
#         break
#     except ValueError:
#         print("oops try again")
#### USING IF AND ELIF
# while True:
#     if True:
#         try:
#             x = int(input("enter in a number>>>"))
#             break
#         except ValueError:
#             print('oops')
#     else:
#         print('oops')
#         break
##### ADVANCED TRY/EXCEPT
# try:
#     do_something()
# except Error1:
#     failure1()
# except Error2:
#     failure2()
# else:
#     only_execute_when_successful()
# finally:
#     always_execute()
#### CREATING YOUR OWN FAILURE
# x = 10
# if x > 5:
#     raise Exception('Custom Error: Danielle Sucks')
##### USING PICKLE AS A DATABASE!!!!
# import pickle
# data = {'name' : 'Paul'}
# with open('data.pickle', 'wb') as fh:
#     pickle.dump(data, fh)
# import pickle
# with open('data.pickle,' 'rb') as fh:
#     data = pickle.load(fh)
# print(data)
