# 3. Get Values From a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary2(key_name, some_list):
#     for item in some_list:
#         for key, value in item.items():
#             if key == key_name:
#                 print(value)

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


def iterateDictionary2(key_name, some_list):
    for i in range (0,len(some_list)):
        for key, value in some_list[i].items():
            if key == key_name:
                print(value)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
