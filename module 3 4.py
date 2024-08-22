import re


def single_root_words(root_word,*otcher_words):
    same_words = []
    #is_root_words = True

    for i in otcher_words:
            if root_word.lower() in i.lower() or i.lower() in root_word.lower():
                same_words.append(i)
    return same_words
result = single_root_words("rich","richiest","orichalcum","cheers",'richies')
print(result)
result_2 = single_root_words("Disablement","Able","Mable","Disable","Bagel")
print(result_2)





















