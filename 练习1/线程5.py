import threading
import time

def showthreadinfo():
    print('current thread = {}\nname thread = {}\nactive count = {}\nenumerate = {}\n'.format(
        threading.current_thread(),threading.main_thread(),threading.active_count(),threading.enumerate()
    ))

def worker():
    showthreadinfo()
    for i in range(5):
        time.sleep(1)
        print('I am working')
    print('finished')

t = threading.Thread(target=worker,name='worker')
showthreadinfo()
time.sleep(1)
t.start()

print('==end==')






