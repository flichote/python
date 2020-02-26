import threading
import time
"""该函数的线程也是能正常执行，知道打印  ==end==  到主进程结束！！"""
def add(x,y):
    print('{} + {} = {}'.format(x,y,x+y,threading.current_thread().ident))

t1 = threading.Thread(target=add,name = 'add',args=(4,5))

t1.start()
print('t1_______')
time.sleep(2)

t2 = threading.Thread(target=add, name='add', args=(6,),kwargs={'y':7})

t2.start()
time.sleep(2)
print('t2~~~~~~~~~~~')

t3 = threading.Thread(target=add,name='add',args=(8,),kwargs={'y':9})
time.sleep(2)
t3.start()

print('t3~~~~~~~~~')
print("==end==")

