// Reverses an array of integers
func reverse_array(a: [Int]) -> ([Int]) {
        return (a.count - 1).stride(to: -1, by: -1).map { a[$0] }
}
