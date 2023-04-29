from urllib.parse import urljoin
import json
import http.client
import re
import requests


def postScript( url,payload):
    connection = http.client.HTTPSConnection("script.googleusercontent.com")
    headers = { 'Content-Type': 'application/json' }
    connection.request("POST", url,payload, headers)
    response = connection.getresponse()
    location_header = response.getheader('location')
    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return postScript(location,payload)


def getBalance(start=None,end=None):
    if (start==None and end==None):
        balances=[]
        for user in data:
            # print(user["name"],"=",end="")
            balances.append(balance(user["cookieIn"]))
        url = 'https://script.google.com/macros/s/AKfycbzWpDEJTSJRw2Dn9S1l357-rcTBQLd6ZZOzQZyn6a7yNQCmIKMmtT4iVdRlcSi3b2hWkg/exec'
        response = requests.post(url, json.dumps(balances))
        print(response.text)

    elif(end==None):
        print(data[start-1]["name"],end="=")
        balance(data[start-1]["cookieIn"])
    else:
        for i in range(start-1,end):
            # print(data[i]["name"],"=",end="")
            balance(data[i]["cookieIn"])


def balance(cookie):
    conn = http.client.HTTPSConnection("www.bing.com")
    payload = ''
    headers = {
    'authority': 'www.bing.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookie,
    'origin': 'https://www.bing.com',
    'referer': 'https://www.bing.com',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"112.0.1722.46"',
    'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.87", "Microsoft Edge";v="112.0.1722.46", "Not:A-Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-ms-gec-version': '1-112.0.1722.46',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46'
    }
    try:
        conn.request("POST", "/rewardsapp/reportActivity", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data=data.decode("utf-8")
        balance = re.search(r'"Balance":(\d+)', data).group(1)
        print(balance)
        return(balance)
    except:
        print("failed")
        return("")


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

url = "/macros/s/AKfycbylr-wMNGwyOHi7yrD1pMGoD5ixLZ_3BVeD_T2rWREdr1z-fPlaDeuntEsnAghAloDUEQ/exec"
response = getScript(url)
data=json.loads(response.read())

getBalance()