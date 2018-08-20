#примеры и задачи на рекурсию

def matryoshka(n):
    if n == 1:
        print(' '*n + 'матрёшечка')
    else:
        print(' '*n + 'матрёшка №', n)
        matryoshka(n-1)
        print(' '*n + 'матрёшка №', n)


#факториал
def factorial(n):
    if n == 0:
        print ('барьер! 0')
        return 1
    else:
        print (' '*n + 'n = ', n)
        result = factorial(n-1)*n
        print (' '*n + 'n = ', n)
        return result

"""
факториал в одну строку
def f(n):
    return 1 if n == 0 else f(n-1)*n
"""

#степень
#
def degree(a, n):
    if n == 0:
        return 1
    else:
        return degree(a, n-1)*a

#быстрое возведение в степень
def fast_degree(a, n):
    if n == 0:
        return 1
    elif n%2: #чётное
        return degree(a*a, n//2)
    else: #не чётное
        return degree(a, n-1)*a

#алгоритм Эвклида
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# return a if b == 0 else return gcd(b, a%b)

#быстрая сортировка Хоара

#быстрая сортировка слиянием
#O(n*log n)
def merge(A, B):
    i, k, n = 0
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

def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A)//2
    L = merge_sort(A[:middle])
    R = merge_sort(B[middle:])
    return merge(A, B)
#return A if len(A) <= 1 else merge(merge_sort(A[len(A)//2]), merge_sort(B[len(A)//2:]))

#числа Фибоначи
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    #matryoshka(5)
    #print(factorial(10))
    #print(degree(2, 10))
    #print(gcd(a, b))
    #print(fib(10))
