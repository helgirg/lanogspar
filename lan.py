#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from pylab import *
import numpy as np
import Tkinter
from Tkinter import *
import math

z = [] # global fylki til thess ad reikna medalverdbolgu midad vid valid timabil i verdbolguvidmid

def lan():

    #byr til nyjan glugga
    newwin = Toplevel()
    newwin.geometry("950x550")
    newwin.title('Lan')
    newwin.focus_set()

    #Labels fyrir lan upphaed vextir lengd VT
    L1 = Label(newwin, text="Lan")
    L1.place(x=50, y=20)

    L1 = Label(newwin, text="Höfudstoll")
    L1.place(x=200, y=20)

    L1 = Label(newwin, text="Vextir")
    L1.place(x=400, y=20)

    L1 = Label(newwin, text="Lengd (manudir)")
    L1.place(x=600, y=20)

    L1 = Label(newwin, text="Verdtryggt?")
    L1.place(x=800, y=20)

    #Label/box husnaedislan
    L1 = Label(newwin, text="Husnaedislan")
    L1.place(x=50, y=50)
    E5 = Entry(newwin, bd=5)#höfudstoll
    E5.insert(0, 0)
    E5.place(x=200, y=50)
    E6 = Entry(newwin, bd=5)#vextir
    E6.insert(0, 0)
    E6.place(x=400, y=50)
    E7 = Entry(newwin, bd=5)#lengd
    E7.insert(0, 0)
    E7.place(x=600, y=50)

    #Label/box yfirdrattur
    L1 = Label(newwin, text="Yfirdrattur")
    L1.place(x=50, y=100)
    E8 = Entry(newwin, bd=5)#höfudstoll
    E8.insert(0, 0)
    E8.place(x=200, y=100)
    E9 = Entry(newwin, bd=5)#vextir
    E9.insert(0, 0)
    E9.place(x=400, y=100)
    E10 = Entry(newwin, bd=5)#lengd
    E10.insert(0, 0)
    E10.place(x=600, y=100)

    #Label/box Bilalan
    L1 = Label(newwin, text="Bilalan")
    L1.place(x=50, y=150)
    E11 = Entry(newwin, bd=5)#höfudstoll
    E11.insert(0, 0)
    E11.place(x=200, y=150)
    E12 = Entry(newwin, bd=5)#vextir
    E12.insert(0, 0)
    E12.place(x=400, y=150)
    E13 = Entry(newwin, bd=5)#lengd
    E13.insert(0, 0)
    E13.place(x=600, y=150)

    #Label fyrir tima
    L2 = Label(newwin, text="Her fyrir nedan setur thu inn tha upphaed sem thu getur lagt fyrir og hvad thu getur lagt thessa upphaed fyrir i marga manudi.")
    L2.place(x=50, y=200)

    #Label/box upphaed
    L1 = Label(newwin, text="Upphaed:")
    L1.place(x=50, y=250)
    E14 = Entry(newwin, bd=5)
    E14.insert(0, 0)
    E14.place(x=200, y=250)
    
    #Label/box manudir
    L1 = Label(newwin, text="Manudir:")
    L1.place(x=50, y=300)
    E15 = Entry(newwin, bd=5)
    E15.insert(0, 0)
    E15.place(x=200, y=300)

    #Label fyrir verðbólguviðmið
    L2 = Label(newwin, text="Her fyrir nedan skrifar thu inn timabil (ar a bilinu 1990 til 2013) fyrir verdbolguvidmid")
    L2.place(x=50, y=350)
    
    #Label/box verdbolgu manudi fra
    L1 = Label(newwin, text="Fra:")
    L1.place(x=50, y=400)
    OM3 = Entry(newwin, bd=5)
    OM3.insert(0, 1990)
    OM3.place(x=200, y=400)

    #Label/box verdbolgu manudi til
    L1 = Label(newwin, text="Til:")
    L1.place(x=50, y=450)
    OM4 = Entry(newwin, bd=5)
    OM4.insert(0, 2013)
    OM4.place(x=200, y=450)

    var13 = int(OM3.get())      
    var14 = int(OM4.get())

    # fall til ad reikna medalverdbolgu midad vid valid timabil i verdbolguvidmid
    def verdbfra(tala):
        verdb = {1990:15.9, 1991:6.8, 1992:4, 1993:4.1, 1994:1.6, 1995:1.7, 1996:2.3, 
                1997:1.8, 1998:1.7, 1999:3.2, 2000:5.2, 2001:6.4, 2002:5.3, 2003:2.1, 2004:3.2, 
                2005:4, 2006:6.7, 2007:5.1, 2008:12.6, 2009:12.2, 2010:5.4, 2011:4, 2012:5.2, 2013:3.9}
        for i in range(0, len(tala)):
            global z
            z.append(verdb[tala[i]])

    # kollum i verdbolgufallid midad vid valid timabil i verdbolguvidmid
    verdbfra(range(var13, var14))
    medalverdb = sum(z)/len(range(var13, var14))

    #Checkbox husnaedislan
    checkvar1 = IntVar()
    c1 = Checkbutton(newwin, text="ja", variable=checkvar1, onvalue=float(medalverdb), offvalue=0)
    c1.place(x=800, y=50)

    #Checkbox yfirdrattur
    checkvar2 = IntVar()
    c2 = Checkbutton(newwin, text="ja", variable=checkvar2, onvalue=float(medalverdb), offvalue=0)
    c2.place(x=800, y=100)

    #Checkbox bilalan
    checkvar3 = IntVar()
    c3 = Checkbutton(newwin, text="ja", variable=checkvar3, onvalue=float(medalverdb), offvalue=0)
    c3.place(x=800, y=150)

    def newwin2():
        newwin2 = Toplevel()
        newwin2.geometry("656x256")
        newwin2.title("Nidurstada")
        newwin2.focus_set()
        var12 = (checkvar1.get())   #verdbolguvidmid husnaedislan
        var15 = (checkvar2.get())   #verdbolguvidmid yfirdrattur
        var16 = (checkvar3.get())   #verdbolguvidmid bilalan
        var1 = (E5.get())           #husbaedislan höfudstoll
        var2 = (E6.get())           #husbaedislan vextir
        var3 = (E7.get())           #husbaedislan lengd
        var4 = (E8.get())           #yfirdrattur höfudstoll
        var5 = (E9.get())           #yfirdrattur vextir
        var6 = (E10.get())          #yfirdrattur lengd
        var7 = (E11.get())          #Bilalan höfudstoll
        var8 = (E12.get())          #Bilalan vextir
        var9 = (E13.get())          #Bilalan lengd
        var10 = (E14.get())         #Upphaed
        var11 = (E15.get())         #Manudir

        if var1.isdigit() and var2.isdigit() and var3.isdigit() and var4.isdigit() and var5.isdigit() and var6.isdigit() and var7.isdigit() and var8.isdigit() and var9.isdigit() and var10.isdigit() and var11.isdigit():

            var12 = float(checkvar1.get())/100      #verdbolguvidmid husnaedislan
            var15 = float(checkvar2.get())/100      #verdbolguvidmid yfirdrattur
            var16 = float(checkvar3.get())/100      #verdbolguvidmid bilalan
            var1 = float(E5.get())*(1+var12)        #husbaedislan höfudstoll
            var2 = float(E6.get())/100              #husbaedislan vextir
            var3 = int(E7.get())                    #husbaedislan lengd
            var4 = float(E8.get())*(1+var15)        #yfirdrattur höfudstoll
            var5 = float(E9.get())/100              #yfirdrattur vextir
            var6 = int(E10.get())                   #yfirdrattur lengd
            var7 = float(E11.get())*(1+var16)       #Bilalan höfudstoll
            var8 = float(E12.get())/100             #Bilalan vextir
            var9 = int(E13.get())                   #Bilalan lengd
            var10 = float(E14.get())                #Upphaed
            var11 = float(E15.get())                #Manudir
            x = [0]
            a = [0]
            manhus = int(var11)
            manhus2 = int(var11)

            #husnaedislan
            if var1 > 0:
                if var2 + var12 > var5 + var15 and var2 + var12 > var8 + var16:
                    y = [var1]
                    b = [var1]
                    husla = var1/var3
                    husan = var1
                    hof2 = var1
                    lenhus = var3
                    hof3 = var1
                    
                    #an innborgunar
                    for i in range(1, var3+2):
                        husan = husan - husla
                        x.append(i)
                        y.extend([husan])

                    # med innborgun
                    for i in range(1, manhus+1):
                        hof2 = hof2 - var10 - husla
                        a.append(i)
                        b.append(hof2)
                    for i in range(manhus+1, lenhus+1):
                        hof2 = hof2 - husla
                        a.extend([i])
                        b.extend([hof2])
                    
                    while hof3 > 0:
                        hof3 = hof3 - var10 - husla
                        manhus2 = manhus2 - 1

                    # prentum ut nidurstodur i newwin2
                    L10 = Label(newwin2, text=("Graf sem lysir throun hofudstols opnast i odrum glugga"),font=("Times New Roman",14))
                    L10.place(x=50,y=50)
                    L11 = Label(newwin2, text=("Thad er hagstaedast fyrir thig ad borga " + str(var10) + " kr. inn a husnaedislanid thitt"),font=("Times New Roman",14))
                    L11.place(x=50,y=100)
                    if manhus2 > 0:
                        if var5 + var15 > var8 + var16:         
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a yfirdrattinn"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)
                        else:
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a bilalanid"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)

                    fig = plt.figure()
                    fig.canvas.set_window_title('Hunsnaedislan - Graf med yfirliti yfirliti yfir lanathroun thina')

                    # plottum grafid
                    plt.plot(x,y)
                    plt.plot(a,b)
                    plt.axis([0, var3, 0, var1])
                    plt.xlabel('Timi i manudum')
                    plt.ylabel('Kr')
                    plt.title('Graf med yfirliti yfir lanathroun thina')
                    plt.show()

            #yfirdrattur
            if var4 > 0:
                if var5 + var15 > var12 + var15 and var5 + var15 > var8 + var16:
                    y = [var4]
                    b = [var4]
                    husla = var4/var6
                    husan = var4
                    hof2 = var4
                    lenhus = var6
                    
                    #an innborgunar
                    for i in range(1, var6+2):
                        husan = husan - husla
                        x.append(i)
                        y.extend([husan])

                    # med innborgun
                    for i in range(1, manhus+1):
                        hof2 = hof2 - var10 - husla
                        a.append(i)
                        b.append(hof2)
                    for i in range(manhus+1, lenhus+1):
                        hof2 = hof2 - husla
                        a.extend([i])
                        b.extend([hof2])

                    while hof3 > 0:
                        hof3 = hof3 - var10 - husla
                        manhus2 = manhus2 - 1

                    # prentum ut nidurstodur i newwin2
                    L10 = Label(newwin2, text=("Graf sem lysir throun hofudstols opnast i odrum glugga"),font=("Times New Roman",14))
                    L10.place(x=50,y=50)
                    L11 = Label(newwin2, text=("Thad er hagstaedast fyrir thig ad borga " + str(var10) + " kr. inn a yfirdrattinn thinn"),font=("Times New Roman",14))
                    L11.place(x=50,y=100)
                    if manhus2 > 0:
                        if var2 + var12 > var8 + var16:         
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a husnaedislanid thitt"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)
                        else:
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a bilalanid"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)

                    fig = plt.figure()
                    fig.canvas.set_window_title('Yfirdrattur - Graf med yfirliti yfirliti yfir lanathroun thina')

                    # plottum grafid
                    plt.plot(x,y)
                    plt.plot(a,b)
                    plt.axis([0, var6, 0, var4])
                    plt.xlabel('Timi i manudum')
                    plt.ylabel('Kr')
                    plt.title('Graf med yfirliti yfir lanathroun thina')
                    plt.show()

            #bilalan        
            if var7 > 0:
                if var8 + var16 > var2 + var12 and var8 + var16 > var5 + var15:
                    y = [var7]
                    b = [var7]
                    husla = var7/var9
                    husan = var7
                    hof2 = var7
                    lenhus = var9
                    
                    #an innborgunar
                    for i in range(1, var9+2):
                        husan = husan - husla
                        x.append(i)
                        y.extend([husan])

                    # med innborgun
                    for i in range(1, manhus+1):
                        hof2 = hof2 - var10 - husla
                        a.append(i)
                        b.append(hof2)
                    for i in range(manhus+1, lenhus+1):
                        hof2 = hof2 - husla
                        a.extend([i])
                        b.extend([hof2])

                    while hof3 > 0:
                        hof3 = hof3 - var10 - husla
                        manhus2 = manhus2 - 1

                    # prentum ut nidurstodur i newwin2
                    L10 = Label(newwin2, text=("Graf sem lysir throun hofudstols opnast i odrum glugga"),font=("Times New Roman",14))
                    L10.place(x=50,y=50)
                    L11 = Label(newwin2, text=("Thad er hagstaedast fyrir thig ad borga " + str(var10) + " kr. inn a bilalanid thitt"),font=("Times New Roman",14))
                    L11.place(x=50,y=100)
                    if manhus2 > 0:
                        if var2 + var12 > var5 + var15:         
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a husnaedislanid thitt"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)
                        else:
                            L12 = Label(newwin2, text=("Eftir thad skalt thu greida inn a yfirdrattinn"),font=("Times New Roman",14))
                            L12.place(x=50,y=150)

                    fig = plt.figure()
                    fig.canvas.set_window_title('Bilalan - Graf med yfirliti yfirliti yfir lanathroun thina')

                    # plottum grafid
                    plt.plot(x,y)
                    plt.plot(a,b)
                    plt.axis([0, var9, 0, var7])
                    plt.xlabel('Timi i manudum')
                    plt.ylabel('Kr')
                    plt.title('Graf med yfirliti yfir lanathroun thina')
                    plt.show()       
                    
        #Villumelding
        else:
            L21 = Label(newwin2, text =("Villa: Innsláttur má einungis vera tala."),font=("Times New Roman",14))
            L21.place(x=10,y=10)

        
    #Upplysingar i Hjalp-takka fyrir Lan
    def newwin4():
        newwin4 = Toplevel()
        newwin4.geometry("750x250")
        newwin4.title("Hjálp")
        newwin4.focus_set()
        L40 = Label(newwin4, text="Lan",font=("Times New Roman",14))
        L40.place(x=10,y=10)
        L50 = Label(newwin4, text="Sláðu inn hofudstol a laninu thinu,vexti sem vid a og fjolda manada fyrir thad lan sem thu ert ad athuga fyrir .",font=("Times New Roman",14))
        L50.place(x=10,y=40)
        L60 = Label(newwin4, text="Thvi næst hakar þu i verðtryggda boxið ef það a við lanið sem þu med utfyllt. ",font=("Times New Roman",14))
        L60.place(x=10,y=60)
        L70 = Label(newwin4, text="Ath thu getur slad inn fyrir allt ad thrju lan i einu.",font=("Times New Roman",14))
        L70.place(x=10,y=80)
        L80 = Label(newwin4, text="Her fyrir nedan setur thu inn tha upphæð sem þu getur lagt fyrir og hvad þu getur lagt þessa.",font=("Times New Roman",14))
        L80.place(x=10,y=100)
        L160=Label(newwin4,text="upphaed fyrir i marga manuði miða við gefnar forsendur.",font=("Times New Roman",14))
        L160.place(x=10,y=120)        
        L100=Label(newwin4,text="I neðsta boxinu velur þu verðbolgutimabil(fra 1990 til 2013) fyrir verdtryggdu lanin thin ef vid a.",font=("Times New Roman",14))      
        L100.place(x=10,y=140)
        L110=Label(newwin4,text="Ýttu á Reikna takkann.",font=("Times New Roman",14))
        L110.place(x=10,y=160)
        L120=Label(newwin4,text="Upp kemur þá nýr gluggi sem sýnir þér hversu mikid thu tharft ad borga inn a lanid thitt a manudi og hver greiðslan er",font=("Times New Roman",14))
        L120.place(x=10,y=180)
        L130=Label(newwin4,text="þegar þu ert buin að leggja einhverja akvedna upphæð fyrir, miðað við gefnar forsendur.",font=("Times New Roman",14))
        L130.place(x=10,y=200)


    #Help-takki
    A3= Tkinter.Button(newwin, text="Hjálp", command=newwin4)
    A3.place(x=400, y=500)


    #Utreikningartakki
    A1 = Tkinter.Button(newwin, text="Reikna", command=newwin2)
    A1.place(x=300,y=500)

    
