// Returns true if number is prime

func is_prime(number: Int) -> (Bool) {
        var max:Int = number
        var i:Int = 2
        if number < 2 {
                return false
        } else if number == 2 {
                return true
        }

        while i < max {
                if number % i == 0 {
                        return false
                }
                max = number / i
                i += 1
        }
        return true
}
