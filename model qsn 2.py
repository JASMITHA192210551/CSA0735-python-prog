
def get_first_letters(sentence):
    sentence = sentence.strip()
    words = sentence.split()
    if words:
        first_letters = [word[0] for word in words]
        result = '.'.join(first_letters)
        return result
    else:
        return ""  
input_sentence = "The cat on the wall"
output = get_first_letters(input_sentence)
print(output)
