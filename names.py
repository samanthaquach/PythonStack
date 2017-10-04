# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for i in students:
#     print i['first_name'],i['last_name']

full_name = ''
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for items, names in users.iteritems():
    # print names
    print items
    num = 0
    for i in names:
        # print i
        num += 1
        full_name = i['first_name']+(' ')+i['last_name']
        print str(num) + '-' + full_name + '-' + str(len(full_name)-full_name.count(" "))
        full_name = ''
    


    # print (len(users[group]))
    # for key in group:
    # for val in group.intervalues():
    #     print val
        
        

# for key,data in users.iteritems():
#     #  print key, " = ", data
#     print key
#     # print data
