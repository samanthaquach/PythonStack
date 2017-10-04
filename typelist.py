# a = ['sam','is','the','best']
# s = ' '
# print s.join(a)

#input
a = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

def value_list(a):
    str_value = False
    int_value = False
    word_str = "String:"
    sum = 0
    for i in (a):
        print (i)
        if (type(i) == str):
            str_value = True
        elif (type(i) == int):
            int_value = True
        if (type(i) == str):
            word_str= word_str + " " + i
        if (type(i) == int or type(i) == float):
            sum = sum +i
    if str_value == True and int_value == True:
        print ('The list you entered is of mixed type')
    print word_str
    print sum
    
value_list(a)

