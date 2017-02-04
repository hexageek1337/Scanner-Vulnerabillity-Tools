#!/usr/bin/python

# Recoded by H3xagon from Cyber Merah Putih

#  Copyright Do Not Change  #
#    Thanks to T1KUS90T     #

import sys
from urllib.request import urlopen
import time
from socket import timeout
import urllib.parse, urllib.error

def timer():

    now = time.localtime(time.time())

    return time.asctime(now)


def slowprint(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush() # defeat buffering

        time.sleep(95./3169)

slowprint('''
  -----------------------------------------------------------
 |                                                          |____
 |      #     #  #####                                           |
 |      #     # #     # #    #   ##    ####   ####  #    #       |
 |      #     #       #  #  #   #  #  #    # #    # ##   #       |
 |      #######  #####    ##   #    # #      #    # # #  #       |
 |      #     #       #   ##   ###### #  ### #    # #  # #       |
 |      #     # #     #  #  #  #    # #    # #    # #   ##       |
 |      #     #  #####  #    # #    #  ####   ####  #    #       |
 |                                                               |
 |                            Powered by Cyber Merah Putih       |
 |  [ Scanner Tools ]                    ( Denny Septian )       |
 |                                                               |
  ----------------------------------------------------------------
''')

hexaa_pilih = input("\n[+] 1.Wordpress Theme Scanner\n[+] 2.Wordpress Plugin Scanner\n[+] 3.Joomla! Component Scanner\n[+] 4.Admin Login Finder\n\nChoose one : ")

# Theme Scanner
if hexaa_pilih == "1":
    thm = input("Input target:")
    print("\n[+] Target:",thm)
    print("[+] Scanning...")
    if not thm.startswith("http://"):
        thm = "http://"+thm
    magazine = thm+"/wp-content/themes/magazine"
    bizco = thm+"/wp-content/themes/bizco"
    suco = thm+"/wp-content/themes/suco"
    agency = thm+"/wp-content/themes/agency"
    koi = thm+"/wp-content/themes/koi"
    grido = thm+"/wp-content/themes/grido"
    education = thm+"/wp-content/themes/education"
    appius = thm+"/wp-content/themes/appius/"
    archin = thm+"/wp-content/themes/archin/"
    simfo = thm+"/wp-content/themes/simfo"
    radial = thm+"/wp-content/themes/radial-theme"
    echea = thm+"/wp-content/themes/echea/"
    reganto = thm+"/wp-content/themes/reganto-theme"
    rockstar = thm+"/wp-content/themes/rockstar-theme"
    elemin = thm+"/wp-content/themes/elemin"
    rayoflight = thm+"/wp-content/themes/rayoflight-theme"
    oxygen = thm+"/wp-content/themes/oxygen-theme"
    basic = thm+"/wp-content/themes/basic"
    bordeaux = thm+"/wp-content/themes/bordeaux-theme"
    wigi = thm+"/wp-content/themes/wigi"
    bulteno = thm+"/wp-content/themes/bulteno-theme"
    agritourismo = thm+"/wp-content/themes/agritourismo-theme/"
    wumblr = thm+"/wp-content/themes/wumblr"
    blogfolio = thm+"/wp-content/themes/blogfolio"
    minblr = thm+"/wp-content/themes/minblr"
    funki = thm+"/wp-content/themes/funki"
    folo = thm+"/wp-content/themes/folo"
    newsy = thm+"/wp-content/themes/newsy"
    responz = thm+"/wp-content/themes/responz"
    slide = thm+"/wp-content/themes/slide"
    parallax = thm+"/wp-content/themes/parallax"
    tisa = thm+"/wp-content/themes/tisa"
    bold = thm+"/wp-content/themes/bold"
    postline = thm+"/wp-content/themes/postline"
    qualifire = thm+"/wp-content/themes/qualifire"
    thisway = thm+"/wp-content/themes/ThisWay"
    metro = thm+"/wp-content/themes/metro"
    rezo = thm+"/wp-content/themes/rezo"
    pinboard = thm+"/wp-content/themes/pinboard"
    kmp = thm+"/wp-content/themes/kmp/"
    strange = thm+"/wp-content/themes/ut-strange"
    ghost = thm+"/wp-content/themes/Ghost"
    minshop = thm+"/wp-content/themes/minshop"
    area = thm+"/wp-content/themes/area53"
    purevision = thm+"/wp-content/themes/purevision"
    liberal = thm+"/wp-content/themes/liberal/"
    udesign = thm+"/wp-content/themes/u-design"
    shopsum = thm+"/wp-content/themes/shopsum/"
    ninetofive = thm+"/wp-content/themes/ninetofive"
    shotzz = thm+"/wp-content/themes/shotzz/"
    majestics = thm+"/wp-content/themes/majestics/"
    village = thm+"/wp-content/themes/village"
    travelify = thm+"/wp-content/themes/travelify"
    scanmaje = urlopen(majestics)
    scanshot = urlopen(shotzz)
    scanshop = urlopen(shopsum)
    scanlib = urlopen(liberal)
    scanqual = urlopen(qualifire)
    scankm = urlopen(kmp)
    scansim = urlopen(simfo)
    scanvill = urlopen(village)
    scangrid = urlopen(grido)
    scansuc = urlopen(suco)
    scanrez = urlopen(rezo)
    scanbiz = urlopen(bizco)
    scanmin = urlopen(minshop)
    scanec = urlopen(echea)
    scanslid = urlopen(slide)
    scanbol = urlopen(bold)
    scanpost = urlopen(postline)
    scanpin = urlopen(pinboard)
    scanmet = urlopen(metro)
    scanrez = urlopen(responz)
    scanpara = urlopen(parallax)
    scanrock = urlopen(rockstar)
    scantis = urlopen(tisa)
    scanblog = urlopen(blogfolio)
    scanel = urlopen(elemin)
    scannew = urlopen(newsy)
    scanbas = urlopen(basic)
    scanwum = urlopen(wumblr)
    scanfol = urlopen(folo)
    scanfunk = urlopen(funki)
    scanminb = urlopen(minblr)
    scanagri = urlopen(agritourismo)
    scanwig = urlopen(wigi)
    scanborde = urlopen(bordeaux)
    scanbul = urlopen(bulteno)
    scanrad = urlopen(radial)
    scanox = urlopen(oxygen)
    scanarc = urlopen(archin)
    scanapi = urlopen(appius)
    scanray = urlopen(rayoflight)
    scanmag = urlopen(magazine)
    scanreg = urlopen(reganto)
    scanudes = urlopen(udesign)
    scanare = urlopen(area)
    scanagn = urlopen(agency)
    scannine = urlopen(ninetofive)
    scanstrang = urlopen(strange)
    scanthis = urlopen(thisway)
    scanko = urlopen(koi)
    scanghos = urlopen(ghost)
    scanpure = urlopen(purevision)
    scanedu = urlopen(education)
    scantrave = urlopen(travelify)
    if scanvill.getcode() == 200:
        print("[+] Found:",village)
    elif scanvill.getcode() == 403:
        print("[+] Forbidden:",village)
    elif scanvill.getcode() == 500:
        print("[+] Server Error:",village)
    else:
        print("[-] Not found!:",village)
    if scantrave.getcode() == 200:
    	print("[+] Found :",travelify)
    elif scantrave.getcode() == 403:
    	print("[+] Forbidden :",travelify)
    elif scantrave.getcode() == 500:
    	print("[+] Server Error :",travelify)
    else:
    	print("[+] Not found! :",travelify)
    if scanghos.getcode() == 200:
        print("[+] Found:",ghost)
    elif scanghos.getcode() == 403:
        print("[+] Forbidden:",ghost)
    elif scanghos.getcode() == 500:
        print("[+] Server Error:",ghost)
    else:
        print("[-] Not found!:",ghost)
    if scanstrang.getcode() == 200:
        print("[+] Found:",strange)
    elif scanstrang.getcode() == 403:
        print("[+] Forbidden:",strange)
    elif scanstrang.getcode() == 500:
        print("[+] Server Error:",strange)
    else:
        print("[-] Not found!:",strange)
    if scanpure.getcode() == 200:
        print("[+] Found:",purevision)
    elif scanpure.getcode() == 403:
        print("[+] Forbidden:",purevision)
    elif scanpure.getcode() == 500:
        print("[+] Server Error:",purevision)
    else:
        print("[-] Not found!:",purevision)
    if scanthis.getcode() == 200:
        print("[+] Found:",thisway)
    elif scanthis.getcode() == 403:
        print("[+] Forbidden:",thisway)
    elif scanthis.getcode() == 500:
        print("[+] Server Error:",thisway)
    else:
        print("[-] Not found!:",thisway) 
    if scannine.getcode() == 200:
        print("[+] Found:",ninetofive)
    elif scannine.getcode() == 403:
        print("[+] Forbidden:",ninetofive)
    elif scannine.getcode() == 500:
        print("[+] Server Error:",ninetofive)
    else:
        print("[-] Not found!:",ninetofive)
    if scanare.getcode() == 200:
        print("[+] Found:",area)
    elif scanare.getcode() == 403:
        print("[+] Forbidden:",area)
    elif scanare.getcode() == 500:
        print("[+] Server Error:",area)
    else:
        print("[-] Not found!:",area)
    if scanudes.getcode() == 200:
        print("[+] Found:",udesign)
    elif scanudes.getcode() == 403:
        print("[+] Forbidden:",udesign)
    elif scanudes.getcode() == 500:
        print("[+] Server Error:",udesign)
    else:
        print("[-] Not found!:",udesign)
    if scanqual.getcode() == 200:
        print("[+] Found:",qualifire)
    elif scanqual.getcode() == 403:
        print("[+] Forbidden:",qualifire)
    elif scanqual.getcode() == 500:
        print("[+] Server Error:",village)
    else:
        print("[-] Not found!:",village)
    if scanrock.getcode() == 200:
        print("[+] Found:",rockstar)
    elif scanrock.getcode() == 403:
        print("[+] Forbidden:",rockstar)
    elif scanrock.getcode() == 500:
        print("[+] Server Error:",rockstar)
    else:
        print("[-] Not found!:",rockstar)
    if scanreg.getcode() == 200:
        print("[+] Found:",reganto)
    elif scanreg.getcode() == 403:
        print("[+] Forbidden:",reganto)
    elif scanreg.getcode() == 500:
        print("[+] Server Error:",reganto)
    else:
        print("[-] Not found!:",reganto)
    if scanray.getcode() == 200:
        print("[+] Found:",rayoflight)
    elif scanray.getcode() == 403:
        print("[+] Forbidden:",rayoflight)
    elif scanray.getcode() == 500:
        print("[+] Server Error:",rayoflight)
    else:
        print("[-] Not found!:",rayoflight)
    if scanrad.getcode() == 200:
        print("[+] Found:",radial)
    elif scanrad.getcode() == 403:
        print("[+] Forbidden:",radial)
    elif scanrad.getcode() == 500:
        print("[+] Server Error:",radial)
    else:
        print("[-] Not found!:",radial)
    if scanox.getcode() == 200:
        print("[+] Found:",oxygen)
    elif scanox.getcode() == 403:
        print("[+] Forbidden:",oxygen)
    elif scanox.getcode() == 500:
        print("[+] Server Error:",oxygen)
    else:
        print("[-] Not found!:",oxygen)
    if scanbul.getcode() == 200:
        print("[+] Found:",bulteno)
    elif scanbul.getcode() == 403:
        print("[+] Forbidden:",bulteno)
    elif scanbul.getcode() == 500:
        print("[+] Server Error:",bulteno)
    else:
        print("[-] Not found!:",bulteno)
    if scanborde.getcode() == 200:
        print("[+] Found:",bordeaux)
    elif scanborde.getcode() == 403:
        print("[+] Forbidden:",bordeaux)
    elif scanborde.getcode() == 500:
        print("[+] Server Error:",bordeaux)
    else:
        print("[-] Not found!:",bordeaux)
    if scanagri.getcode() == 200:
        print("[+] Found:",agritourismo)
    elif scanagri.getcode() == 403:
        print("[+] Forbidden:",agritourismo)
    elif scanagri.getcode() == 500:
        print("[+] Server Error:",agritourismo)
    else:
        print("[-] Not found!:",agritourismo)
    if scanblog.getcode() == 200:
        print("[+] Found:",blogfolio)
    elif scanblog.getcode() == 403:
        print("[+] Forbidden:",blogfolio)
    elif scanblog.getcode() == 500:
        print("[+] Server Error:",blogfolio)
    else:
        print("[-] Not found!:",blogfolio)
    if scanwig.getcode() == 200:
        print("[+] Found:",wigi)
    elif scanwig.getcode() == 403:
        print("[+] Forbidden:",wigi)
    elif scanwig.getcode() == 500:
        print("[+] Server Error:",wigi)
    else:
        print("[-] Not found!:",wigi)
    if scanwum.getcode() == 200:
        print("[+] Found:",wumblr)
    elif scanwum.getcode() == 403:
        print("[+] Forbidden:",wumblr)
    elif scanwum.getcode() == 500:
        print("[+] Server Error:",wumblr)
    else:
        print("[-] Not found!:",wumblr)
    if scannew.getcode() == 200:
        print("[+] Found:",newsy)
    elif scannew.getcode() == 403:
        print("[+] Forbidden:",newsy)
    elif scannew.getcode() == 500:
        print("[+] Server Error:",newsy)
    else:
        print("[-] Not found!:",newsy)
    if scanminb.getcode() == 200:
        print("[+] Found:",minblr)
    elif scanminb.getcode() == 403:
        print("[+] Forbidden:",minblr)
    elif scanminb.getcode() == 500:
        print("[+] Server Error:",minblr)
    else:
        print("[-] Not found!:",minblr)
    if scanfunk.getcode() == 200:
        print("[+] Found:",funki)
    elif scanfunk.getcode() == 403:
        print("[+] Forbidden:",funki)
    elif scanfunk.getcode() == 500:
        print("[+] Server Error:",funki)
    else:
        print("[-] Not found!:",funki)
    if scanfol.getcode() == 200:
        print("[+] Found:",folo)
    elif scanfol.getcode() == 403:
        print("[+] Forbidden:",folo)
    elif scanfol.getcode() == 500:
        print("[+] Server Error:",folo)
    else:
        print("[-] Not found!:",folo)
    if scanel.getcode() == 200:
        print("[+] Found:",elemin)
    elif scanel.getcode() == 403:
        print("[+] Forbidden:",elemin)
    elif scanel.getcode() == 500:
        print("[+] Server Error:",elemin)
    else:
        print("[-] Not found!:",elemin)
    if scantis.getcode() == 200:
        print("[+] Found:",tisa)
    elif scantis.getcode() == 403:
        print("[+] Forbidden:",tisa)
    elif scantis.getcode() == 500:
        print("[+] Server Error:",tisa)
    else:
        print("[-] Not found!:",tisa)
    if scanrez.getcode() == 200:
        print("[+] Found:",responz)
    elif scanrez.getcode() == 403:
        print("[+] Forbidden:",responz)
    elif scanrez.getcode() == 500:
        print("[+] Server Error:",responz)
    else:
        print("[-] Not found!:",responz)
    if scanbas.getcode() == 200:
        print("[+] Found:",basic)
    elif scanbas.getcode() == 403:
        print("[+] Forbidden:",basic)
    elif scanbas.getcode() == 500:
        print("[+] Server Error:",basic)
    else:
        print("[-] Not found!:",basic)
    if scanpara.getcode() == 200:
        print("[+] Found:",parallax)
    elif scanpara.getcode() == 403:
        print("[+] Forbidden:",parallax)
    elif scanpara.getcode() == 500:
        print("[+] Server Error:",parallax)
    else:
        print("[-] Not found!:",parallax)
    if scanbol.getcode() == 200:
        print("[+] Found:",bold)
    elif scanbol.getcode() == 403:
        print("[+] Forbidden:",bold)
    elif scanbol.getcode() == 500:
        print("[+] Server Error:",bold)
    else:
        print("[-] Not found!:",bold)
    if scanmet.getcode() == 200:
        print("[+] Found:",metro)
    elif scanmet.getcode() == 403:
        print("[+] Forbidden:",metro)
    elif scanmet.getcode() == 500:
        print("[+] Server Error:",metro)
    else:
        print("[-] Not found!:",metro)
    if scanslid.getcode() == 200:
        print("[+] Found:",slide)
    elif scanslid.getcode() == 403:
        print("[+] Forbidden:",slide)
    elif scanslid.getcode() == 500:
        print("[+] Server Error:",slide)
    else:
        print("[-] Not found!:",slide)
    if scanpost.getcode() == 200:
        print("[+] Found:",postline)
    elif scanpost.getcode() == 403:
        print("[+] Forbidden:",postline)
    elif scanpost.getcode() == 500:
        print("[+] Server Error:",postline)
    else:
        print("[-] Not found!:",postline)
    if scanpin.getcode() == 200:
        print("[+] Found:",pinboard)
    elif scanpin.getcode() == 403:
        print("[+] Forbidden:",pinboard)
    elif scanpin.getcode() == 500:
        print("[+] Server Error:",pinboard)
    else:
        print("[-] Not found!:",pinboard)
    if scanmin.getcode() == 200:
        print("[+] Found:",minshop)
    elif scanmin.getcode() == 403:
        print("[+] Forbidden:",minshop)
    elif scanmin.getcode() == 500:
        print("[+] Server Error:",minshop)
    else:
        print("[-] Not found!:",minshop)
    if scansim.getcode() == 200:
        print("[+] Found:",simfo)
    elif scansim.getcode() == 403:
        print("[+] Forbidden:",simfo)
    elif scansim.getcode() == 500:
        print("[+] Server Error:",simfo)
    else:
        print("[-] Not found!:",simfo)
    if scanrez.getcode() == 200:
        print("[+] Found:",rezo)
    elif scanrez.getcode() == 403:
        print("[+] Forbidden:",rezo)
    elif scanrez.getcode() == 500:
        print("[+] Server Error:",rezo)
    else:
        print("[-] Not found!:",rezo)
    if scangrid.getcode() == 200:
        print("[+] Found:",grido)
    elif scangrid.getcode() == 403:
        print("[+] Forbidden:",grido)
    elif scangrid.getcode() == 500:
        print("[+] Server Error:",grido)
    else:
        print("[-] Not found!:",grido)
    if scanbiz.getcode() == 200:
        print("[+] Found:",bizco)
    elif scanbiz.getcode() == 403:
        print("[+] Forbidden:",bizco)
    elif scanbiz.getcode() == 500:
        print("[+] Server Error:",bizco)
    else:
        print("[-] Not found!:",bizco)
    if scansuc.getcode() == 200:
        print("[+] Found:",suco)
    elif scansuc.getcode() == 403:
        print("[+] Forbidden:",suco)
    elif scansuc.getcode() == 500:
        print("[+] Server Error:",suco)
    else:
        print("[-] Not found!:",suco)
    if scanmaje.getcode() == 200:
        print("[+] Found:",majestics)
    elif scanmaje.getcode() == 403:
        print("[+] Forbidden:",majestics)
    elif scanmaje.getcode() == 500:
        print("[+] Server Error:",majestics)
    else:
        print("[-] Not found!:",majestics)
    if scanshot.getcode() == 200:
        print("[+] Found:",shotzz)
    elif scanshot.getcode() == 403:
        print("[+] Forbidden:",shotzz)
    elif scanshot.getcode() == 500:
        print("[+] Server Error:",shotzz)
    else:
        print("[-] Not found!:",shotzz)
    if scanshop.getcode() == 200:
        print("[+] Found:",shopsum)
    elif scanshop.getcode() == 403:
        print("[+] Forbidden:",shopsum)
    elif scanshop.getcode() == 500:
        print("[+] Server Error:",shopsum)
    else:
        print("[-] Not found!:",shopsum)
    if scanlib.getcode() == 200:
        print("[+] Found:",liberal)
    elif scanlib.getcode() == 403:
        print("[+] Forbidden:",liberal)
    elif scanlib.getcode() == 500:
        print("[+] Server Error:",liberal)
    else:
        print("[-] Not found!:",liberal)
    if scanapi.getcode() == 200:
        print("[+] Found:",appius)
    elif scanapi.getcode() == 403:
        print("[+] Forbidden:",appius)
    elif scanapi.getcode() == 500:
        print("[+] Server Error:",appius)
    else:
        print("[-] Not found!:",appius)
    if scanarc.getcode() == 200:
        print("[+] Found:",archin)
    elif scanarc.getcode() == 403:
        print("[+] Forbidden:",archin)
    elif scanarc.getcode() == 500:
        print("[+] Server Error:",archin)
    else:
        print("[-] Not found!:",archin)
    if scanec.getcode() == 200:
        print("[+] Found:",echea)
    elif scanec.getcode() == 403:
        print("[+] Forbidden:",echea)
    elif scanec.getcode() == 500:
        print("[+] Server Error:",echea)
    else:
        print("[-] Not found!:",echea)
    if scankm.getcode() == 200:
        print("[+] Found:",kmp)
    elif scankm.getcode() == 403:
        print("[+] Forbidden:",kmp)
    elif scankm.getcode() == 500:
        print("[+] Server Error:",kmp)
    else:
        print("[-] Not found!:",kmp)    
    if scanedu.getcode() == 200:
        print("[+] Found:",education)
    elif scanedu.getcode() == 403:
        print("[+] Forbidden:",education)
    elif scanedu.getcode() == 500:
        print("[+] Server Error:",education)
    else:
        print("[-] Not found!:",education)
    if scanko.getcode() == 200:
        print("[+] Found:",koi)
    elif scanko.getcode() == 403:
        print("[+] Forbidden:",koi)
    elif scanko.getcode() == 500:
        print("[+] Server Error:",koi)
    else:
        print("[-] Not found!:",koi)
    if scanagn.getcode() == 200:
        print("[+] Found:",agency)
    elif scanagn.getcode() == 403:
        print("[+] Forbidden:",agency)
    elif scanagn.getcode() == 500:
        print("[+] Server Error:",agency)
    else:
        print("[-] Not found!:",agency)
    if scanmag.getcode() == 200:
        print("[+] Found:",magazine)
    elif scanmag.getcode() == 403:
        print("[+] Forbidden:",magazine)
    elif scanmag.getcode() == 500:
        print("[+] Server Error:",magazine)
    else:
        print("[-] Not found!:",magazine)
    sys.exit()


# Plugin Scanner
if hexaa_pilih == "2":
    plug = input("Input target:")
    print("\n[+] Target:",plug)
    print("[+] Scanning...")
    if not plug.startswith("http://"):
        plug = "http://"+plug
    simple = plug+"/wp-content/plugins/simple-ads-manager"
    wp3d = plug+"/wp-content/plugins/wp-3dflick-slideshow"
    fluid = plug+"/wp-content/plugins/fluid_forms"
    wpshop = plug+"/wp-content/plugins/wpshop"
    jqueryh = plug+"/wp-content/plugins/jquery-html5-file-upload"
    slideshow = plug+"/wp-content/plugins/slide-show-pro"
    easycom = plug+"/wp-content/plugins/easy-comment-uploads"
    comgallery = plug+"/wp-content/plugins/complete-galerry-manager"
    formcraft = plug+"/wp-content/plugins/formcraft"
    pitchprint = plug+"/wp-content/plugins/pitchprint"
    tevolution = plug+"/wp-content/plugins/Tevolution"
    wpmobile = plug+"/wp-content/plugins/wp-mobile-locator"
    scanwpmobil = urlopen(wpmobile)
    scanslides = urlopen(slideshow)
    scanwps = urlopen(wpshop)
    scanjquery = urlopen(jqueryh)
    scaneasy = urlopen(easycom)
    scansim = urlopen(simple)
    scancom = urlopen(comgallery)
    scanpitch = urlopen(pitchprint)
    scanform = urlopen(formcraft)
    scanwp3 = urlopen(wp3d)
    scanflu = urlopen(fluid)
    scantevo = urlopen(tevolution)
    if scanwpmobil.getcode() == 200:
        print("[+] Found:",wpmobile)
    elif scanwpmobil.getcode() == 403:
        print("[+] Forbidden:",wpmobile)
    elif scanwpmobil.getcode() == 500:
        print("[+] Server Error:",wpmobile)
    else:
       print("[-] Not found!:",wpmobile)

    if scanwps.getcode() == 200:
        print("[+] Found:",wpshop)
    elif scanwps.getcode() == 403:
        print("[+] Forbidden:",wpshop)
    elif scanwps.getcode() == 500:
        print("[+] Server Error:",wpshop)
    else:
       print("[-] Not found!:",wpshop)

    if scanjquery.getcode() == 200:
        print("[+] Found:",jqueryh)
    elif scanjquery.getcode() == 403:
        print("[+] Forbidden:",jqueryh)
    elif scanjquery.getcode() == 500:
        print("[+] Server Error:",jqueryh)
    else:
       print("[-] Not found!:",jqueryh)

    if scanslides.getcode() == 200:
        print("[+] Found:",slideshow)
    elif scanslides.getcode() == 403:
        print("[+] Forbidden:",slideshow)
    elif scanslides.getcode() == 500:
        print("[+] Server Error:",slideshow)
    else:
       print("[-] Not found!:",slideshow)

    if scaneasy.getcode() == 200:
        print("[+] Found:",easycom)
    elif scaneasy.getcode() == 403:
        print("[+] Forbidden:",easycom)
    elif scaneasy.getcode() == 500:
        print("[+] Server Error:",easycom)
    else:
       print("[-] Not found!:",easycom)

    if scancom.getcode() == 200:
        print("[+] Found:",comgallery)
    elif scancom.getcode() == 403:
        print("[+] Forbidden:",comgallery)
    elif scancom.getcode() == 500:
        print("[+] Server Error:",comgallery)
    else:
       print("[-] Not found!:",comgallery)

    if scantevo.getcode() == 200:
        print("[+] Found:",tevolution)
    elif scantevo.getcode() == 403:
        print("[+] Forbidden:",tevolution)
    elif scantevo.getcode() == 500:
        print("[+] Server Error:",tevolution)
    else:
       print("[-] Not found!:",tevolution)

    if scanflu.getcode() == 200:
        print("[+] Found:",fluid)
    elif scanflu.getcode() == 403:
        print("[+] Forbidden:",fluid)
    elif scanflu.getcode() == 500:
        print("[+] Server Error:",fluid)
    else:
       print("[-] Not found!:",fluid)

    if scanwp3.getcode() == 200:
        print("[+] Found:",wp3d)
    elif scanwp3.getcode() == 403:
        print("[+] Forbidden:",wp3d)
    elif scanwp3.getcode() == 500:
        print("[+] Server Error:",wp3d)
    else:
       print("[-] Not found!:",wp3d)

    if scansim.getcode() == 200:
        print("[+] Found:",simple)
    elif scansim.getcode() == 403:
        print("[+] Forbidden:",simple)
    elif scansim.getcode() == 500:
        print("[+] Server Error:",simple)
    else:
       print("[-] Not found!:",simple)

    if scanform.getcode() == 200:
        print("[+] Found:",formcraft)
    elif scanform.getcode() == 403:
        print("[+] Forbidden:",formcraft)
    elif scanform.getcode() == 500:
        print("[+] Server Error:",formcraft)
    else:
       print("[-] Not found!:",formcraft)

    if scanpitch.getcode() == 200:
        print("[+] Found:",pitchprint)
    elif scanpitch.getcode() == 403:
        print("[+] Forbidden:",pitchprint)
    elif scanpitch.getcode() == 500:
        print("[+] Server Error:",pitchprint)
    else:
       print("[-] Not found!:",pitchprint)
    sys.exit()    


# Component Scanner
if hexaa_pilih == "3":
    jom = input("Input target:")
    print("\n[+] Target:",jom)
    print("[+] Scanning...")
    if not jom.startswith("http://"):
        jom = "http://"+jom
    jom1 = jom+"/index.php?option=com_ca"
    jom2 = jom+"/index.php?option=com_calendario"
    jom3 = jom+"/index.php?option=com_camelcitydb2"
    jom4 = jom+"/index.php?option=com_camp"
    jom5 = jom+"/index.php?option=com_candle"
    jom6 = jom+"/index.php?option=com_canteen"
    jom7 = jom+"/index.php?option=com_caproductprices"
    jom8 = jom+"/index.php?option=com_carman"
    jom9 = jom+"/index.php?option=com_cartweberp"
    jom10 = jom+"/index.php?option=com_casino"
    jom11 = jom+"/index.php?option=com_casino_blackjack"
    jom12 = jom+"/index.php?option=com_casino_videopoker"
    jom13 = jom+"/index.php?option=com_casinobase"
    jom14 = jom+"/index.php?option=com_catalogproduction"
    jom15 = jom+"/index.php?option=com_categories"
    jom16 = jom+"/index.php?option=com_category"
    jom17 = jom+"/index.php?option=com_cbcontact"
    jom18 = jom+"/index.php?option=com_cbe"
    jom19 = jom+"/index.php?option=com_cbresumebuilder"
    jom20 = jom+"/index.php?option=com_adsmanager"
    jom21 = jom+"/index.php?option=com_ccinvoices"
    jom22 = jom+"/index.php?option=com_ccnewsletter"
    jom23 = jom+"/index.php?option=com_cgtestimonial"
    jom24 = jom+"/index.php?option=com_content"
    jom25 = jom+"/index.php?option=com_users"
    jom26 = jom+"/index.php?option=com_media"
    jom27 = jom+"/index.php?option=com_jdownloads"
    jom28 = jom+"/index.php?option=com_facileforms"
    jom29 = jom+"/index.php?option=com_imagebrowser"
    jom30 = jom+"/index.php?option=com_jfuploader"
    jom31 = jom+"/index.php?option=com_marketplace"
    jom32 = jom+"/index.php?option=com_aicontactsafe"
    jom33 = jom+"/index.php?option=com_blog_calendar"
    jom34 = jom+"/index.php?option=com_breezingforms"
    jom35 = jom+"/index.php?option=com_simplephotogallery"
    jom36 = jom+"/index.php?option=com_guru"
    jom37 = jom+"/index.php?option=com_forms"
    jom38 = jom+"/index.php?option=com_smartformer"
    jom39 = jom+"/index.php?option=com_aclassfb"
    jom40 = jom+"/index.php?option=com_inneradmission"
    jom41 = jom+"/index.php?option=com_attachments"
    jom42 = jom+"/index.php?option=com_garyscookbook"
    jom43 = jom+"/index.php?option=com_collector"
    jom44 = jom+"/index.php?option=com_aclsfgpl"
    jom45 = jom+"/index.php?option=com_joomgalaxy"
    jom46 = jom+"/index.php?option=com_jesubmit"
    jom47 = jom+"/index.php?option=com_hospital"
    jom48 = jom+"/index.php?option=com_controller"
    jom49 = jom+"/index.php?option=com_ksadvertiser"
    jom50 = jom+"/index.php?option=com_newssearch"
    jom51 = jom+"/index.php?option=com_free_consulation"
    jom52 = jom+"/index.php?option=com_shop"
    jom53 = jom+"/index.php?option=com_fileuploader"
    jom54 = jom+"/index.php?option=com_jemessenger"
    scanjom1s = urlopen(jom1)
    scanjom2s = urlopen(jom2)
    scanjom3s = urlopen(jom3)
    scanjom4s = urlopen(jom4)
    scanjom5s = urlopen(jom5)
    scanjom6s = urlopen(jom6)
    scanjom7s = urlopen(jom7)
    scanjom8s = urlopen(jom8)
    scanjom9s = urlopen(jom9)
    scanjom10s = urlopen(jom10)
    scanjom11s = urlopen(jom11)
    scanjom12s = urlopen(jom12)
    scanjom13s = urlopen(jom13)
    scanjom14s = urlopen(jom14)
    scanjom15s = urlopen(jom15)
    scanjom16s = urlopen(jom16)
    scanjom17s = urlopen(jom17)
    scanjom18s = urlopen(jom18)
    scanjom19s = urlopen(jom19)
    scanjom20s = urlopen(jom20)
    scanjom21s = urlopen(jom21)
    scanjom22s = urlopen(jom22)
    scanjom23s = urlopen(jom23)
    scanjom24s = urlopen(jom24)
    scanjom25s = urlopen(jom25)
    scanjom26s = urlopen(jom26)
    scanjom27s = urlopen(jom27)
    scanjom28s = urlopen(jom28)
    scanjom29s = urlopen(jom29)
    scanjom30s = urlopen(jom30)
    scanjom31s = urlopen(jom31)
    scanjom32s = urlopen(jom32)
    scanjom33s = urlopen(jom33)
    scanjom34s = urlopen(jom34)
    scanjom35s = urlopen(jom35)
    scanjom36s = urlopen(jom36)
    scanjom37s = urlopen(jom37)
    scanjom38s = urlopen(jom38)
    scanjom39s = urlopen(jom39)
    scanjom40s = urlopen(jom40)
    scanjom41s = urlopen(jom41)
    scanjom42s = urlopen(jom42)
    scanjom43s = urlopen(jom43)
    scanjom44s = urlopen(jom44)
    scanjom45s = urlopen(jom45)
    scanjom46s = urlopen(jom46)
    scanjom47s = urlopen(jom47)
    scanjom48s = urlopen(jom48)
    scanjom49s = urlopen(jom49)
    scanjom50s = urlopen(jom50)
    scanjom51s = urlopen(jom51)
    scanjom52s = urlopen(jom52)
    scanjom53s = urlopen(jom53)
    scanjom54s = urlopen(jom54)
    if scanjom1s.getcode() == 200:
        print("[+] Found:",jom1)
    else:
        print("[-] Not Found:",jom1)

    if scanjom2s.getcode() == 200:
        print("[+] Found:",jom2)
    else:
        print("[-] Not Found:",jom2)

    if scanjom3s.getcode() == 200:
        print("[+] Found:",jom3)
    else:
        print("[-] Not Found:",jom3)

    if scanjom4s.getcode() == 200:
        print("[+] Found:",jom4)
    else:
        print("[-] Not Found:",jom4)

    if scanjom1s.getcode() == 200:
        print("[+] Found:",jom1)
    else:
        print("[-] Not Found:",jom1)

    if scanjom5s.getcode() == 200:
        print("[+] Found:",jom5)
    else:
        print("[-] Not Found:",jom5)

    if scanjom6s.getcode() == 200:
        print("[+] Found:",jom6)
    else:
        print("[-] Not Found:",jom6)

    if scanjom7s.getcode() == 200:
        print("[+] Found:",jom7)
    else:
        print("[-] Not Found:",jom7)

    if scanjom8s.getcode() == 200:
        print("[+] Found:",jom8)
    else:
        print("[-] Not Found:",jom8)

    if scanjom9s.getcode() == 200:
        print("[+] Found:",jom9)
    else:
        print("[-] Not Found:",jom9)

    if scanjom10s.getcode() == 200:
        print("[+] Found:",jom10)
    else:
        print("[-] Not Found:",jom10)

    if scanjom11s.getcode() == 200:
        print("[+] Found:",jom11)
    else:
        print("[-] Not Found:",jom11)

    if scanjom12s.getcode() == 200:
        print("[+] Found:",jom12)
    else:
        print("[-] Not Found:",jom12)

    if scanjom13s.getcode() == 200:
        print("[+] Found:",jom13)
    else:
        print("[-] Not Found:",jom13)

    if scanjom14s.getcode() == 200:
        print("[+] Found:",jom14)
    else:
        print("[-] Not Found:",jom14)

    if scanjom15s.getcode() == 200:
        print("[+] Found:",jom15)
    else:
        print("[-] Not Found:",jom15)

    if scanjom16s.getcode() == 200:
        print("[+] Found:",jom16)
    else:
        print("[-] Not Found:",jom16)

    if scanjom17s.getcode() == 200:
        print("[+] Found:",jom17)
    else:
        print("[-] Not Found:",jom17)

    if scanjom18s.getcode() == 200:
        print("[+] Found:",jom18)
    else:
        print("[-] Not Found:",jom18)

    if scanjom19s.getcode() == 200:
        print("[+] Found:",jom19)
    else:
        print("[-] Not Found:",jom19)

    if scanjom20s.getcode() == 200:
        print("[+] Found:",jom20)
    else:
        print("[-] Not Found:",jom20)

    if scanjom21s.getcode() == 200:
        print("[+] Found:",jom21)
    else:
        print("[-] Not Found:",jom21)

    if scanjom22s.getcode() == 200:
        print("[+] Found:",jom22)
    else:
        print("[-] Not Found:",jom22)

    if scanjom23s.getcode() == 200:
        print("[+] Found:",jom23)
    else:
        print("[-] Not Found:",jom23)

    if scanjom24s.getcode() == 200:
        print("[+] Found:",jom24)
    else:
        print("[-] Not Found:",jom24)

    if scanjom25s.getcode() == 200:
        print("[+] Found:",jom25)
    else:
        print("[-] Not Found:",jom25)

    if scanjom26s.getcode() == 200:
        print("[+] Found:",jom26)
    else:
        print("[-] Not Found:",jom26)

    if scanjom27s.getcode() == 200:
        print("[+] Found:",jom27)
    else:
        print("[-] Not Found:",jom27)

    if scanjom28s.getcode() == 200:
        print("[+] Found:",jom28)
    else:
        print("[-] Not Found:",jom28)

    if scanjom29s.getcode() == 200:
        print("[+] Found:",jom29)
    else:
        print("[-] Not Found:",jom29)

    if scanjom30s.getcode() == 200:
        print("[+] Found:",jom30)
    else:
        print("[-] Not Found:",jom30)

    if scanjom31s.getcode() == 200:
        print("[+] Found:",jom31)
    else:
        print("[-] Not Found:",jom31)

    if scanjom32s.getcode() == 200:
        print("[+] Found:",jom32)
    else:
        print("[-] Not Found:",jom32)

    if scanjom33s.getcode() == 200:
        print("[+] Found:",jom33)
    else:
        print("[-] Not Found:",jom33)

    if scanjom34s.getcode() == 200:
        print("[+] Found:",jom34)
    else:
        print("[-] Not Found:",jom34)

    if scanjom35s.getcode() == 200:
        print("[+] Found:",jom35)
    else:
        print("[-] Not Found:",jom35)

    if scanjom36s.getcode() == 200:
        print("[+] Found:",jom36)
    else:
        print("[-] Not Found:",jom36)

    if scanjom37s.getcode() == 200:
        print("[+] Found:",jom37)
    else:
        print("[-] Not Found:",jom37)

    if scanjom38s.getcode() == 200:
        print("[+] Found:",jom38)
    else:
        print("[-] Not Found:",jom38)

    if scanjom39s.getcode() == 200:
        print("[+] Found:",jom39)
    else:
        print("[-] Not Found:",jom39)

    if scanjom40s.getcode() == 200:
        print("[+] Found:",jom40)
    else:
        print("[-] Not Found:",jom40)

    if scanjom41s.getcode() == 200:
        print("[+] Found:",jom41)
    else:
        print("[-] Not Found:",jom41)

    if scanjom42s.getcode() == 200:
        print("[+] Found:",jom42)
    else:
        print("[-] Not Found:",jom42)

    if scanjom43s.getcode() == 200:
        print("[+] Found:",jom43)
    else:
        print("[-] Not Found:",jom43)

    if scanjom44s.getcode() == 200:
        print("[+] Found:",jom44)
    else:
        print("[-] Not Found:",jom44)

    if scanjom45s.getcode() == 200:
        print("[+] Found:",jom45)
    else:
        print("[-] Not Found:",jom45)

    if scanjom46s.getcode() == 200:
        print("[+] Found:",jom46)
    else:
        print("[-] Not Found:",jom46)

    if scanjom47s.getcode() == 200:
        print("[+] Found:",jom47)
    else:
        print("[-] Not Found:",jom47)

    if scanjom48s.getcode() == 200:
        print("[+] Found:",jom48)
    else:
        print("[-] Not Found:",jom48)

    if scanjom49s.getcode() == 200:
        print("[+] Found:",jom49)
    else:
        print("[-] Not Found:",jom49)

    if scanjom50s.getcode() == 200:
        print("[+] Found:",jom50)
    else:
        print("[-] Not Found:",jom50)

    if scanjom51s.getcode() == 200:
        print("[+] Found:",jom51)
    else:
        print("[-] Not Found:",jom51)

    if scanjom52s.getcode() == 200:
        print("[+] Found:",jom52)
    else:
        print("[-] Not Found:",jom52)

    if scanjom53s.getcode() == 200:
        print("[+] Found:",jom53)
    else:
        print("[-] Not Found:",jom53)

    if scanjom54s.getcode() == 200:
        print("[+] Found:",jom54)
    else:
        print("[-] Not Found:",jom54)
    sys.exit() 

# Admin Page Scanner
if hexaa_pilih == "4":
    adm = input("Input target:")
    print("\n[+] Target:",adm)
    print("[+] Scanning...")
    if not adm.startswith("http://"):
        adm = "http://"+adm
    admin1 = adm+"/admin"
    admin2 = adm+"/administrator"
    admin3 = adm+"/adminweb"
    admin4 = adm+"/4dm1n"
    admin5 = adm+"/4dm1n1str4t0r"
    admin6 = adm+"/panel_admin"
    admin7 = adm+"/admin_panel"
    admin8 = adm+"/login/admin"
    admin9 = adm+"/admin/login"
    admin10 = adm+"/_admin"
    admin11 = adm+"/user/admin"
    admin12 = adm+"/admin.php"
    admin13 = adm+"/admin.aspx"
    admin14 = adm+"/redaktur"
    admin15 = adm+"/cp-admin"
    admin16 = adm+"/po-admin"
    admin17 = adm+"/p0-4dm1n"
    admin18 = adm+"/admin123"
    admin19 = adm+"/dataweb"
    admin20 = adm+"/pengurus"
    admin21 = adm+"/webpanel"
    admin22 = adm+"/paneldata"
    admin23 = adm+"/panel"
    admin24 = adm+"/admin/account.php"
    admin25 = adm+"/admin/login.php"
    admin26 = adm+"/admin/login.html"
    admin27 = adm+"/moderator"
    admin28 = adm+"/moderator/login.php"
    admin29 = adm+"/controlpanel"
    admin30 = adm+"/yonetim.asp"
    admin31 = adm+"/fileadmin"
    admin32 = adm+"/sysadmin"
    admin33 = adm+"/myadmin"
    admin34 = adm+"/wp-admin"
    admin35 = adm+"/ur-admin"
    admin36 = adm+"/webadmin"
    admin37 = adm+"/useradmin"
    admin38 = adm+"/blogindex"
    admin39 = adm+"/formslogin"
    admin40 = adm+"/admin_area"
    admin41 = adm+"/adminpro"
    admin42 = adm+"/super-admin"
    admin43 = adm+"/adm"
    admin44 = adm+"/cms"
    admin45 = adm+"/ADMIN"
    scanadm1 = urlopen(admin1)
    scanadm2 = urlopen(admin2)
    scanadm3 = urlopen(admin3)
    scanadm4 = urlopen(admin4)
    scanadm5 = urlopen(admin5)
    scanadm6 = urlopen(admin6)
    scanadm7 = urlopen(admin7)
    scanadm8 = urlopen(admin8)
    scanadm9 = urlopen(admin9)
    scanadm10 = urlopen(admin10)
    scanadm11 = urlopen(admin11)
    scanadm12 = urlopen(admin12)
    scanadm13 = urlopen(admin13)
    scanadm14 = urlopen(admin14)
    scanadm15 = urlopen(admin15)
    scanadm16 = urlopen(admin16)
    scanadm17 = urlopen(admin17)
    scanadm18 = urlopen(admin18)
    scanadm19 = urlopen(admin19)
    scanadm20 = urlopen(admin20)
    scanadm21 = urlopen(admin21)
    scanadm22 = urlopen(admin22)
    scanadm23 = urlopen(admin23)
    scanadm24 = urlopen(admin24)
    scanadm25 = urlopen(admin25)
    scanadm26 = urlopen(admin26)
    scanadm27 = urlopen(admin27)
    scanadm28 = urlopen(admin28)
    scanadm29 = urlopen(admin29)
    scanadm30 = urlopen(admin30)
    scanadm31 = urlopen(admin31)
    scanadm32 = urlopen(admin32)
    scanadm33 = urlopen(admin33)
    scanadm34 = urlopen(admin34)
    scanadm35 = urlopen(admin35)
    scanadm36 = urlopen(admin36)
    scanadm37 = urlopen(admin37)
    scanadm38 = urlopen(admin38)
    scanadm39 = urlopen(admin39)
    scanadm40 = urlopen(admin40)
    scanadm41 = urlopen(admin41)
    scanadm42 = urlopen(admin42)
    scanadm43 = urlopen(admin43)
    scanadm44 = urlopen(admin44)
    scanadm45 = urlopen(admin45)
    if scanadm1.getcode() == 200:
        print("[+] Found:",admin1)
    else:
        print("[-] Not Found:",admin1)

    if scanadm2.getcode() == 200:
        print("[+] Found:",admin2)
    else:
        print("[-] Not Found:",admin2)

    if scanadm3.getcode() == 200:
        print("[+] Found:",admin3)
    else:
        print("[-] Not Found:",admin3)

    if scanadm4.getcode() == 200:
        print("[+] Found:",admin4)
    else:
        print("[-] Not Found:",admin4)

    if scanadm5.getcode() == 200:
        print("[+] Found:",admin5)
    else:
        print("[-] Not Found:",admin5)

    if scanadm6.getcode() == 200:
        print("[+] Found:",admin6)
    else:
        print("[-] Not Found:",admin6)

    if scanadm7.getcode() == 200:
        print("[+] Found:",admin7)
    else:
        print("[-] Not Found:",admin7)

    if scanadm8.getcode() == 200:
        print("[+] Found:",admin8)
    else:
        print("[-] Not Found:",admin8)

    if scanadm9.getcode() == 200:
        print("[+] Found:",admin9)
    else:
        print("[-] Not Found:",admin9)

    if scanadm10.getcode() == 200:
        print("[+] Found:",admin10)
    else:
        print("[-] Not Found:",admin10)

    if scanadm11.getcode() == 200:
        print("[+] Found:",admin11)
    else:
        print("[-] Not Found:",admin11)

    if scanadm12.getcode() == 200:
        print("[+] Found:",admin12)
    else:
        print("[-] Not Found:",admin12)

    if scanadm13.getcode() == 200:
        print("[+] Found:",admin13)
    else:
        print("[-] Not Found:",admin13)

    if scanadm14.getcode() == 200:
        print("[+] Found:",admin14)
    else:
        print("[-] Not Found:",admin14)

    if scanadm15.getcode() == 200:
        print("[+] Found:",admin15)
    else:
        print("[-] Not Found:",admin15)

    if scanadm16.getcode() == 200:
        print("[+] Found:",admin16)
    else:
        print("[-] Not Found:",admin16)

    if scanadm17.getcode() == 200:
        print("[+] Found:",admin17)
    else:
        print("[-] Not Found:",admin17)

    if scanadm18.getcode() == 200:
        print("[+] Found:",admin18)
    else:
        print("[-] Not Found:",admin18)

    if scanadm19.getcode() == 200:
        print("[+] Found:",admin19)
    else:
        print("[-] Not Found:",admin19)

    if scanadm20.getcode() == 200:
        print("[+] Found:",admin20)
    else:
        print("[-] Not Found:",admin20)

    if scanadm21.getcode() == 200:
        print("[+] Found:",admin21)
    else:
        print("[-] Not Found:",admin21)

    if scanadm22.getcode() == 200:
        print("[+] Found:",admin22)
    else:
        print("[-] Not Found:",admin22)

    if scanadm23.getcode() == 200:
        print("[+] Found:",admin23)
    else:
        print("[-] Not Found:",admin23)

    if scanadm24.getcode() == 200:
        print("[+] Found:",admin24)
    else:
        print("[-] Not Found:",admin24)

    if scanadm25.getcode() == 200:
        print("[+] Found:",admin25)
    else:
        print("[-] Not Found:",admin25)

    if scanadm26.getcode() == 200:
        print("[+] Found:",admin26)
    else:
        print("[-] Not Found:",admin26)

    if scanadm27.getcode() == 200:
        print("[+] Found:",admin27)
    else:
        print("[-] Not Found:",admin27)

    if scanadm28.getcode() == 200:
        print("[+] Found:",admin28)
    else:
        print("[-] Not Found:",admin28)

    if scanadm29.getcode() == 200:
        print("[+] Found:",admin29)
    else:
        print("[-] Not Found:",admin29)

    if scanadm30.getcode() == 200:
        print("[+] Found:",admin30)
    else:
        print("[-] Not Found:",admin30)

    if scanadm31.getcode() == 200:
        print("[+] Found:",admin31)
    else:
        print("[-] Not Found:",admin31)

    if scanadm32.getcode() == 200:
        print("[+] Found:",admin32)
    else:
        print("[-] Not Found:",admin32)

    if scanadm33.getcode() == 200:
        print("[+] Found:",admin33)
    else:
        print("[-] Not Found:",admin33)

    if scanadm34.getcode() == 200:
        print("[+] Found:",admin34)
    else:
        print("[-] Not Found:",admin34)

    if scanadm35.getcode() == 200:
        print("[+] Found:",admin35)
    else:
        print("[-] Not Found:",admin35)

    if scanadm36.getcode() == 200:
        print("[+] Found:",admin36)
    else:
        print("[-] Not Found:",admin36)

    if scanadm37.getcode() == 200:
        print("[+] Found:",admin37)
    else:
        print("[-] Not Found:",admin37)

    if scanadm38.getcode() == 200:
        print("[+] Found:",admin38)
    else:
        print("[-] Not Found:",admin38)

    if scanadm39.getcode() == 200:
        print("[+] Found:",admin39)
    else:
        print("[-] Not Found:",admin39)

    if scanadm40.getcode() == 200:
        print("[+] Found:",admin40)
    else:
        print("[-] Not Found:",admin40)

    if scanadm41.getcode() == 200:
        print("[+] Found:",admin41)
    else:
        print("[-] Not Found:",admin41)

    if scanadm42.getcode() == 200:
        print("[+] Found:",admin42)
    else:
        print("[-] Not Found:",admin42)

    if scanadm43.getcode() == 200:
        print("[+] Found:",admin43)
    else:
        print("[-] Not Found:",admin43)

    if scanadm44.getcode() == 200:
        print("[+] Found:",admin44)
    else:
        print("[-] Not Found:",admin44)

    if scanadm45.getcode() == 200:
        print("[+] Found:",admin45)
    else:
        print("[-] Not Found:",admin45)
    sys.exit()