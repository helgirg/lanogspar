#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from pylab import *
import numpy as np
import Tkinter
from Tkinter import *
import math

def sparnadur():

    #Byr til nyjan glugga
    newwin = Toplevel()
    newwin.geometry("512x512")
    newwin.title("Sparnadur")
    newwin.focus_set()

    #Label fyrir upphaed eftir manudi
    L0 = Label(newwin, text="Sparnaður", font=("Helvetica",16))
    L0.place(x=210, y=10)

    #Label fyrir Upphaed og entry gluggi
    L1 = Label(newwin, text="Sparnaðarupphæð á mán:")
    L1.place(x=50, y=70)
    E1 = Entry(newwin, bd=5)
    E1.place(x=200, y=70)
    L7 = Label(newwin, text="Kr.")
    L7.place(x=350, y=70)

    #Label fyrir tima
    L2 = Label(newwin, text="Fjöldi sparnaðarmánaða:")
    L2.place(x=50, y=120)


    #Label fyrir manaðarfjolda eftir sparnad
    L0 = Label(newwin, text="Reikna sparnaðartíma", font=("Helvetica",16))
    L0.place(x=160, y=250)

    #Label fyrir Upphaed og entry gluggi 2
    L6 = Label(newwin, text="Sparnaður á mánuði:")
    L6.place(x=50, y=310)
    E6 = Entry(newwin, bd=5)
    E6.place(x=200, y=310)
    L8 = Label(newwin, text="Kr.")
    L8.place(x=350, y=310)


   #Label fyrir Upphaed sem skal safna upp i og entry gluggi
    L3 = Label(newwin, text="Ég vil safna upp í:")
    L3.place(x=50, y=360)
    E4 = Entry(newwin, bd=5)
    E4.place(x=200, y=360)
    L9 = Label(newwin, text="Kr.")
    L9.place(x=350, y=360)

    #Vextir
    L10 = Label(newwin, text="Vextir")
    L10.place(x=50, y=410)
    E7 = Entry(newwin, bd=5)
    E7.place(x=200, y=410)
    L11 = Label(newwin, text=("%"))
    L11.place(x=350, y=410)

    
    #Entry-box fyrir manudi
    E5=Entry(newwin, bd=5)
    E5.place(x=200,y=120)

    def newwin2():
        newwin2 = Toplevel()
        newwin2.geometry("650x100")
        newwin2.title("Sparnaður")
        newwin2.focus_set()
        var1 = (E1.get())
        var2 = (E5.get())

        if var1.isdigit() and var2.isdigit():

            var1 = int(E1.get())
            var2 = int(E5.get())
            manudir = 0
            
            #Vaxtathrep overdtryggt grunnthrep
            if (var1<100000):
                manvext=1.0033
                a=0
                for i in range(0,var2):
                    b=a+var1
                    a=b*manvext
                for i in range(0,var2):
                    L30=Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Vaxtaþrep á Grunnþrepi sem er óverðtryggt. Þú værir þá bundinn í 30 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L30.place(x=10,y=10)
                    
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

             #Vaxtathrep overdtryggt grunnthrep
            if (var1< 5000000 and var1>=100000 and var2<3 ):
                manvext=1.0033
                a=0
                for i in range(0,var2):
                    b=a+var1
                    a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Vaxtaþrep á Grunnþrepi sem er óverðtryggt. Þú værir þá bundinn í 30 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

            #Vaxtathrep overdtryggt 1.threp
            if (var1<=20000000 and var1>=5000000 and var2 <=2 ):
                manvext=1.0035
                a=0
                for i in range(0,var2):
                    b=a+var1
                    a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Vaxtaþrep á 1.þrepi sem er óverðtryggt. Þú værir þá bundinn í 30 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                a=int(a/1000000)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Milljonir Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

            #Vaxtathrep overdtryggt 2.threp
            if (var1<= 75000000 and var1>20000000 and var2 <=2 ):
                manvext=1.0038
                a=0
                for i in range(0,var2):
                    b=a+var1
                    a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Vaxtaþrep á 2.þrepi sem er óverðtryggt. Þú værir þá bundinn í 30 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                a=int(a/1000000)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Milljonir Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

            #Vaxtathrep overdtryggt 3.threp
            if (var1 > 75000000 and var2 <=2 ):
                manvext=1.0040
                a=0
                for i in range(0,var2):
                    b=a+var1
                    a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Vaxtaþrep á 3.þrepi sem er óverðtryggt. Þú værir þá bundinn í 30 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                a=int(a/1000000)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Milljonir Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()
                
            #Fastvaxtareikningur overdtryggt 3-5 manudir
            if(var1>=100000 and var2 >= 3 and var2<6):
                manvext=1.0041
                a=0
                for i in range(0,var2):
                        b=a+var1
                        a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Óverðtryggðan fastvaxtareikning. Þú værir þá bundinn í 90 daga og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

            #Fastvaxtareikningur overdtryggt 6-11 manudir
            if (var1>=100000 and var2 >= 6 and var2<12):
                manvext=1.0042
                a=0
                for i in range(0,var2):
                        b=a+var1
                        a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Óverðtryggðan fastvaxtareikning. Þú værir þá bundinn í hálft ár og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()
                
            #Fastvaxtareikningur overdtryggt 12 manudir eda fleiri
            if (var1>=100000 and var2>=12):
                manvext=1.0045
                a=0
                for i in range(0,var2):
                        b=a+var1
                        a=b*manvext
                for i in range(0,var2):
                    L5 = Label(newwin2, text=("Hentugast væri fyrir þig að leggja inn á sparnaðarreikninginn" +"\n" +"Óverðtryggðan fastvaxtareikning. Þú værir þá bundinn í 1.ár og eftir" + "\n" + str(var2)+ " mánuði yrði sparnaðurinn þinn kominn upp í " +str(a)+ " krónur."),font=("Times New Roman",14))
                    L5.place(x=10,y=10)
                i = i+1
                fig = plt.figure()
                fig.canvas.set_window_title('Graf med thinni sparnadarleid')
                x=[0,i]
                y=[0,a]
                plot(x,y)
                plt.xlim(0,i+1)
                plt.ylim(0,a+(a/5))
                plt.xlabel('Timi i manudum')
                plt.ylabel('Kr')
                plt.title('Graf med thinni sparnadarleid')
                plt.show()

         #Villumelding           
        else:
            L21 = Label(newwin2, text =("Villa: Innsláttur má einungis vera tala."),font=("Times New Roman",14))
            L21.place(x=10,y=10)

    def newwin3():
        newwin3 = Toplevel()
        newwin3.geometry("650x100")
        newwin3.title("Sparnaðartími")
        newwin3.focus_set()
        var1=(E6.get())
        var2=(E4.get())
        var3=(E7.get())

        if var1.isdigit() and var2.isdigit() and var3.isdigit():
             var1=float(E6.get())
             var2=float(E4.get())
             var3=float(E7.get())
             v1=(var3/100)/12
             v2=v1+1
             a=0
             for i in range(0,1000):
                 b = a+var1
                 a=b*v2
                 
                 if(a>var2):
                     L20 = Label(newwin3, text=("Þú þarft að spara í "+str(i)+ " mánuði."),font=("Times New Roman",14))
                     L20.place(x=10,y=10)
                     break

                       

 
                
        #Villumelding           
        else:
            L21 = Label(newwin2, text =("Villa: Innsláttur má einungis vera tala."),font=("Times New Roman",14))
            L21.place(x=10,y=10)





    #Utreikningartakki 1
    A1 = Tkinter.Button(newwin, text="Reikna", command=newwin2)
    A1.place(x=230,y=170)

    #Utreikningartakki 2
    A2 = Tkinter.Button(newwin, text="Reikna", command=newwin3)
    A2.place(x=230,y=460)

def lan():
    newwin = Toplevel()
    newwin.geometry("1024x512")
    newwin.title('Lán')
    newwin.focus_set()
