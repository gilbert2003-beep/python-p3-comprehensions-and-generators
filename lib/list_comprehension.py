def return_evens(num_list):
    return [item for item in num_list if item % 2 == 0]

def make_exclamation(sentence_list):
    return [item + "!" for item in sentence_list]

# Test the return_evens function
old_list = [1, 2, 3, 4, 5]
new_list = return_evens(old_list)
print(new_list)  # Output: [2, 4]

# Test the make_exclamation function
sentences = ["Hello", "How are you", "Python is fun"]
exclamations = make_exclamation(sentences)
print(exclamations)  # Output: ['Hello!', 'How are you!', 'Python is fun!']
