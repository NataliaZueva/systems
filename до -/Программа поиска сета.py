import json

with open('text.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    cards = []
    for txt in text["cards"]:
        cards.append([txt['count'], txt["color"], txt["shape"], txt["fill"]])
sets = []
for i in range(len(cards) - 2):
    for j in range(i+1, len(cards) - 1):
        for k in range(j+1, len(cards)):
            num = 0
            for n in range(4):
                lst = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (1, 1, 1), (2, 2, 2), (3, 3, 3)]
                a = cards[i][n], cards[j][n], cards[k][n]
                if a in lst:
                    num += 1
            if num == 4:
                sets.append([cards[i], cards[j], cards[k]])
if sets:
    print('Найденный сет:', next(i for i in sets))
else:
    print('Сетов нет')