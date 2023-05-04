from urllib.parse import urljoin
import json
import http.client
import random
import time
import threading

import logging
import logging.handlers


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


def getScript( url):
    connection = http.client.HTTPSConnection("script.googleusercontent.com")
    connection.request('GET', url)
    response = connection.getresponse()
    location_header = response.getheader('location')
    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return getScript(location)

def processUsPc(cookie,num):        
    for x in range(num):
        rex=randomWords()
        conn = http.client.HTTPSConnection("www.bing.com")
        payload = ''
        headers = {
        'authority': 'www.bing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
        'referer': 'https://www.bing.com/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"112.0.1722.48"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.62", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.149"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-ms-gec-version': '1-112.0.1722.48',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        }
        try:
            conn.request("GET", "/search?q={}&form=QBLH&sp=-1&lq=0&pq=ho&sc=10-2&qs=n&sk=&cvid=90CF49F0576D4345A610043476ACEAAC&ghsh=0&ghacc=0&ghpl=".format(rex), payload, headers)
            res = conn.getresponse()
            time.sleep(1)
        except:
            logger.info("failed")
            logger.info(x)

def processUsMob(cookie,num):        
    for x in range(num):
        rex=randomWords()
        conn = http.client.HTTPSConnection("www.bing.com")
        payload = ''
        headers = {
              'authority': 'www.bing.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'accept-language': 'en-US,en;q=0.9',
              'cookie':cookie,
              'referer': 'https://www.bing.com/?toWww=1&redig=07042FBC5A774C3CA0AB5E7DE7789776',
              'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
              'sec-ch-ua-arch': '""',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-full-version': '"112.0.1722.58"',
              'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Microsoft Edge";v="112.0.1722.58", "Not:A-Brand";v="99.0.0.0"',
              'sec-ch-ua-mobile': '?1',
              'sec-ch-ua-model': '"Pixel 5"',
              'sec-ch-ua-platform': '"Android"',
              'sec-ch-ua-platform-version': '"11"',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-user': '?1',
              'sec-ms-gec-version': '1-112.0.1722.58',
              'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/112.0.0.0'
            }
        try:
            conn.request("GET", "/search?q={}&form=QBLH&rdr=1&rdrig=0C42BFEA1B6348AE99B724BE42E6E363".format(rex), payload, headers)
            res = conn.getresponse()
            time.sleep(1)
        except:
            logger.info("failed")
            logger.info(x)


def runUsPc(pcNum,start=None,end=None):
    logger.info("running pc")
    if (start==None and end==None):
        for user in data:
            processUsPc(user["cookieUs"],pcNum)
    elif(end==None):
        processUsPc(data[start-1]["cookieUs"],pcNum)
    else:
        for i in range(start-1,end):
            processUsPc(data[i]["cookieUs"],pcNum)

def runUsMob(MobNum,start=None,end=None):
    logger.info("running Us mob")
    if (start==None and end==None):
        for user in data:
            processUsMob(user["cookieUs"],MobNum)
    elif(end==None):
        processUsMob(data[start-1]["cookieUs"],MobNum)
    else:
        for i in range(start-1,end):
            processUsMob(data[i]["cookieUs"],MobNum)

def randomWords():
    sentence=''
    for i in range(3):
        sentence += random.choice(words)
        if(i<2):
            sentence+="+"
    return(sentence)

def getWords():  
    conn = http.client.HTTPSConnection("svnweb.freebsd.org")
    path = "/csrg/share/dict/words?view=co&content-type=text/plain"
    conn.request("GET", path)
    response = conn.getresponse()
    long_txt = response.read().decode()
    return(long_txt.splitlines())

words = getWords()

url = "/macros/s/AKfycbylr-wMNGwyOHi7yrD1pMGoD5ixLZ_3BVeD_T2rWREdr1z-fPlaDeuntEsnAghAloDUEQ/exec"
response = getScript(url)
data=json.loads(response.read())
#ht
conn = http.client.HTTPSConnection("httpbin.org")
conn.request("GET", "/ip")

res = conn.getresponse()
data1 = res.read().decode("utf-8")
ip_address = json.loads(data1)['origin']

logger.info( ip_address)

logger.info("test")

t1 = threading.Thread(target=runUsPc, args=(35,1,25))
t2 = threading.Thread(target=runUsPc, args=(35,26,50))
t3 = threading.Thread(target=runUsPc, args=(35,51,53))
# t4 = threading.Thread(target=runUsPc, args=(35,76,100))
t1.start()
t2.start()
t3.start()
# t4.start()
t1.join()
t2.join()
t3.join()
# t4.join()
t1 = threading.Thread(target=runUsMob, args=(22,1,25))
t2 = threading.Thread(target=runUsMob, args=(22,26,50))
t3 = threading.Thread(target=runUsMob, args=(22,51,53))
# t4 = threading.Thread(target=runUsMob, args=(22,76,100))
t1.start()
t2.start()
t3.start()
# t4.start()
t1.join()
t2.join()
t3.join()
# t4.join()

