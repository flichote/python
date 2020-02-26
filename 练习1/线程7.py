import threading
import  time

def worker():
    for i in range(5):
        time.sleep(1)
        print('I am working')

    print('finished')

class MyTheath(threading.Thread):
    def start(self):
        print('start~~~~~')
        super().start()

    def run(self):
        print('run~~~~~~')
        super().run()

t = MyTheath(target=worker,name='worker')

t.start()

