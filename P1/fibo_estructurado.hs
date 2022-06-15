fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo 2 = 1
fibo n = (fibo (n-1)) + (fibo (n-2) + fibo(n-3))


main :: IO ()
main = do
    n <- getLine
    let prn = fibo(read n-1)
    print prn