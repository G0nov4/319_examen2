def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    sum = fib(n-1) + fib(n-2) + fib(n-3)
    return sum

def list(f,n):
    for i in range(0, n):
        print(f(i), end= " ")


#########################################################
## 3ra Pregunta Fibonnacc con funciones de orden superior
## 0,1,1,2,4,7,13
#########################################################

list(fib, 10)