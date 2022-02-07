import threading
import time
event = threading.Event()

def image_handler():
    thr_num = threading.currentThread().name
    print(f'идет подготовка изображения из потока - [{thr_num}]')
    event.wait()
    print('изображение отрпавлено')


for i in range(10):
    threading.Thread(target=image_handler,name=str(i)).start()
    print(f'поток {i} запущен')
    time.sleep(1)

if threading.active_count() >= 10:
    event.set()