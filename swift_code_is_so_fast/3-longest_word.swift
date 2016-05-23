// Returns the longest word in a string

func longest_word(text: String) -> (String) {
        let textArr = text.characters.split{$0 == " "}.map(String.init)
        var longest:String = ""
        for word in textArr {
                let longLen:Int = longest.characters.count
                let len:Int = word.characters.count
                if len > longLen {
                        longest = word
                }
        }
        return longest
}
