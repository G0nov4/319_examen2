def fibonacci(count): 
    fib_list = [0, 1] 
    any(map(lambda fibo: fib_list.append(sum(fib_list[-3:])), range(2, count))) 
    return fib_list[:count] 
  
n = int(input("Ingrese un numero:\n>> "))
print(fibonacci(n))
