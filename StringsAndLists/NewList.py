x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
# print x
y = x[len(x)/2:]
# print y
z = x[:len(x)/2]
y.insert(0,z)
print y
