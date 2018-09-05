
from BOT import runFromFight
from BOT import optimalPath1
from BOT import kill
from BOT import catchem
from scapy.all import *

count = 0

p = open('parse', 'w')
new = rdpcap('C:/Users/rquis/Desktop/packet/hur.pcap')
newnew = open('C:/Users/rquis/Desktop/packet/hur.pcap', encoding='ISO-8859-1')
newest = newnew.readlines()
srcPort = 9339
destPort = '26433'
srcIP = '158.69.125.191'
destIP = '192.168.43.16'


#for line in newest:
 #   print(line)



while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((srcIP, srcPort))
    data = s.recv(200)
    optimalPath1(count)



    for line in newnew:
        print(line)
        if 'pmsg' in line:
            continue
        if 'Graveler' in line:
            kill()
        elif 'Golbat' in line:
            runFromFight()
        elif 'Sandslash' in line:
            kill()
        elif 'Marowalk' in line:
            exit()
        elif 'Machop' in line:
            exit()
        elif 'Machoke' in line:
            exit()
        elif 'Onix' in line:
            exit()






#    elif '---*' in line or '*---' in line or '_*)'  in line:
  #          runFromFight()

