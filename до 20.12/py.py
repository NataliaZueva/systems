import json

import requests

folder_id = 'b1gtf3dqupicap0o7l1v'
IAM_TOKEN = 't1.9euelZrPnZmbjcyRz46Vl5TIxozNnu3rnpWais-QkJ7OlZOcic6Llpaenprl9PdgUQBj-e8cSSPj3fT3IAB-YvnvHEkj4w.3aKdh7Kx8ZQvyQl8NGwM1FmEAYorfJ7RzemlEf1stxu89EY3F0lacBMAgdes46KTiH1UAhl5n2mOdPYxa_9WDg'
target_language = 'ru'
url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + IAM_TOKEN
}
body = {
    "targetLanguageCode": target_language,
    "texts": '',
    "folderId": folder_id
}

a = list(input("Введите имя файлов для Чтения и Ответов \n       1 - чтобы работать с готовыми: ").split())
if a[0] == '1':
    name, answer = 'text.txt', 'answer.txt'
else:
    name, answer = a[0], a[1]
lines = []
with open(name, 'r', encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

with open("answer.txt", 'w') as file:
    for line in open(name, 'r', encoding="utf-8"):
        body["texts"] = line.strip()
        response = requests.post(url, headers=headers, json=body)
        file.write(json.dumps(response.json(), ensure_ascii=False) + "\n")
