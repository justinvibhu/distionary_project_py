import json

from difflib import get_close_matches


data = json.load(open("data.json"))


def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y for YES or N for NO " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "please Enter Correct word "
        else:
            return "word doesn't Exist,please Enter Correct word "
    else:
        return "The word is no exits in dictionary"


print("Welcome to python Dictionary :")
word = input("Enter the word: ")

output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

