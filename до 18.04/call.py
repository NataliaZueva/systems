import datetime
import random

start_date = datetime.datetime.now() - datetime.timedelta(weeks=1)
call_log = []

for i in range(20):
    call_start = start_date + datetime.timedelta(
        minutes=random.randint(0, 60 * 24 * 7))
    call_duration = random.randint(10, 10800)  # от 10 сек до 3 часов
    caller_number = '8' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
    called_number = '8' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
    call_log.append({'start_time': call_start, 'end_time': call_start + datetime.timedelta(seconds=call_duration),
                     'duration': call_duration, 'caller': caller_number, 'called': called_number})

with open('file.txt', 'w') as f:
    f.write("""CREATE TABLE call_log (
        id INT(10) unsigned NOT NULL AUTO_INCREMENT,
        start_time DATETIME NOT NULL,
        end_time DATETIME NOT NULL,
        duration INT NOT NULL,
        caller_number VARCHAR(20) NOT NULL,
        callee_number VARCHAR(20) NOT NULL,
        PRIMARY KEY (`id`));\n\n""")
    f.write('INSERT INTO `call_log` (`start_time`, `end_time`, `duration`, `caller_number`, `callee_number`) VALUES\n')
    for call in call_log:
        f.write(f"('{call['start_time'].strftime('%Y-%m-%d %H:%M:%S')}', "
                f"'{call['end_time'].strftime('%Y-%m-%d %H:%M:%S')}', "
                f"'{call['duration']}', "
                f"'{call['caller']}', "
                f"'{call['called']}')")
        if call != call_log[-1]:
            f.write(", \n")
    f.write(";")
