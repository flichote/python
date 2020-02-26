import threading

def worker():
    print("I am working")
    print("fineshed")

    
t = threading.Thread(target=worker,name = 'worker')

t.start()

