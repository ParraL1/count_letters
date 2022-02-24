#Name: Lilliana Parra
#Date: 2/23/2022
#Github user: ParraL1
#Description: counts the number of letters entered

def count_letters(string):
    your_dict={}
    for i in string.upper():
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
    return your_dict