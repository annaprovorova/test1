#Реализованы базовые алгоритмы сортировок

#FIXME: Сортировка обезьяны (Bogosort)
#FIXME:Пирамидальная сортировка
#FIXME: Порядковая сортировка работает не на всех тестах в силу своей логики

#сортировка "Пузырьком"
#O(N**2), где N - количество элементов в списке
def bubble_sort(A):
    N = len(A)
    for prohod in range(1, N): #тут мы считаем количество проходов, поэтому идём от 1 до N
        for i in range(N - prohod):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


#Сортировка простого выбора
def choice_sort(A):
    N = len(A)
    for pos in range(0, N-1): #тут мы смотрим позиции элементов, поэтому от 0 до N-1
        for i in range(pos+1, N):
            if A[i] < A[pos]:
                A[pos], A[i] = A[i], A[pos]

#Сортировка простыми вставками
def insert_sort(A):
    N = len(A)
    for pos in range(1, N):
        # УВЕРЕНЫ, что список отсортирован в позициях с 0-й по (pos-1)-ю включительно
        i = 0
        while A[i] < A[pos]:
            i += 1
        # УВЕРЕНЫ, что i указывает на элемент не меньше вставляемого
        tmp = A[pos]
        for k in range(pos-1, i-1, -1): #это обратный перебор по списку с перевёрнутыми индексами
            A[k+1] = A[k]
        A[i] = tmp
        # УВЕРЕНЫ, что список отсортирован в позициях с 0-й по pos-ю включительно

#Быстрая сортировка слиянием
#O(n*log n)
def merge(A, B):
    i = k = n = 0
    C = [0]*(len(A)+len(B))
    while i < len(A) and k < len(B):
        if A[i] < B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    C[n::] = A[i:] + B[k:]
    return C

#Бинарная сортировка
def merge_sort(A):
    B = []
    if len(A) <= 1:
        return A
    middle = len(A)//2
    L = merge_sort(A[:middle])
    R = merge_sort(B[middle:])
    return merge(A, B)
#return A if len(A) <= 1 else merge(merge_sort(A[len(A)//2]), merge_sort(B[len(A)//2:]))

def standard_sort(A):
    A.sort()
    B = A.sorted()

#Порядковая сортировка (сортировка посчётом)
#FIXME: в текущем виде работает только на тест-кейсах 1, 4, 5, 6
#не работает с отрицательными числами и со словами

def count_sort(A):
    Q = [0]*1001 #здесь 1000 - это количество РАЗЛИЧНЫХ элементов, которые могут встретиться в A
    for x in A:
             Q[x] += 1 #создаём список, в котором хранится частота встречаемости чисел в последовательности
    for k in range(1001): #диапазон зависит от разброса чисел в последовательности
                        #эта сортировка хороша, когда разброс небольшой, например встречаются числа от 0 до 9
             for i in range (Q[k]):
                        print (k, end=' ')

#тестирование сортировок
def sort_test(my_sort):
    import random

    A = [1, 2, 3, 4, 5, 6]
    A_ans = [1, 2, 3, 4, 5, 6]
    my_sort(A)
    print('test case #1: ' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, -2, -3, -4, -5, -6]
    A_ans = [-6, -5, -4, -3, -2, -1]
    my_sort(A)
    print('test case #2: ' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, 2, -3, 4, -5, 6]
    A_ans = [-5, -3, -1, 2, 4, 6]
    my_sort(A)
    print('test case #3: ' + ('OK' if A == A_ans else 'Fail'))

    A = [1000]
    A_ans = [1000]
    my_sort(A)
    print('test case #4: ' + ('OK' if A == A_ans else 'Fail'))

    A = []
    A_ans = []
    my_sort(A)
    print('test case #5: ' + ('OK' if A == A_ans else 'Fail'))

    A = [5]*100
    A_ans = [5]*100
    my_sort(A)
    print('test case #6: ' + ('OK' if A == A_ans else 'Fail'))

    A = [random.randint(1, 100) for i in range(1000)]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #7: ' + ('OK' if A == A_ans else 'Fail'))

    A = [[2], [1], [3], [5], [4], [5]]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #8: ' + ('OK' if A == A_ans else 'Fail'))


if __name__ == '__main__':
    '''print('Test Bubble Sort:')
    sort_test(bubble_sort)
    print('Test Choice Sort:')
    sort_test(choice_sort)
    print('Test Insert Sort:')
    sort_test(insert_sort)
    print('Test Standard Sort:')
    sort_test(standard_sort)'''
    print('Test Merge Sort:')
    sort_test(merge_sort)
    #print('Test Count Sort:')
    #sort_test(count_sort)
