string = "which is better python 2 or python 3"
str_split = string.split()
d = {}
for st in str_split:
    i = 1
    if st in d.keys():
        d[st] = i
    else:
        d[st] = 1
list_d = list(d.items())
sorted_list = sorted(list_d)
for i in sorted_list:
    print(i)
