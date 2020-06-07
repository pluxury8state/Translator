import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}'.format(to_lang)
    }
    response = requests.get(URL, params=params)
    json_ = response.json()


    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    text = []
    with open('DE.txt', 'r', encoding='utf8') as file:
        for string in file:
            string = translate_it(string,'ru')
            text.append(string)
    with open('new_DE.txt', 'w', encoding='utf8') as new_file:
        for string in text:
            new_file.write(string)
        text = []
    with open('ES.txt', 'r', encoding='utf8') as file:
        for string in file:
            string = translate_it(string, 'ru')
            text.append(string)
    with open('new_ES.txt', 'w', encoding='utf8') as new_file:
        for string in text:
            new_file.write(string)
        text = []
    with open('FR.txt', 'r', encoding='utf8') as file:
        for string in file:
            string = translate_it(string, 'ru')
            text.append(string)
    with open('new_FR.txt', 'w', encoding='utf8') as new_file:
        for string in text:
            new_file.write(string)
        text = []
