import threading
import time


cond = threading.Condition()

def f1():
    while True:
        with cond:
            cond.wait()
            print('получили событие')

def f2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f'f1: {i}')
        time.sleep(0.2)

threading.Thread(target=f1).start()
threading.Thread(target=f2).start()