var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)

if s.isStudent()
{
    print("\(s.fullName()) is student")
}
if m.isStudent()
{
    print("\(m.fullName()) is student")
}
else
{
    print("\(m.fullName()) is mentor of \(m.stringSubject())")
}
