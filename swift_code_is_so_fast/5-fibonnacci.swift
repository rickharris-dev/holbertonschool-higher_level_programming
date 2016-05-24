// Function returns the fibonacci number at the given index

func fibonacci(number: Int) -> (Int) {
        var i:Int = 2
        var a:Int = 1
        var b:Int = 1
        var c:Int = 0
        if number == 0 {
                return a
        } else if number == 1 {
                return b
        } else {
                while i < number {
                        c = a
                        a = b
                        b = c + a
                        i += 1
                }
                return b
        }
}
