import threading
import time
"""该线程会正常结束"""

def worker():
    count = 0
    while True:
        if count > 5:
            break
        time.sleep(1)
        count += 1
        print('I am working')

    print('finished')

t = threading.Thread(target=worker, name='worker')

t.start()
print("==end==")

