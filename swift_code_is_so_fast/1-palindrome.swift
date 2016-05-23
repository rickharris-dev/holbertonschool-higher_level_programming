// Takes a string and returns True if is a palindrome
func is_palindrome(s: String) -> (Bool) {
        let r = String(s.characters.reverse())
        return s == r
}
