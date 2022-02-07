import threading
import time


def get_data(data, value):
    for _ in range(value):
        print(f'[{threading.currentThread().name}] - {data}')
        time.sleep(1)


thr_list = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(
        str(time.time()), i,), name=f'thr-{i}')
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()
print('finsh')
