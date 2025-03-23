my_list = []
for i in range(10,40.10):
    my_list.append(i)
    
my_list[1] = 15

my_list.extend(50, 60, 70)

my_list.pop()

my_list.sort()

print(my_list.index(30))