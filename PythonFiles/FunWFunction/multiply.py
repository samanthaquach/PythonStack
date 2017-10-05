def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b


def layered_multiples(arr):
    a = [2,4,5]
    print arr
    newarr = []
    for x in arr:
        arro = []
        # return arro
        for i in range(0,x):
            arro.append(1)
            # return arro
        newarr.append(arro)
    return newarr
a = [2,4,5]
x = layered_multiples(multiply(a,3))
print x
layered_multiples