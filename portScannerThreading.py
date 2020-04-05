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

#If you want to prompt the user for port numbers
#while True:
#       try:
#           ports = input('Enter number of ports to scan: ')
#           if int(ports) <= 0 or int(ports) > 65535:
#               raise ValueError
#           break
#       except ValueError:
#          print("Invalid port number. Must be in the range of 1-65535.")
#
#print('Scanning ports 1-',ports,sep='')