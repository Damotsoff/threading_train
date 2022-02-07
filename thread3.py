import threading
import time

# Отличия lock от Rlock , синхронизация потоков
#отлчия заключается в том что лок можно разблокировать из любого потока , 
# а используя рлок разблокировать можно только из потока которым выполнена блокировка


value = 0
locker = threading.Lock()


def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(1)
        print(value)
        locker.release()


for _ in range(5):
    threading.Thread(target=inc_value).start()
