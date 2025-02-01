import headers_and_footers as description
import itertools
import math
import prime


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def product_digits(n):
    if n==0:
        return 0
    p = 1
    while n:
        p *= n % 10
        n //= 10
    return p
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

    odpowiedzi = []
    DOWN = 10
    UP = 100
    for n in range(DOWN,UP):
        if(n==sum_digits(n)+product_digits(n)):
            odpowiedzi.append(n)
    print("ilosc odpowiedzi : 1", "    odp : ", len(odpowiedzi), "   spr : ", odpowiedzi)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_11(name):
    odpowiedzi = []
    DOWN = 1
    UP = 46
    for i in range(DOWN,UP):
        for j in range(DOWN, UP):
            if(2025==i*i + i*i + j*j):
                odpowiedzi.append([i,i,j])
    print("ilosc odpowiedzi : ", len(odpowiedzi), "   odp : ", odpowiedzi)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_12(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_13(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_14(name):

    odpowiedzi = []
    Y = 2025
    for n in range(1,Y):
        k = n
        while (k<Y):
            k=k+2*sum_digits(k)
        if(k==Y):
            odpowiedzi.append(n)

    print("ilosc odpowiedzi : 1", "    odp : ", len(odpowiedzi), odpowiedzi)

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_15(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_16(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_17(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
@description.task_header_and_footer
def zadanie_18(name):
    description.not_resolved()

# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    description.main_header('2025', 'Eliminacje krajowe')

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
    zadanie_11('')
    description.end_of_c1()

    zadanie_12('')
    zadanie_13('')
    zadanie_14('')
    description.end_of_c2()

    zadanie_15('')
    zadanie_16('')
    description.end_of_l1()
    description.end_of_gp()

    zadanie_17('')
    zadanie_18('')
    description.end_of_l2()
    description.end_of_hc()
