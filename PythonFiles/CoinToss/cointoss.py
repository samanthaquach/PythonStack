import random
import itertools
side = ['head','tail']
num = 1
str1 = ('Throwing a coin...')
outcomes = { 'heads':0,
                'tails':0,
                }
def coins(num):
    for num in range (7):
        num+=1
        sides = outcomes.keys()
        outcomes[ random.choice(sides) ] += 1
        print ("Attempt #"), num
        print str1
        quarter = random.choice(side)
        print ("it is ") + quarter
        print 'Heads:', outcomes['heads']
        print 'Tails:', outcomes['tails']

ls = [1,2]
coins(ls)

    
    