// Defines subjects in school
enum Subject {
        case Math
        case English
        case French
        case History
}

// Defines method to classify students and mentors
protocol Classify {
        func isStudent() -> Bool
}

// Defines a Person class inheriting CustomStringConvertible
class Person: CustomStringConvertible {
        var first_name: String
        var last_name: String
        var age: Int

        // Initializes Person class with listed attributes
        init(first_name: String, last_name: String, age: Int) {
                self.first_name = first_name
                self.last_name = last_name
                self.age = age
        }

        // Concatenates first_name and last_name string with space
        func fullName() -> String {
                return self.first_name + " " + self.last_name
        }

        // Defines string to return on print call for class
        var description:String {
                return self.fullName()
        }
}

// Defines Student class that inherits from Person class and Classify protocol
class Student: Person, Classify {
        var list_exercises: [Exercise] = []

        // Returns that Person is a Student
        func isStudent() -> Bool {
                return true
        }

        // Returns average of grades in a specific subject
        func average(subject: Subject) -> Float {
                var total: Int = 0
                var i: Int = 0
                for exercise in list_exercises {
                        if exercise.subject == subject {
                                total += exercise.note
                                i += 1
                        }
                }
                return (Float)(total) / (Float)(i)
        }

        // Returns average of all grades in all subjects
        func averageAll() -> Float {
                var total: Int = 0
                var i: Int = 0
                for exercise in list_exercises {
                        total = total + exercise.note
                        i = i + 1
                }
                return (Float)(total) / (Float)(i)
        }

        // Creates a new Exercise and adds to list of Exercises
        func addNewNote(subject: Subject, note: Int) {
                let new: Exercise = Exercise(subject:subject)
                new.setNote(note)
                list_exercises.append(new)
        }
}

// Defines Mentor class which inherits from Person class and Classify protocol
class Mentor: Person, Classify {
        let subject: Subject

        // Initiates Mentor class with listed attributes
        init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
                self.subject = subject
                super.init(first_name:first_name, last_name:last_name, age:age)
        }

        // Returns that a Mentor is not a student
        func isStudent() -> Bool {
                return false
        }

        // Returns string related to subject enum
        func stringSubject() -> String {
                switch (self.subject) {
                        case .Math:
                                return "Math"
                        case .English:
                                return "English"
                        case .French:
                                return "French"
                        case .History:
                                return "History"
                }
        }
}


// Defines School class with listed attributes
class School {
        var name: String
        var list_persons: [Person] = []

        // Initializes School class object
        init(name: String) {
                self.name = name
        }

        // Adds student to the School Person list and returns true
        func addStudent(p: Person) -> Bool {
                if p is Student {
                        list_persons.append(p)
                        return true
                }
                return false
        }

        // Adds mentor to the School person list and returns true
        func addMentor(p: Person) -> Bool {
                if p is Mentor {
                        list_persons.append(p)
                        return true
                }
                return false
        }

        // Returns a list of the students in the school
        func listStudents() -> [Person] {
                var list: [Person] = []
                for person in list_persons {
                        if person is Student {
                                list.append(person)
                        }
                }
                list = list.sort {$0.age > $1.age}
                return list
        }

        // Returns a list of the mentors in the school
        func listMentors() -> [Person] {
                var list: [Person] = []
                for person in list_persons {
                        if person is Mentor {
                                list.append(person)
                        }
                }
                list = list.sort {$0.age > $1.age}
                return list
        }

        // Returns list of mentors for a specific subject
        func listMentorsBySubject(subject: Subject) -> [Person] {
                var list: [Person] = []
                for person in list_persons {
                        let mentor = person as? Mentor
                        if mentor != nil && mentor!.subject == subject {
                                list.append(person)
                        }
                }
                list = list.sort {$0.age > $1.age}
                return list
        }

        // Returns the average age of mentors
        func mentorsAgeAverge() -> Int {
                let list: [Person] = self.listMentors()
                var total:Int = 0
                var i:Int = 0
                for person in list {
                        total += person.age
                        i += 1
                }
                return total / i
        }

        // Returns the average age of students
        func studentsAgeAverge() -> Int {
                let list: [Person] = self.listStudents()
                var total: Int = 0
                var i: Int = 0
                for person in list {
                        total += person.age
                        i += 1
                }
                return total / i
        }

        // Returns the average grade of students in a specific subject
        func average(subject: Subject) -> Float {
                var total: Float = 0
                var i: Int = 0
                for student in self.listStudents() {
                        let current = student as? Student
                        if current != nil {
                                total += current!.average(subject)
                                i += 1
                        }
                }
                return total / (Float)(i)
        }

        // Returns the average overall grade of students
        func averageAll() -> Float {
                var total: Float = 0
                var i: Float = 0
                var avg: Float
                var totalAvg: Float
                for student in self.listStudents() {
                        let current = student as? Student
                        if current != nil {
                                avg = current!.averageAll()
                                total += avg
                                i += 1
                        }
                }
                totalAvg = total / i
                return totalAvg
        }
}

// Defines the Exercise class
class Exercise {
        let subject: Subject
        var note: Int

        // Initializes the Exercise class object
        init(subject: Subject) {
                self.subject = subject
                self.note = 0
        }

        // Sets the grade for a given Exercise object
        func setNote(note: Int) {
                if note < 0 {
                        self.note = 0
                } else if note > 10 {
                        self.note = 10
                } else {
                        self.note = note
                }
        }
}
