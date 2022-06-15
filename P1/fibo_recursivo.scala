object Fibonacci {
    def fibonacci(n: Int): Int = {
        if (n == 0) {
            return 0
        }
        if (n == 1){
            return 1
        }
        if ( n == 2){
            return 1
        }
        else fibonacci(n - 1) + fibonacci(n - 2) + fibonacci(n - 3)
    }

    def main(args: Array[String]) {
        print("Ingrese un valor N:")
        val n = scala.io.StdIn.readInt()
        for {i <- List.range(0, n)} 
            yield { print(fibonacci(i) + " ") }
    }
}