var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)
var m2 = Mentor(first_name: "Gus", last_name: "Fring", age: 54, subject: Subject.English)
var m3 = Mentor(first_name: "Walter", last_name: "White", age: 52, subject: Subject.Math)

print(s)
print(m3)

var school = School(name: "Holberton")
school.addStudent(s)
school.addMentor(m)
school.addMentor(m2)
school.addMentor(m3)

print("Mentors age average: \(school.mentorsAgeAverge())")
print("Students age average: \(school.studentsAgeAverge())")    
