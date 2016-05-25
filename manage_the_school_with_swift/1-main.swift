var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var t = Mentor(first_name: "Alex", last_name: "Rap", age: 34)

if s.isStudent()
{
    print("\(s.fullName()) is student")
}
if t.isStudent()
{
    print("\(t.fullName()) is student")
}
