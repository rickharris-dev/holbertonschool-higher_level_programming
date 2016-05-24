var numbers = [4, 7, 1, 9, 6, 5, 6, 9]

// Finds the largest number in an array of integers
let max = numbers.sort(){$0 > $1}[0]

print(max)
