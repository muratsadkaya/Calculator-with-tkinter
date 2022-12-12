import tkinter as tk

s1 = 0
islem = ""


def yaz(m):
    n = len(bosluk.get())
    bosluk.insert(n, str(m))
    print(m)


def topla():
    global islem
    global s1
    s1 = float(bosluk.get())
    islem = "+"
    bosluk.delete(0, "end")


def cikar():
    global islem
    global s1
    s1 = float(bosluk.get())
    islem = "-"
    bosluk.delete(0, "end")


def carp():
    global islem
    global s1
    s1 = float(bosluk.get())
    islem = "*"
    bosluk.delete(0, "end")


def bol():
    global islem
    global s1
    s1 = float(bosluk.get())
    islem = "/"
    bosluk.delete(0, "end")


s2 = 0


def hesap():
    global s2
    s2 = float(bosluk.get())
    print(s2)
    global islem
    sonuc = 0
    if islem == "+":
        sonuc = s1 + s2
    elif islem == "-":
        sonuc = s1 - s2
    elif islem == "*":
        sonuc = s1 * s2
    elif islem == "/":
        sonuc = s1 / s2
    bosluk.delete(0, "end")
    bosluk.insert(0, str(sonuc))


def sil():
    bosluk.delete(0, "end")


pencere = tk.Tk()
pencere.geometry("300x300+70+70")
pencere.title("Calculator")
pencere["bg"] = "red"

bosluk = tk.Entry(font="Ariel 16 bold", width=20, bg="yellow", justify="right")
bosluk.place(x=25, y=30)

sıfır = tk.Button(text="0", font="Ariel 17 bold", bg="yellow", command=lambda m=0: yaz(m))
sıfır.place(x=180, y=240)

bir = tk.Button(text="1", font="Ariel 17 bold", bg="yellow", command=lambda m=1: yaz(m))
bir.place(x=30, y=240)

iki = tk.Button(text="2", font="Ariel 17 bold", bg="yellow", command=lambda m=2: yaz(m))
iki.place(x=80, y=240)

uc = tk.Button(text="3", font="Ariel 17 bold", bg="yellow", command=lambda m=3: yaz(m))
uc.place(x=130, y=240)

dort = tk.Button(text="4", font="Ariel 17 bold", bg="yellow", command=lambda m=4: yaz(m))
dort.place(x=30, y=180)

bes = tk.Button(text="5", font="Ariel 17 bold", bg="yellow", command=lambda m=5: yaz(m))
bes.place(x=80, y=180)

alti = tk.Button(text="6", font="Ariel 17 bold", bg="yellow", command=lambda m=6: yaz(m))
alti.place(x=130, y=180)

yedi = tk.Button(text="7", font="Ariel 17 bold", bg="yellow", command=lambda m=7: yaz(m))
yedi.place(x=30, y=120)

sekiz = tk.Button(text="8", font="Ariel 17 bold", bg="yellow", command=lambda m=8: yaz(m))
sekiz.place(x=80, y=120)

dokuz = tk.Button(text="9", font="Ariel 17 bold", bg="yellow", command=lambda m=9: yaz(m))
dokuz.place(x=130, y=120)

nokta = tk.Button(text=".", font="Ariel 16 bold", bg="grey", width=2, command=lambda m=".": yaz(m))
nokta.place(x=80, y=70)

ac = tk.Button(text="C", font="Ariel 16 bold", bg="grey", width=2, command=sil)
ac.place(x=30, y=70)

sonuc = tk.Button(text="=", font="Ariel 17 bold", bg="grey", width=2, command=hesap)
sonuc.place(x=230, y=240)

btopla = tk.Button(text="+", font="Ariel 17 bold", bg="grey", width=2, command=topla)
btopla.place(x=180, y=80)

bcarp = tk.Button(text="x", font="Ariel 17 bold", bg="grey", width=2, command=carp)
bcarp.place(x=180, y=160)

bcikar = tk.Button(text="-", font="Ariel 17 bold", bg="grey", width=2, command=cikar)
bcikar.place(x=230, y=80)

bbol = tk.Button(text="/", font="Ariel 17 bold", width=2, bg="grey", command=bol)
bbol.place(x=230, y=160)

pencere.mainloop()