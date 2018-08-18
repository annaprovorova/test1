#Алгоритмы для работы с цифрами числа и последовательностями

#Количество цифр числа
def kol_digits(n, s):
    '''возвращает количество цифр числа'''
    s = 0
    while n!=0:
        s += 1
        n //= 10
    print(s)
    return s

def sum_digits(n, s):
    '''возвращает сумму цифр числа'''
    s = 0
    while n!=0:
        s += n%10
        n //= 10
    print(s)
    return s

#сумма последовательности чисел
#количество чисел задаётся с клавиатуры
def sum_of_sequence():
    sum = 0
    n = int(input('Введите количество чисел в последовательности: ')) #считываем количесво чисел
    print('Вводите числа последовательности через Enter')
    for i in range(n):
        sum += int(input())
    print(sum)

#сумма последовательности чисел
#суммирование до барьерного элемента
def sum_of_sequence_bar():
    sum = 0
    bar = int(input('Введите барьерный элемент: ')) #считываем количесво чисел
    print('Вводите числа последовательности через Enter')
    a = int(input()) #первый элемент
    while a != bar: #сам барьерный элемент к сумме не прибавляется
        sum += a
        a = int(input())
    print(sum)


#Выделение цифр числа в отдельный список
def digits_of_number(n, A): #n - число, А - список цифр числа
    lenght = len(str(n)) #количество цифр в числе + 1 для корректного ренджа
    i = 0
    while n!=0:
        A[i] = n%10
        n //= 10
        i += 1
    A.reverse()
    print(*A)


def test():
    #x = int(input('Введите число:'))
    #A = [0]*len(str(x))
    s = 0
    #digits_of_number(x, A)
    #kol_digits(x, s)
    #sum_digits(x, s)
    #sum_of_sequence()
    #sum_of_sequence_bar()

if __name__ == '__main__':
    test()
