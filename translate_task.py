import requests


KEY = 'trnsl.1.1.20170314T160307Z.1e7a6b7de4b87ee7.93710f562d9b1c24923b14a54ea97edf244f694c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_me(my_text, language='ru-en'):
    """
    Function gets parameters:
    text for translating;
    language in format 'ru-en' or 'ua-fr'
     :return:
     """
    params = {
        'key': KEY,
        'text': my_text,
        'lang': language
    }
    response = requests.get(URL, params=params)
    return response.json()


text = 'Не проигрывается видео на нашем сайте? Возможно, заблокирован прием Cookies в вашем браузере. Разрешите прием Cookies для php-academy.kiev.ua и для devionity.com. Если Cookies разрешены, напишите на oleg@php-academy.kiev.ua для срочного решения проблемы.У вас есть вопрос, предложение или жалоба? Напишите напрямую Олегу Шумару на oleg@php-academy.kiev.ua Помните, что вы в несколько кликов можете оценить качество обучения онлайн в личном кабинете! Просим поделиться вашим мнением →'

json = translate_me(text)
print(' '.join(json['text']))
