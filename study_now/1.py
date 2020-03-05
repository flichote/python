
import threading
import  logging
import datetime
import socket

logging.basicConfig(level=logging.INFO,format="%s(asctime)s %(thread)d %(message)s")

class ChatServer:
    def __init__(self,ip='127.0.0.1',port=9999):
        self.sock = socket.socket()
        self.addr = (ip,port)
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        # accept
        threading.Thread(target=self.accept).start()

    def accept(self):
        while not self.event.is_set():
            sock,client = self.sock.accept()
            self.clients[client] = sock

            threading.Thread(target=self.recv,args=(sock,client)).start()


    def recv(self,sock:socket.socket,client):
        while not self.event.is_set():
            data = sock.recv(1024)
            msg = "{:%Y/%m/%d  %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(),*client,data.decode())
            logging.info(msg)
            msg = msg.encode()
            for s in self.clients.values():
                s.send(msg)

    def stop(self):
        self.event.set()
        for s in self.clients.values():
            s.close()
        self.sock.close()

cs = ChatServer()
cs.start()

while True:
    cmd = input('>>').strip()
    if cmd == 'quit':
        cs.stop()
        threading.Event().wait(3)
        break









