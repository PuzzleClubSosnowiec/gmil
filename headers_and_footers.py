import time

# -------------------------------------------------------------------------------------------------
def main_header(year, competitions):
    print()
    print(f'GMiL {year} - {competitions}')
    print()

# -------------------------------------------------------------------------------------------------
def task_header_and_footer(func):
    def wrapper(*args, **kwargs):

        print('--------------------------------------------------------------------------------------------------\\')
        print(func.__name__, *args)
        print()
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print()
        print(f'  czas wykonania = {int((finish - start)*1000)}ms')
        print('--------------------------------------------------------------------------------------------------/')
        return result

    return wrapper

# -------------------------------------------------------------------------------------------------
def not_resolved():
    print(f'  Jeszcze nie rozwoiązane')

# -------------------------------------------------------------------------------------------------
def end_of_ce():
    print(f'Koniec kategorii CE - uczniowie klasy III SP lub młodsi')

# -------------------------------------------------------------------------------------------------
def end_of_cm():
    print(f'Koniec kategorii CM - uczniowie klas IV oraz V SP')

# -------------------------------------------------------------------------------------------------
def end_of_c1():
    print(f'Koniec kategorii C1 - uczniowie klas VI oraz VII SP')

# -------------------------------------------------------------------------------------------------
def end_of_c2():
    print(f'Koniec kategorii C2 - uczniowie klasy VIII SP i klasy pierwszej szkół średnich')

# -------------------------------------------------------------------------------------------------
def end_of_l1():
    print(f'Koniec kategorii L1 - pozostali uczniowie szkół srednich')

# -------------------------------------------------------------------------------------------------
def end_of_gp():
    print(f'Koniec kategorii GP - dorosli nie występujący w kategorii L2 oraz HC')

# -------------------------------------------------------------------------------------------------
def end_of_l2():
    print(f'Koniec kategorii L2 - studenci kierunków scisłych i technicznych, nie starsi niż 26 lat')

# -------------------------------------------------------------------------------------------------
def end_of_hc():
    print(f'Koniec kategorii HC - osoby zawodowo zajmujące się matematyką i informatyką')

