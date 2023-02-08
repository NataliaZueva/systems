def mac_mac(v):
    val, s = input(f'{v}\n\t1. Yes\n\t0. No\n\t\t'), mac.get(v)
    result = s[0] if val == '1' else (s[1] if val == '0' else 'Ошибка')
    return result


mac = {}
with open('text.txt', 'r', encoding="utf-8") as file:
    for line in file:
        a = {line.split(':')[0]: line.split(':')[1].strip().split(',')}
        mac |= a

print('Какую базу данных выбрать?')
c = list(mac.keys())
res = mac_mac(c[0])
while len(mac.get(res.strip())) != 1:
    res = mac_mac(res.strip())
print(res)
