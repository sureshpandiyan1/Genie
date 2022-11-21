import requests, json, shutil
import bs4
import os,re, string, random
import re, urllib
from functools import partial
import dragon_form_validator

class genies():


    def g_rdthat(**kwargs):
        with open(kwargs['pth'],encoding=kwargs['encodes']) as k: 
            GTEXT = k.readlines()
        return GTEXT


    def g_jthat(data):
        try:
            with open("./app/tlkbk/genierply.json",encoding="utf8") as k: 
                GTEXT = json.loads(k.read())
                z = dict(GTEXT)
                return z[data]
        except:
            print("genie tlk-back were not found")
        finally:
            print("genie is talking to you ...")


    def g_np(name):
        try:
            p = name[0].split(" ")[-1]
            name = p
            url = f"https://www.npmjs.com/package/{name}"
            urls_end = url.split("/")[-1]
            ll = requests.get(url)
            llz = ll.text
            z = os.environ["USERPROFILE"]+ "\Desktop\{0}.html".format(urls_end)
            with open(z, "w", encoding="utf8") as m:
                print(llz, file=m)
        except:
            print("something went wrong due your package not found or too many requests")


    def g_fontscale(b):
        try:
            for y in range(1):
                p = []
                zz = 16 / b
                p.append(zz)
                [p.append(p[m] * b) for m in range(0, 9)]
                p  = [round(p[0]) / b] + p
                x =  "".join([str(xx)+"px \n"   for xx in p]).strip()
                return p
        except:
            print("only 12 gd system allowed")


    def g_pkgdwld(n):
        try:
            s = n[0].split("pkg")[-1].strip()
            x = str(s).split(" ")
            name,version = str(s).split(" ")[0],x[1]
            response = requests.get(f"https://registry.npmjs.org/{name}/-/{name}-{version}.tgz", stream=True)
            if response.status_code == 200:
                with open(os.environ["USERPROFILE"] + f"\Desktop\{name}-{version}.tgz".format(name), 'wb') as filerd:
                    shutil.copyfileobj(response.raw, filerd)
        except:
            print("something went wrong ,due to internet connection not turned on")


    def g_hashtg(hashy):
        try:
            hashy= str(hashy).split(" ")[-1].replace("']","")
            usersearch = hashy; 
            usersearch = re.sub('#', '%23', usersearch)
            find_username = f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended" \
                            f"&query={usersearch}&rank_token=0.2712077074231197&include_reel=true "
            bs = requests.get(find_username, headers={"X-IG-App-ID": "936619743392459"})
            ps = json.loads(bs.text); 
            myhash = []
            totalhashtags = len(ps['hashtags']) - 1
            for m in range(0, totalhashtags + 1):
                hashname = ps['hashtags'][m]['hashtag']['name']
                print(hashname)
                mediaposts = ps['hashtags'][m]['hashtag']['search_result_subtitle']
                myhash.append('#' + hashname + "     " + mediaposts)
            with open( os.environ["USERPROFILE"]+ "\Desktop\{0}.txt".format(hashy), "w", encoding="utf8") as zz:
                for x in myhash:
                    print('%s\n' % (x), file=zz)
        except:
            print("something went wrong ,due to many requests")
        
    def g_cssoneliner(mm):
        try:
            pth = mm[0].split("css")[1]
            pp = str(pth).split("\\")
            pth = "/".join(pp) + "css"
            cs = pp[-1]
            css_save = []
            print(pth)
            with open(pth.strip(),"r") as css:
                for source in css:
                    css_save.append(source.strip())
                with open(os.environ["USERPROFILE"]+ "\Desktop\{0}css".format(cs), "w", encoding="utf8") as zz:
                    zz.write(' '.join(css_save))
        except:
            print("something went wrong due to  path is incorrect or file were not found")

    def g_chkmail(cc):
        try:
            cc = cc[0].split(" ")[-1]
            if dragon_form_validator.checks('mail',cc):
                msg = cc + " - valid mail"
            else:
                msg = cc + " - not valid mail, maybe not valid vendor"
            with open(os.environ["USERPROFILE"]+ "\Desktop\{0}.txt".format(cc), "w", encoding="utf8") as zz:
                    zz.write(msg)
        except:
            print("something went wrong due to email not valid in our vendor list")


    def g_gdsytm(c):
        try:
            c = c[0].split(" ")[1]
            c = int(c)
            p = []; g = []
            for i in range(1,c + 1):
                yy = round(80 * i + 20 * i - 20) / int(c) * 1
                p.append(yy)
                g.append(i)
            z = "".join([".gd-%s { width: %spx } \n" % (y,x) for x,y in zip(p,g)])
            with open(os.environ["USERPROFILE"] + "\Desktop\{0}".format(str(c)+"gd.css"),"w") as m:
                print(z,file=m)
        except:
            print("you are not typed cmnds properly")


    def g_crtrndm():
        try:
            x = {x:z for x,z in zip(list(string.ascii_letters)[0:round(len(list(string.ascii_letters)) / 2)], [i for i in range (0, round(len(list(string.ascii_letters)) / 2))]) }
            zx = {z:u for u,z in zip(list(string.ascii_letters)[0:round(len(list(string.ascii_letters)) / 2)], [i for i in range (0, round(len(list(string.ascii_letters)) / 2))]) }
            p = []
            storethat = []
            for z in list(y for y in string.ascii_letters * 3):
                try: p.append(x[z])
                except: pass
            for y in p:
                try: storethat.append(str([i for i in range(1,len(p))][y - random.randint(0,7)] + [i for i in range(1,len(p))][y]))
                except: pass
            zzz = []
            for mm in storethat:
                try: zzz.append("".join([s for s in zx[int(mm)]]))
                except:pass
            zu = "".join(zzz)
            for y in range(0,len(zu), len(zu) // 1):
                pp = list(zu[y: y + len(zu) // random.randint(10,23)][::-1] + zu[y: y + len(zu)][::-1])
                zzx = [x[random.choice(xg)]  for xg in pp]
                plk = {m:j for j,m in zip(list(string.punctuation),range(0, len(list(string.punctuation)) - 5))  }
                kjk = [plk[lkz] for lkz in zzx ]
                kj = [zx[lkz] for lkz in zzx ]
                how = list(kjk) + list(kj)
                how = "".join(set(how))
                chkz = {'key': how}
            z = os.environ["USERPROFILE"]+ r"\Desktop\randompass.txt"
            with open(z, "w+", encoding="utf8") as m:
                print(chkz['key'], file=m)
        except:
            print("you are not typed cmnds properly")
            
    def g_card(types):
        q = types
        def choosethecard(select):
            if select == 1: return str(random.randint(4000500030005000, 4600600050006000))
            if select == 2: return str(random.randint(5004003002001000, 5506006006005000))
        i = 0
        while i < 2:
            rand_num =choosethecard(q); s = ''.join(str(rand_num))
            cds = s[0:16:2]
            sortth = [int(cds[0]) + int(cds[0]), int(cds[1]) + int(cds[1]), int(cds[2]) + int(cds[2]),
                int(cds[3]) + int(cds[3]), int(cds[4]) + int(cds[4]), int(cds[5]) + int(cds[5]),
                int(cds[6]) + int(cds[6]), int(cds[7]) + int(cds[7])]

            now = [m for m in sortth]
            def sorter(j):
                if j > 9:
                    x = str(j)[0:1]
                    y = str(j)[1:2]
                    z = int(x) + int(y)
                    return z
                else:
                    return j
            cps = ''.join([str(sorter(cards)) for cards in now])
            alls = int(cps[0]) + int(rand_num[1]) + int(cps[1]) + int(rand_num[3]) + int(cps[2]) + int(rand_num[5]) + int(
                cps[3]) + int(rand_num[7]) + int(cps[4]) + int(rand_num[9]) + int(cps[5]) + int(rand_num[11]) + int(
                cps[6]) + int(rand_num[13]) + int(cps[7]) + int(rand_num[15])
            def makesurepass():
                try:
                    if int(str(alls)[1:2]) == 0: return "pass"
                    else: return "failed"
                except:
                    if int(str(alls)[2:3]) == 0: return "pass"
                    else: return "fail"
            if makesurepass() == "pass":
                ll  = {1: "dummyvisa.txt", 2: "dummymaster.txt"}
                z = os.environ["USERPROFILE"]+ r"\Desktop\{0}".format(ll[types])
                with open(z, "w+", encoding="utf8") as m:
                    print(s, file=m)
                break

