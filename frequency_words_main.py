from frequency_words import frequency_of_words,sorting
def main():
    string = "which is better python 2 or python 3"
    st_split = string.split()
    dic = frequency_of_words(st_split)
    sort = sorting(dic)
    for s in sort:
        print(s)
if __name__ == "__main__":
    main()
