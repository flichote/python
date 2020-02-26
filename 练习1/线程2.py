import threading
import time
"""该线程会一直打印I am working,不会打印fineshed"""

def worker():
    while True:
        time.sleep(1)
        print("I am working")
    print("fineshed")

t = threading.Thread(target=worker,name='worker')
t.start()