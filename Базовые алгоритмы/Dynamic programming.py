#примеры задач динамического программирования

#числа Фибоначи
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#Задача о кузнечике (сразу с платным посещением ячеек)
#Суть задачи: кузнечи мжет посещать только i+1 и i+2 ячейки вперёд,
#посещение ячеек платное. Найти стоимость наиболее дешёвого пути до n

def find_shortest_path(price, n):
    C = [float('inf'), price[1]] + [0]*(n-1)
    for i in range(2, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    print(*enumerate(C)) #мы выводим весь список посещений клеток для наглядности. ответ в Схшъ
#вывод правильного пути
    path = [n]
    i = n
    while i!= 1:
        if C[i-1] < C[i-2]:
            i -= 1
        else:
            i -= 2
        path.append(i)
   # path[:] =  path[::-1] #инверсия списка через срезы
    path.reverse()
    return path

price = [0, 10, 2 ,2 , 1, 6, 2, 3, 0, 1, 3]
path = find_shortest_path(price, 10)
print(path)
