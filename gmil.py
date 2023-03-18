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
    total = 2*3*5*7*11*13*17
    min_roznica = total
    for i in range(1,4):
        for j in itertools.permutations([2, 3, 5, 7, 11, 13, 17], i):
            iloczyn = 1;
            for k in range(i):
                iloczyn *= j[k]
            pozostalosc = total/iloczyn
            roznica = abs(iloczyn - pozostalosc)
            suma_iloczynow = pozostalosc + iloczyn
            if(min_roznica > roznica):
                min_roznica = roznica
                print(j, roznica, suma_iloczynow)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_10(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_11(name):
    counter = 0
    for d in range(1, 10):
        for j in range(10):
            dj = 10*d+j
            d23j=1000*d+230+j
            if(d23j%dj==0):
                counter +=1
                print(counter,") ", dj, " bo ",d23j,"/", dj,"=", d23j/dj)
    print("Ilość rozwiązan =", counter)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_12(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_13(name):
    a = 2023
    b = 32368
    c = 8092
    print(a,"->",b,"->",c, "->", "suma =",a+b+c)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_14(name):
    counter = 0
    for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
        A = i[0]
        B = i[1]
        C = i[2]
        D = i[3]
        ABCD = 1000*A+100*B+10*C+D
        DCBA = 1000*D+100*C+10*B+A
        if(ABCD*23==DCBA*32):
            counter += 1
            print(counter, ") ", ABCD)
    print("Ilość rozwiązan =", counter)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_15(name):
    print(1-((12*math.sqrt(3))/(2*math.sqrt(3)+1)*(2*math.sqrt(3)+1)))

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_16(name):
    N = 20
    delta = 0.0000000000001
    ab_ok = 0;
    ac_ok = 0;
    bc_ok = 0;
    for i in itertools.permutations(range(1, N), 3):
        a = i[0]
        b = i[1]
        c = i[2]
        ab = math.sqrt(a * a + b * b)
        ac = math.sqrt(a * a + c * c)
        bc = math.sqrt(b * b + c * c)
        if(abs(ab - int(ab)) < delta):
            ab_ok = 1
        if(abs(ac - int(ac)) < delta):
            ac_ok = 1
        if(abs(bc - int(bc)) < delta):
            bc_ok = 1
        if(ab_ok + ac_ok + bc_ok>1):
            if(abs(a+b+c-ab-ac) < delta):
                print("odp a+b+c=", a+b+c, "a =", a, "b =", b, "c =", c, "ab =", ab, "ac =", ac, "bc =", bc)



    # -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_17(name):
    def f(n):
        if(n==0):
            return math.sqrt(23*44484)
        return math.sqrt(23*44484+f(n-1))

    print(f(20))



# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_18(name):
    description.not_resolved()

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

    zadanie_09('Siedem żetonów')
    zadanie_10('')
    zadanie_11('Przeplatajmy!')
    description.end_of_c1()

    zadanie_12('')
    zadanie_13('Cykl roku')
    zadanie_14('Symetryczne mnożenie')
    description.end_of_c2()

    zadanie_15('')
    zadanie_16('Pryzmat Tomka')
    description.end_of_l1()
    description.end_of_gp()

    zadanie_17('Rachunek Ala Embika')
    zadanie_18('')
    description.end_of_l2()
    description.end_of_hc()
