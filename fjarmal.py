import sys
import Tkinter
from Tkinter import *
from pylab import *
import numpy as np
import math
from sparnadur import *
from lan import *

root = Tkinter.Tk()
root.tk.call('encoding', 'system', 'utf-8')

root.geometry("700x512")
root.title("Reiknivél Íslandsbanka")
B1= Tkinter.Button (root, text="Sparnaður", command=sparnadur, fg="red", font=("Helvetica",16))
B1.pack(fill=BOTH, expand=1)
B2 = Tkinter.Button(root, text="Lán", command=lan, fg="red", font=("Helvetica",16))
B2.pack(fill=BOTH, expand=1)
root.mainloop()
