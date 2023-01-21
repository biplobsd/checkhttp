import requests
import re

def getIps():
    data = ''
    with open('data.txt') as r:
        data = r.read()
    
    return re.findall(r'Open\s(.+)', data, re.M)

def checkBr(ip, s=False):
    try:
        ips = 'http'+ ('s' if s else '') +'://'+ip
        if requests.get(ips, timeout=1).raw:
            return True, ips
    except:
        pass
    return False, ''

if __name__=='__main__':
    for i in getIps():
        print('.', end='', flush=True)
        r = checkBr(i)
        if r[0]:
            print()
            print(r[1])
        
        rs = checkBr(i, True)
        if rs[0]:
            print()
            print(r[1])
