#операции над числами

#возведение в степень
# O(n**2)
def degree(a, n):
    '''возвращает число a, возведённое в степень n'''
    c = 1
    for i in range(n):
        c *= a
    return c

#быстрое возведение в степень
#используется "перевод в двоичную с/с счисления" показателя степени
#O(log n)
def fast_degree(a, n):
    ''''''
    c = 1
    while n > 0:
        if n%2 > 0:
            c *= a #нечётная степень - обычное умножение на а
        a *= a #чётная степень - умножаем а*а
        n //= 2
    print(c)

#обмен двухчисле местами
def change(a,b):
    a, b = b, a

#Алгоритм Евклида через вычитание
#O(a/b)
def Euclid_substraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            a, b = b, (b - a)
    print (a) #не важно какой возвращать или печать - в конце они равны.


#факториал числа
def factotial(n):
    

#Алгоритм Евклида через деление с остатком
#O(log(a/b))
def Euclid_division_1(a, b):
    while b > 0:
        a, b = b, a%b
    print (a)

#Алгоритм Евклида через деление с остатком
# a, b - не упорядоченная пара
def Euclid_division_2(a, b):
    while (a!=0) and (b!=0):
        if a > b:
            a %= b
        else:
            b %= a
    print(a+b) #один из них 0, а в другом содержится НОД, но заранее не знаем, в каком - что



#переворот числа (ВСЯ МОЩЬ ПИТОНА! :))
def flip(n):
    s = list(str(n))
    s.reverse()
    n = int(''.join(s))
    print(n)

#переворот числа классический (не волжно оканчиваться на 0)
def flip_classic(n):
    s = 0
    while n!=0:
        s = s*10 + n%10
        n //= 10
    print (s)

#проверка числа на НЕ простоту (потому что такой алгоритм легче)
#О(n**0,5)
def is_not_simple(x):
    d = 2
    while d <= x**0.5: #меньший из делителей не превышает корня из числа
        if x%d == 0:
            return True
        else:
            d += 1

#проверка числа на простоту классика
def is_simple(x):
    flag = True
    d = 2
    while flag and d <= x**0.5:
        if x%d == 0:
            flag = False
        else:
            d += 1
    if x==1:
        print ('Никакое')
    elif flag:
        print ('Простое')
    else:
        print ('Составное')

#факторизация числа
def factorization(x):
    D = [] #пустой список делителей чила
    d = 2
    while x != 1:
        while  x%d == 0:
            D.append(d)
            x //= d
        d += 1

    """
    #другой вариант с условием вместо вложенного цикла
    while x != 1:
        if x%d == 0:
            D.append(d)
            x //= d
        else:
            d += 1
    """
    print(*D)

def  test():
    #fast_degree(2, 10)
    #Euclid_substraction(1024, 512)
    #Euclid_division_1(7, 3)
    #Euclid_division_2(1024, 256)
    #flip(123450)
    #flip_classic(123245)
    """if is_not_simple(121):
        print('not simple')
    else:
        print('simple')
    """
    #is_simple(107)
    factorization(12356)

if __name__ == '__main__':
    test()
