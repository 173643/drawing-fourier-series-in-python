import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import cmath as math2
import math
import keyboard
import pygame
from svgpathtools import svg2paths

# Ścieżka pliku svg powinna zaczynać się od 'm', a kończyć na 'z'
# i powinna składać się jedynie z bezwzględnie podanych prostych i krzywych Beziera(duże L i C)

class Funkcja:
    def __init__(self, funk, start=0, stop=1):
        self.funk = funk
        self.start = start
        self.stop = stop

    def oblicz(self, a, b, c):
        return ((a - b) / (c - b)) * (self.stop - self.start) + self.start


def czytaj():
    global baza
    tablica = []
    paths, attributes = svg2paths('rzeszow.svg')  #nazwa pliku svg
    for k, v in enumerate(attributes):
        tablica.append(v['d'])
    x = tablica[0]
    tab2 = x.split(" ")
    y = tab2[0]
    p1 = y[1:]
    p2 = tab2[1]
    baza = [float(p1), float(p2)]
    ii = 2
    while ii < len(tab2)-1:
        y = tab2[ii]
        if y.isdigit() or y[0] == '-':
            print("Plik svg nie spełnia wymagań")
        elif y[1:].isdigit() or y[1] == '-':
            print("Poprawnie dodano ścieżekę")
            p3 = y[1:]
            znak = y[0]
            ii = ii+1
            ii = uzupelnij(p1, p2, p3, tab2, ii, znak)
            p1 = tab2[ii-2]
            p2 = tab2[ii-1]
            if not(p1.isdigit() or p1[0] == '-'):
                p1 = p1[1:]

def uzupelnij(ax, ay, bx, tab2, ii, znak):
    lista = [ax, ay, bx]
    while tab2[ii].isdigit() or (tab2[ii][0] == '-' and tab2[ii][1:].isdigit()):
        lista.append(tab2[ii])
        ii = ii+1
    y = tab2[ii]
    if y[:-1].isdigit() or y[0] == '-':
        lista.append(y[:-1])
    w = 0
    dodaj(lista, znak, w)
    return ii

def dodaj(lista, znak,w):
    if (znak == 'c' or znak == 'C') and w+7 < len(lista):
        ax = lista[w]
        ay = lista[w+1]
        bx = lista[w+2]
        by = lista[w+3]
        cx = lista[w+4]
        cy = lista[w+5]
        dx = lista[w+6]
        dy = lista[w+7]
        x = Funkcja(lambda t: complex(float(ax) * (1 - t) ** 3 + 3 * float(bx)*t * (1 - t) ** 2 + 3 * float(cx) * t ** 2 * (1 - t) + float(dx) * t ** 3,
                            float(ay) * (1 - t) ** 3 + 3*float(by) * t * (1 - t) ** 2 + 3 * float(cy) * t ** 2 * (1 - t) + float(dy) * t ** 3))
        rownanie.append(x)
        w = w+6
        dodaj(lista, znak, w)

    elif (znak == 'l' or znak == 'L') and w+3 < len(lista):
        ax = float(lista[w])
        ay = float(lista[w+1])
        bx = float(lista[w+2])
        by = float(lista[w+3])
        x = Funkcja(lambda t: complex(
                ax * (1 - t) ** 3 + 3 * ax * t * (1 - t) ** 2 + 3 * bx * t ** 2 * (1 - t) + bx * t ** 3,
                ay * (1 - t) ** 3 + 3 * ay * t * (1 - t) ** 2 + 3 * by * t ** 2 * (1 - t) + by * t ** 3))
        w = w + 2
        rownanie.append(x)
        dodaj(lista, znak, w)

def f(t):
    x = min(len(rownanie) - 1, math.floor(t * len(rownanie)))
    rownania = rownanie[x]
    return rownania.funk(rownania.oblicz(t, x / len(rownanie), (x + 1) / len(rownanie)))


def obraz(x, y):
    return ((x + baza[0]) * pow + szer/2, (-y + baza[1]) * pow + wys/2)

def odl(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def rys_strzalki(p1, p2):
    odleglosc = odl(p1, p2)
    alfa = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    pygame.draw.aaline(ekran, (255, 255, 255), p1, (math.cos(alfa) * odleglosc * stala + p1[0], math.sin(alfa) * odleglosc * stala + p1[1]))
    p3 = (math.cos(alfa) * odleglosc + math.cos(alfa + _45_stopni + math.pi) * odleglosc / 5 + p1[0],
          math.sin(alfa) * odleglosc + math.sin(alfa + _45_stopni + math.pi) * odleglosc / 5 + p1[1])
    p4 = (math.cos(alfa) * odleglosc + math.cos(alfa - _45_stopni + math.pi) * odleglosc / 5 + p1[0],
          math.sin(alfa) * odleglosc + math.sin(alfa - _45_stopni + math.pi) * odleglosc / 5 + p1[1])
    pygame.draw.aalines(ekran, (255, 255, 0), True, [p2, p3, p4])

def rys_wykres():
    global punkty, baza
#    stara_pozycja = complex(0, 0)
    pozycja = wspolczynniki[zakres]
    strzalki = [(obraz(baza[0], baza[1]), obraz(pozycja.real, pozycja.imag))]
    for i in range(1, zakres+1):
        stara_pozycja = pozycja
        pozycja += wspolczynniki[zakres + i] * math2.exp(i * zmienna * y)
        strzalki.append(((stara_pozycja.real, stara_pozycja.imag), (pozycja.real, pozycja.imag)))
        stara_pozycja = pozycja
        pozycja += wspolczynniki[zakres - i] * math2.exp((-i) * zmienna * y)
        strzalki.append(((stara_pozycja.real, stara_pozycja.imag), (pozycja.real, pozycja.imag)))

    punkty.append(pozycja)

    for i in strzalki:
        rys_strzalki(obraz(*i[0]), obraz(*i[1]))

def wypisz():
    try:
        pygame.draw.aalines(ekran, 500, False, [obraz(punkt.real, punkt.imag) for punkt in punkty])
    except:
        pass

baza=[0,0]
rownanie = []
czytaj()

zakres = 125    # ilość wektorów /2
krok = 0.0001
zmienna = complex(0, 2 * math2.pi) # 2*pi*i
zmienna2 = complex(0, 2 * math2.pi * krok) # 2*pi*i*krok
total = int(1 / krok)
_45_stopni = math.radians(45)
stala = 1 - math.sqrt(2) / 10


wspolczynniki = [sum(f(t * krok) * math2.exp(-n * zmienna2 * t) for t in range(0, total + 1)) / total for n in range(-zakres, zakres + 1, 1)]
wspolczynniki[zakres] = complex(baza[0], baza[1])

pygame.init()
okno = pygame.display.Info()
szer = okno.current_w
wys = okno.current_h

clock = pygame.time.Clock()
ekran = pygame.display.set_mode((szer, wys), pygame.NOFRAME)

pow = 50    # dostosowanie ekranu do pliku

punkty = []
y = 0

while True:
    zwolnij = clock.tick(60)

    ekran.fill(0)
    rys_wykres()
    wypisz()
    pygame.display.update()
    y = y + 0.0005

    if keyboard.is_pressed("esc"):
        break

pygame.quit()