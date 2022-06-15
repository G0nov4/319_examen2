def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    sum = fib(n-1) + fib(n-2) + fib(n-3)
    return sum

#########################################################
## 1ra Pregunta Fibonnacci en programcacion recurisiva
## 0,1,1,2,4,7,13
#########################################################
n = int(input('Introduce un un número:\n>> '))
flag = -1
fibo=[]
while flag < n-1:
    flag += 1
    fibo.append(fib(flag))
print(fibo)