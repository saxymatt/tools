import socket, threading, time
from queue import Queue

print_lock = threading.Lock()

target = 'hackthissite.org'

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port',port,'is open!')
        con.close()
    except:
        pass
    
def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

q = Queue()

for x in range(500):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start_time = time.time()

for worker in range(1025):
    q.put(worker)

q.join()

print('The port scan took: ',time.time()-start_time)
