import random
from datetime import datetime

def experiment():
    ls = []
    for i in range(999999999):
        ls.append(random.randint(-(10**20), 10*20))

    start_time = datetime.now()
    for i in range(600):
        random.randint(-(10**20), 10**20) in ls
    print('1. Поискал 100 раз за ' + str((datetime.now() - start_time).total_seconds()) + ' сек.')

    hash_set = set(ls)
    start_time = datetime.now()
    for i in range(600):
        random.randint(-(10**20), 10**20) in hash_set
    print('2. Поискал 100 раз за ' + str((datetime.now() - start_time).total_seconds()) + ' сек.')

    hash_dict = {}
    for element in ls:
        hash_dict[element] = True
    start_time = datetime.now()
    for i in range(600):
        random.randint(-(10**20), 10 ** 20) in hash_dict
    print('3. Поискал 100 раз за ' + str((datetime.now() - start_time).total_seconds()) + ' сек.')

experiment()