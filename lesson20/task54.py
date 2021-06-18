import threading
import time
import random


def api(result):
    time.sleep(3)
    result['key'] = random.randint(1, 100)

# последовательный запуск

def posledovatelno():
    result1 = {}
    api(result1)

    result2 = {}
    api(result2)

    result3 = {}
    api(result3)

    result4 = {}
    api(result4)

    result5 = {}
    api(result5)

    print(result1['key'] + result2['key'] + result3['key'] + result4['key'] + result5['key'])

#posledovatelno()

# параллельный запуск

def paralelno():
    threads = []
    for _ in range(5):
        result = {}
        t = threading.Thread(target=api, args=(result,))
        t.start()
        threads.append([t, result])
    thread_number = 1
    sum = 0
    for thread, result in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(result['key']))
        sum += result['key']
        thread_number = thread_number + 1
    print('Сумма всех полученых элементов = ' + str(sum))

paralelno()
