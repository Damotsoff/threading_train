import multiprocessing
import time


def test():
    while True:
        print(f'{multiprocessing.current_process().name}-{time.time()}')
        time.sleep(1)


multiprocessing.Process(target=test,name='prc1').start()
print('процесс запущен')
