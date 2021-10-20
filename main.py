def show_menu():
    print('1. Citirea a două mulțimi de numere întregi de la tastatura sub forma a două liste.')
    print('2. Afișați dacă cele două liste au același număr de elemente pare.')
    print('3. Afișați o listă reprezentând intersecția listelor citite de la tastatură.')
    print('4. Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste.')
    print('5. Cerinta.')
    print('x. Iesire')

def read_list():
        lst1=[]
        lst2=[]
        lista1 = input('Introduceti elementele din prima lista separate prin spatiu:')
        lista2 = input('Introduceti elementele din a doua lista separate prin spatiu:')
        lista1_str_split = lista1.split(' ')
        lista2_str_split = lista2.split(' ')
        for num1 in lista1_str_split:
            lst1.append(int(num1))
        for num2 in lista2_str_split:
            lst2.append(int(num2))
        return lst1,lst2
def even_number(lista):
    """
    Determina numarul de elemente pare dintr-o lista
    :param lista: o lista data
    :return: numarul de elemente pare
    """
    np=0
    for num in lista:
        if num % 2 == 0:
            np=np+1
    return np
def test_even_number():

    assert even_number([1, 3, 5]) == 0
    assert even_number([1,1,1,1,1]) == 0
    assert even_number([2,4,12,22,24]) == 5

def both_lists_same_evens(lst1,lst2):
    """
    Verifica daca ambele liste date au aceelasi numar de elemente pare
    :param lst1: o lista data
    :param lst2: o lista data
    :return:returneaza True daca ambele liste au aceelasi numar de elemente pare
            returneaza False in caz contrar
    """
    if even_number(lst1) == even_number(lst2):
        return True
    else:
        return False
def test_both_lists_same_evens():
    assert both_lists_same_evens([2,2,2],[2,4,6,5]) == True
    assert both_lists_same_evens([2, 2, 1], [2, 4, 6, 5]) == False
    assert both_lists_same_evens([1,2,3], [4,5,6]) == False

def intersection(lst1,lst2):
    """
    Determina lista formata din intersectia elementelor din lst1 si lst2
    :param lst1: o lista data
    :param lst2: o lista data
    :return: lista result formata din intersectia elementelor din cele doua liste
    """
    result=[]
    for num1 in lst1:
        for num2 in lst2:
            if num1 == num2:
                result.append(num1)
    return result
def test_intersection():
    assert intersection([12,22,36,424],[22,23,36,55,424]) == [22,36,424]
    assert intersection([1,2,3],[4,5,6]) == []
    assert intersection([1,2,3],[3,4,5]) == [3]
def mirror(n):
    """
    returneaza inversul unui numar dat
    :param n: numar dat
    :return: inversul lui
    """
    r = 0
    while n > 0:
        r=r*10+n%10
        n=n//10
    return r
def test_mirror():
    assert mirror(654) == 456
    assert mirror(111) == 111
    assert mirror(12345) == 54321
def list_palindrom(lst1,lst2):
    """
    Determina toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste
    :param lst1: lista data
    :param lst2:lista data
    :return: result ce contine palindroamele
    """
    result=[]
    l1=len(lst1)
    l2=len(lst2)
    p=0
    while(p<l1 and p<l2):
        n_str=str(lst1[p])+str(lst2[p])
        n=int(n_str)

        if mirror(n) == n:
            result.append(n)
        p=p+1
    return result
def test_list_palindrom():
    assert list_palindrom([12, 22, 36, 11],[21, 23, 63, 55, 424]) == [1221, 3663]
    assert list_palindrom([12, 22, 36, 11,2,222], [21, 23, 63, 55, 424,222]) == [1221, 3663,222222]
def read_list_3():
    lst3 = []
    lista3 = input('Introduceti elementele din a treia lista separate prin spatiu:')
    lista3_str_split = lista3.split(' ')
    for num3 in lista3_str_split:
        lst3.append(int(num3))
    return lst3

def div_with_lst3(n,lst3):
    """
    Determina daca n este divizibil cu toate elmentele din lst3
    :param n: numar dat
    :param lst3: lista data
    :return: True daca este adevarat
             False daca nu
    """
    for num in lst3:
        if n % num !=0:
            return False
    return True

def test_div_with_lst_3():
    assert div_with_lst3(36,[1,2,3,4]) == True
    assert div_with_lst3(36, [1, 2, 3, 4 , 5]) == False
    assert div_with_lst3(12 , [1,2,3,4]) == True
def mirror_list(listai,lst3):
    """
    Returneaza lista obtinuta prin schimbara elementelor din listai ce sunt divizibile cu toate elementele din lst3 cu inversul lor

    """
    result=[]
    p=0
    while p < len(listai):
        if div_with_lst3(listai[p],lst3):
            listai[p] =mirror(listai[p])
        p=p+1
    return listai
def test_mirror_list():
    assert mirror_list([12,22,36,363],[1,2,3,4]) == [21,22,63,363]
def main():
        lst1=[]
        lst2=[]
        lst3=[]
        while True:
            show_menu()
            opt=input('Introduceti o optiune:')
            if opt == '1':
                lst1,lst2=read_list()
            elif opt == '2':
                print(both_lists_same_evens(lst1,lst2))
            elif opt == '3':
                print(intersection(lst1,lst2))
            elif opt == '4':
                print(list_palindrom(lst1,lst2))
            elif opt == '5':
                lst3=read_list_3()
                print(mirror_list(lst1,lst3))
                print(mirror_list(lst2, lst3))
            elif opt == 'x':
                    break
            else:
                print("optiune invalida")
if __name__ == '__main__':
    test_even_number()
    test_both_lists_same_evens()
    test_intersection()
    test_div_with_lst_3()
    test_mirror()
    test_mirror_list()
    test_list_palindrom()
    main()