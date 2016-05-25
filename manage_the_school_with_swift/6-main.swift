var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var s1 = Student(first_name: "Saul", last_name: "Goodman", age: 18)
var s2 = Student(first_name: "Hank", last_name: "Schrader", age: 22)

var school = School(name: "Holberton")
school.addStudent(s)
school.addStudent(s1)
school.addStudent(s2)

s.addNewNote(Subject.Math, note:4)
s.addNewNote(Subject.French, note:5)
s.addNewNote(Subject.Math, note:7)

s1.addNewNote(Subject.Math, note:10)
s1.addNewNote(Subject.French, note:2)
s1.addNewNote(Subject.Math, note:9)

s2.addNewNote(Subject.Math, note:2)
s2.addNewNote(Subject.French, note:6)
s2.addNewNote(Subject.Math, note:4)

print("\(s) has \(s.average(Subject.Math))/10 in Math")
print("\(s1) has \(s1.average(Subject.Math))/10 in Math")
print("\(s2) has \(s2.average(Subject.Math))/10 in Math")

print("And the entire school has \(school.average(Subject.Math))/10 in Math")

print("\(s) has \(s.averageAll())/10 in total")
print("\(s1) has \(s1.averageAll())/10 in total")
print("\(s2) has \(s2.averageAll())/10 in total")

print ("And the entire school has \(school.averageAll())/10 in total")
