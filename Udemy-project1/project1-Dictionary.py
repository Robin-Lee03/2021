import json             # dic 的檔案
import difflib

from difflib import get_close_matches
# data = json.load(open('data.json'))   # way 1


with open('data.json', 'r') as f:       # way 2
    data = json.load(f)

def translate(w):
    if w in data:
        return data[w]
    if w.title() in data:
        return data[w.title()]

    elif len(get_close_matches(w,data.keys())) > 2:
        yn = input('Did you mean %s instead ? Enter Y if yes or N if no: ' % get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. please double check it."
        else:
            return "We don't understand your require: "
    else:
        return "this word can't find in dict"

# print(type(data))

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



# print(data['rain'])