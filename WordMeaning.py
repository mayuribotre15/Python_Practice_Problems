# Create a dictionary and take a input from used and return the meaning of that word
dict_meaning = {'hashable': 'Not changable, cannt be modifies',
                'mutable': 'Changable, can be modified',
                'set': 'collection of uniques element',
                'list': 'collection of items, may be duplicate items',
                'unhashable': 'changable, mutable, can be modified'}
print
# take input from the user
w = input("Enter word to check the meaning: ")
word = w.lower()
if word in dict_meaning.keys():
    print(dict_meaning[word])
else:
    print('Enter a word present in dictionary')
