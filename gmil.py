import headers_and_footers as description
import itertools
import math
import prime

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_01(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_02(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_03(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_04(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_05(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_06(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_07(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_08(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_09(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_10(name):
    counter = 0
    for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5):
        L = i[0]
        I = i[1]
        M = i[2]
        A = i[3]
        E = i[4]
        if (L==0 or A==0 or M==0 or E==0):
            continue
        LIMA = 1000 * L + 100 * I + 10 * M + A
        LEA = 100 * L + 10 * E + A
        AMI = 100 * A + 10 * M + I
        MIL = 100 * M + 10 * I + L
        EIL = 100 * E + 10 * I + L
        if (LEA + AMI + MIL + EIL == LIMA):
            counter += 1
            print(f'  {counter}) Lima = {LIMA}, bo  {LEA} + {AMI} + {MIL} + {EIL} = {LIMA}')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_11(name):
    print(f'  [  1  1  -  2  2  -  3  3]')
    print(f'  [  -  4  4  -  5  6  6  -]')
    print(f'  [  7  7  -  8  5  -  9  9]')
    print(f'  [  - 10 10  8  - 11 11  -]')
    print(f'  [ 12 12  - 13 13  - 14 14]')
    print(f'  [  - 15 15  - 16 17 17  -]')
    print(f'  [ 18 18  - 19 16  - 20 20]')
    print(f'  [  - 21 21 19  - 22 22  -]')
    print()
    print(f'  Odp: Najmniejsza łączna liczba kostek na szachownicy to {22}')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_12(name):
    for i in range(10,100):
        v = i*i*i
        if v % 10 == 7 and int(v / 100) % 10 == 7 and int(v / 10000) % 10 == 7:
            print(f'  Odp: Długość krawędzi tego sześcianu to {i}')
            print(f'   bo  {i} * {i} * {i} = {v}')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_13(name):
    r=140/2
    R=140*math.sqrt(2)/2
    wynik = round(math.pi*r*r/2-(math.pi*R*R/4-r*r))
    print(f'  Odp: pole widocznej częsci gwiazdy wynosi {wynik} mm^2')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_14(name):
    count = 0
    for i in itertools.permutations(prime.prime_to(41), 2):
        a = i[0]
        b = i[1]
        if a + a + b == 41:
            count += 1
            print(f'  {count}) {a} + {a} + {b} = {a+a+b}')
    print(f'  Odp:  Takich prostopadłościanów jest {count}')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_15(name):
    i = 0
    biale = 0
    czarne = 0
    while(True):
        i += 1
        new_rew = i * 7
        tmp = czarne
        czarne = biale
        biale = tmp
        biale += new_rew
        if(biale == 2023):
            print(f'  Odp: Czarnych pereł w naszyjniku jest {czarne}')
            return
        if(biale > 2023):
            print(f'  Odp: ERROR - coś poknociłeś, białych jest za dużo')
            return

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_16(name):
    def find(n, ratio):
        top = 100
        bottom = 1
        bill = 0
        pay_for_false = 600
        pay_for_true = 400
        while(top != bottom):
            mid = round((top - bottom + 1) * ratio) + bottom - 1
            if mid < bottom:
                mid = bottom
            if mid == top:
                mid = top - 1
            if n >= bottom and n <= mid:
                bill += pay_for_false
                top = mid
            else:
                bill += pay_for_true
                bottom = mid + 1
        return bill


    nnn = 0
    rrr = 0
    max_ratio = 1000
    min_max_bill = 600*100
    for r in range(1, max_ratio):
        r = max_ratio-r
        ratio = r / max_ratio
        max_bill = 0
        nn = 0
        for n in range(1, 101):
            bill = find(n, ratio)
            if bill > max_bill:
                max_bill = bill
                nn = n
        if max_bill < min_max_bill:
            min_max_bill = max_bill
            nnn = nn
            rrr = ratio
        min_max_bill
    print(f'  Odp: Zapłaci {min_max_bill} dolarów, dla nnn={nnn} i rrr = {rrr}')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_17(name):
    wynik = round((math.pi/2-1)*100)
    print(f'  Odp: Proporcja powierzchni czarnej części kalejdoskopu do jego powierzchni całkowitej wynosi {wynik}%')

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_18(name):
    def heron(a, b, c):
        p = (a + b + c) / 2
        PSqare = p * (p - a) * (p - b) * (p - c)
        if PSqare > 0:
            return math.sqrt(PSqare)
        return None

    def side(area, a, b):
        h = 2 * area / a
        if h > b:
            return None
        x = math.sqrt(b * b - h * h)
        ax = a - x
        c = math.sqrt(ax * ax + h * h)
        return c

    counter = 0
    bc = 13
    bf = 10
    cd = 15
    N_MAX = 100
    delta = 0.0000000000001
    aa =0;
    for be in range(1, bf):
        for ce in range(1, cd):
            if be + ce > bc and be + bc > ce and bc + ce > be:
                aa += 1
                ef = bf - be
                de = cd - ce
                cf = side(ef * heron(bc, be, ce) / be, ef, ce)
                bd = side(de * heron(bc, be, ce) / ce, de, be)
                if cf != None and bd != None:
                    if abs(cf - int(cf)) < delta and abs(bd - int(bd)) < delta:
                        cf = int(cf)
                        bd = int(bd)
                        for ad in range(1, N_MAX):
                            for af in range(1, N_MAX):
                                ab = bd + ad
                                ac = cf + af
                                p_abc = heron(ab, ac, bc)
                                p_acd = heron(ac, ad, cd)
                                p_bcd = heron(bc, bd, cd)
                                p_abf = heron(ab, af, bf)
                                p_bcf = heron(bc, bf, cf)
                                if p_abc != None and p_acd != None and p_bcd != None and p_abf != None and p_bcf != None:
                                    if abs(p_abc - p_acd - p_bcd) < delta and abs(p_abc - p_abf - p_bcf) < delta:
                                        counter += 1
                                        print(f'{aa}  {counter}) Odp: pole wynosi {round(p_abc)} ... dokładnie {p_abc} bo cf={cf}; bd={bd}; be={be}; ce={ce}; ab={ab}; ac={ac};')

# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    description.main_header('2023', 'Eliminacje krajowe')

    zadanie_01('')
    zadanie_02('')
    zadanie_03('')
    zadanie_04('')
    zadanie_05('')
    description.end_of_ce()

    zadanie_06('')
    zadanie_07('')
    zadanie_08('')
    description.end_of_cm()

    zadanie_09('')
    zadanie_10('')
    zadanie_11('Domino')
    description.end_of_c1()

    zadanie_12('Sześcian Kunegundy')
    zadanie_13('Zaćmienie')
    zadanie_14('Prostopadłościany')
    description.end_of_c2()

    zadanie_15('Naszyjnik')
    zadanie_16('Złote samorodki')
    description.end_of_l1()
    description.end_of_gp()

    zadanie_17('Kalejdoskop')
    zadanie_18('M. Elon i jego ogródek')
    description.end_of_l2()
    description.end_of_hc()
