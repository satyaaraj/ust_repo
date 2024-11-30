string = "which is better python 2 or python 3"
str_split = string.split()
str_split.sort()
d = {}
for st in str_split:
    i = 1
    if st in d.keys():
        d[st] = i
    else:
        d[st] = 1
print(d)
list_d = list(d.items())
for ls in list_d:
    print(ls)
