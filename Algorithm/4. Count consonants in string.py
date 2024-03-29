#consonant is a letter that is not a vowel

input_str_1 = 'abc de'
input_str_2 = 'LuCiDProGrAmMiNG'

vowel = "aeiou"

def iterative_count_consonants(input_str):
    count =0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():#is alphabet
            count +=1
    return count

iterative_count_consonants(input_str_1)
iterative_count_consonants(input_str_2)


def recursive_count_consonant(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1+recursive_count_consonant(input_str[1:])
    else:
        return recursive_count_consonant(input_str[1:])

recursive_count_consonant(input_str_1)
recursive_count_consonant(input_str_2)