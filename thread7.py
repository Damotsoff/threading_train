import time
import random
from threading import currentThread, Barrier, Thread
# Барьеры


def test(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f'potok [{currentThread().name}] запущен в {time.ctime()}')

    barrier.wait()
    print(f'potok [{currentThread().name}] преодолел барьер в {time.ctime()}')


bar = Barrier(5)
for i in range(5):
    Thread(target=test, args=(bar,), name=f'thr-{i}').start()
