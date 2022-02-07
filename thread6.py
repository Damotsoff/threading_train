from threading import Thread, BoundedSemaphore, currentThread
import time
import random


# Семафоры


max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    while True:
        with pool:
            slp = random.randint(1, 5)
            print(f'{currentThread().name} - sleep ({slp})')
            time.sleep(slp)


for i in range(10):
    Thread(target=test, name=f'thr-{i}').start()
