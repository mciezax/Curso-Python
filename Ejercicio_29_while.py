var = 1
while var < 10:
    print("#")
    var = var << 1



a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)



my_list = [3, 1, -2]
print(my_list[my_list[-1]])


vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]


vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)



t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)


my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

