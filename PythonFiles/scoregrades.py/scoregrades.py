def grades(list):
    str0 = ("Your grade is ")
    str1 = ("A")
    str2 = ("B")
    str3 = ("C")
    str4 = ("D")
    str5 = ("Score: ")
    for num in range(10):
        import random
        random_num = (random.randint(60,100))
        if (90 <= random_num <= 100):
            print random_num, str0+str1
        if (80 <= random_num <= 89):
            print random_num, str0+str2
        if (70 <= random_num <= 79):
            print random_num, str0+str3
        if (60 <= random_num <=69):
            print random_num, str0+str4

import random
random_num = (random.randint(90,100))
grades(random_num)