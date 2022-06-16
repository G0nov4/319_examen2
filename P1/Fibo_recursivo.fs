open System

let rec fib n =
    match n with
    | 1 -> 0
    | 2 | 3 -> 1
    | n -> fib(n-1) + fib(n-2) + fib(n-3)

[<EntryPoint>]
let main argv =
    Console.WriteLine("Ingrese un numero: ")
    let n = Console.ReadLine();
    for i in 1 .. int(n) do
        Console.WriteLine(fib(i))
    0;