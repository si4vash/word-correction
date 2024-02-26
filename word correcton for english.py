import enchant
def word_correction(text):
    dictionary = enchant.Dict('en_US')
    corrected_text = []
    words = text.split()
    for word in words:
        if not dictionary.check(word):
            suggestions = dictionary.suggest(word)
            if suggestions:
                corrected_text.append(suggestions[0])
            else:
                corrected_text.append(word)
        else:
            corrected_text.append(word)
    return ' '.join(corrected_text)
input_text = input('please write your text')
corrected_text = word_correction(input_text)
print('corrected text is -----> : ')
print(corrected_text)