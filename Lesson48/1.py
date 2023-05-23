import socks
import socket

from urllib.request import urlopen
#
socks.set_default_proxy(socks.SOCKS5,'localhost',9150)
socket.socket = socks.socksocket

answer = urlopen('https://icanhazip.com/').read()
print(answer)

