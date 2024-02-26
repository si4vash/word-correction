import requests
def word_correction(text , language = 'en-Us'):
   #برای متون فارسی language = 'fa'
   #عموما زبان فارسی به صورت کامل صحیح نمیشود

    url = 'https://languagetool.org/api/v2/check'
    params = {
        'text' : text,
        'language' : language
    }
    response = requests.post(url , data = params)
    if response.ok:
        corrections = response.json()['matches']
        corrected_text = text
        for correction in corrections:
            replacement = str(correction['replacements'][0]['value'])
            corrected_text = corrected_text[:correction['offset']] + replacement + corrected_text[correction['offset'] + correction['length']:]
        return corrected_text
    else:
        print('error: ' ,response.status_code )
input_text = input('please write your text ----->: ')
corrected_text = word_correction(input_text)
print('corrected text is ---->: ')
print(corrected_text)           