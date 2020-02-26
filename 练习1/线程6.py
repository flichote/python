import threading
import time
"""该实验验证了线程只能开启一次"""

def worker():
    for i in range(5):
        time.sleep(1)
        print('I am working')

    print('finished')

t = threading.Thread(target=worker,name='worker')
print(t.name,t.ident)
time.sleep(1)


t.start()

print('==end==')

while True:
    time.sleep(1)
    print('{} {} {}'.format(t.name,t.ident,'alive' if t.is_alive() else 'dead'))

    if not t.is_alive():
        print('{} restart'.format(t.name))
        t.start()




