var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)

var school = School(name: "Holberton")
if(school.addStudent(s)) {
    print("\(s.fullName()) is now student in the school!")
}
if(school.addMentor(s)) {
    print("\(s.fullName()) is now mentor in the school!")
}
if(school.addStudent(m)) {
    print("\(m.fullName()) is now student in the school!")
}
if(school.addMentor(m)) {
    print("\(m.fullName()) is now mentor in the school!")
}
