#Name: Lilliana Parra
#Date: 2/23/2022
#Github user: ParraL1
#Description: counts the number of letters entered


def count_letters(string):
    result = {}


    for x in string.upper():


        if (x>='A' and x<='Z'):


            if not result.get(x):


                result[x] = 1
            else:

                result[x] += 1
                return result




