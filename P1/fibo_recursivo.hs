fib::Int->Int->Int->Int->String
fib 0 a b c =""
fib n 0 0 0 = show(0)++" "++fib (n-1) 0 0 1
fib n 0 0 1 = show(1)++" "++fib (n-1) 0 1 1
fib n 0 1 1 = show(1)++" "++fib (n-1) 1 1 2
fib n a b c=show(c)++" "++fib (n-1) (b) (c) (a+b+c)

fibo::Int->String
fibo n= fib n 0 0 0

main :: IO ()
main = do
    n <- getLine
    let prn = fibo(read n)
    print prn