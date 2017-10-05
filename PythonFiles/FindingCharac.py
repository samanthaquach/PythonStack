
a = ['hello','world','my','name','is','Anna']
new_arr = []

def newarr(new_arr):
    for i in range(len(a)):
        if (a[i]) == 'hello':
            new_arr.append(a[i])
        if (a[i] == 'world'):
            new_arr.append(a[i])
    print new_arr
newarr(new_arr)