def frequency_of_words(stri):
    di = {}
    for st in stri:
        i = 1
        if st in di.keys():
            di[st] = i
        else:
            di[st] = 1
    return di
def sorting(di):
    list_d = list(di.items())
    sort_list = sorted(list_d)
    return sort_list
    
    
