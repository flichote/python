import threading
import time
import selectors
import optparse
# import pymysql





import pyexpat


#
#
# import socket
#
# socket.gethostbyname()
# ss = selectors.EpollSelector

"""该线程会一直打印I am working,不会打印fineshed"""

def worker():
    while True:
        time.sleep(1)
        print("I am working")
    print("fineshed")

t = threading.Thread(target=worker,name='worker')
t.start()