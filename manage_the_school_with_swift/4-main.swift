var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)
var m2 = Mentor(first_name: "Gus", last_name: "Fring", age: 54, subject: Subject.English)
var m3 = Mentor(first_name: "Walter", last_name: "White", age: 52, subject: Subject.Math)


var school = School(name: "Holberton")
school.addStudent(s)
school.addMentor(m)
school.addMentor(m2)
school.addMentor(m3)

var students = school.listStudents()
for student in students
{
    print("Student: \(student.fullName())")
}

var mentors = school.listMentors()
for mentor in mentors
{
    print("Mentor: \(mentor.fullName())")
}

var mentors_math = school.listMentorsBySubject(Subject.Math)
for mentor_math in mentors_math
{
    print("Mentor Math: \(mentor_math.fullName())")
}
