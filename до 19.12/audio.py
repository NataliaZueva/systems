import requests
from tinytag import TinyTag

FOLDER_ID = "b1gtf3dqupicap0o7l1v"
IAMToken = "t1.9euelZrMlIqbnpXJj5yVlciQnM6Lie3rnpWais-QkJ7OlZOcic6Llpaenprl8_cjEQZj-e9QAAUS_t3z92M_A2P571AABRL-.gOBX76B6Hs3jPwMekiARb_XmSTSc58AkCSFjGF4MbiQfvK60DR5qaFC-S3lU2EPdnMnZf3rUahrAvIhw6YF3CQ"

auth_headers = {"Authorization": "Bearer " + IAMToken}
url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?folderId=b1gtf3dqupicap0o7l1v&lang=ru"

post_data = {"folderId": FOLDER_ID, "lang": "ru"}
title = input('Введите имя файла или 1 - чтобы открыть готовый файл: ')
if title == '1':
    title = 'audio.ogg'
files = {'file': open(title, 'rb')}
tag = TinyTag.get(title)
print(f'Длина аудиозапис в секундах: {tag.duration}.')

response = requests.post(url, headers=auth_headers, data=open(title, 'rb'))

print(response.json())

voiceover = response.json()['result']
word = len(voiceover.split())
character = len(voiceover)
spaces = character - word + 1

print(f"Всего символов: {character}     Слов в строке: {word}     Символов без пробелов: {spaces}")
print(f"Скросоть символов в секунду: {character / tag.duration}")

