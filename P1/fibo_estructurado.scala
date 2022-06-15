object Fibo {
    def fib2( n : Int ) {
    var a = 0
    var b = 0
    var c = 1
    var i = 0	  
    
    while( i < n ) {
        val sum = a + b + c
        a = b
        b = c
        c = sum
        print(a+" ")
        i = i + 1
    }  
    }
    def main(args:Array[String]): Unit = {
        print("Ingrese un valor N:")
        val n = scala.io.StdIn.readInt()
        fib2(n)
    }
}
