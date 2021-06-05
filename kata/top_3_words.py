#! /usr/bin/env python3

#def top_3_words(string):
#    first_word = regex of word
#    next_word = first word of string without first word
#    if first word != next_word:
#       get next word
import re

def top_3_words(string, somelist=[]):
    string = string.lower()
    first_word = re.match("\w+", string)
    if first_word is None:
        new_list = sorted(somelist, key=lambda x:x[1], reverse=True)[:3]
        result = []
        for element in new_list:
            result.append(element[0])
        somelist.clear()
        return result 
    else:
        current_word = first_word.group()
        same_words = re.findall(r'\b(?=\w)' + current_word +r'\b(?!\w)', string)
        count = len(same_words)
        new_string = re.sub(r'\b(?=\w)' + current_word +r'\b(?!\w)', ' ',
                string).strip(' ,!')
        somelist.append((current_word, count))
    return top_3_words(new_string, somelist) 

print(top_3_words('hobo hobo hey hobo hobo hey hey hey hey ho ho ho hohey!, heyhobo hobo hoboho'))

result = top_3_words('fa ge t fa fa ge, ge ge ge !')
print(result)
print(top_3_words('merry merry mad merry mad lad ! , happen'))
