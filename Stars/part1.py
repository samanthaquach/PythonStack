# def draw_stars():
# # num = 0
#     x = [4,6,1,3,5,7,25]
#     for num in range(len(x)):
#         print ("*") * (x[num])


# draw_stars()


arr = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
count = 0

for num in arr:
    if (type(num) == int):
        print num * "*"
    elif (type(num) == str):
        # print num
        for letter in num:
            print num[:1]
