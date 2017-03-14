import os
import requests

KEY = 'trnsl.1.1.20170314T160307Z.1e7a6b7de4b87ee7.93710f562d9b1c24923b14a54ea97edf244f694c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
CUR_DIR = os.path.curdir
ABS_PATH = os.path.abspath(CUR_DIR)


def read_from_file(path):
    f = open(path, 'r')
    text = f.read()
    f.close()
    return text


def write_to_file(path, text):
    f = open(path, 'a')
    f.write(str(text) + '\n')
    f.close()


def translate_file(path_to_origin, path_to_translated, origin_lang, future_lang):
    """
    :param path_to_origin:
    :param path_to_translated:
    :param origin_lang:
    :param future_lang:
    :return: path to translated file
    """
    path_to_origin = os.path.join(ABS_PATH, path_to_origin)
    path_to_translated = os.path.join(ABS_PATH, path_to_translated)

    text = read_from_file(path_to_origin)
    lang = origin_lang + '-' + future_lang
    params = {
        'key': KEY,
        'text': text,
        'lang': lang,
    }
    response = requests.get(URL, params)
    if response.status_code != 200:
        print('Can not translate text from file: ', path_to_origin)
    else:
        text = ' '.join(response.json()['text'])
        write_to_file(path_to_translated, text)
    return response.json()

translate_file('origin_files/english.txt', 'translated_files/from_eng.txt', 'en', 'ru')
translate_file('origin_files/german.txt', 'translated_files/from_german.txt', 'de', 'en')
# translate_file('origin_files/italian.txt', 'translated_files/from_italian.txt', 'it', 'ua')
