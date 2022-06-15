n = int(input('Introduce un un número:\n>> '))
fibo=[]
#########################################################
## 1ra Pregunta Fibonnacci en programcacion estructurada
## 0,1,1,2,4,7,13
#########################################################
if ( n == 0 ):
    print('...')
elif(n == 1):
    print(0)
elif(n == 2):
    print('0 1')
elif(n == 3):
    print('0 1 1')
elif(n > 3):
    a = 0
    b = 0
    c = 1
    flag = 0
    sum = 0
    while flag < n:
        fibo.append(b)
        flag+=1
        sum=a+b+c
        a=b
        b=c
        c=sum
    print(fibo)