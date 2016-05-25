enum Subject {
        case Math
        case English
        case French
        case History
}

protocol Classify {
        func isStudent() -> Bool
}

class Person {
        var first_name: String
        var last_name: String
        var age: Int

        init(first_name: String, last_name: String, age: Int) {
                self.first_name = first_name
                self.last_name = last_name
                self.age = age
        }

        func fullName() -> String {
                return self.first_name + " " + self.last_name
        }
}

class Student: Person, Classify {
        func isStudent() -> Bool {
                return true
        }
}

class Mentor: Person, Classify {
        let subject: Subject

        init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
                self.subject = subject
                super.init(first_name:first_name, last_name:last_name, age:age)
        }

        func isStudent() -> Bool {
                return false
        }

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

class School {
        var name: String
        var list_persons: [Person] = []

        init(name: String) {
                self.name = name
        }

        func addStudent(p: Person) -> Bool {
                if p is Student {
                        list_persons.append(p)
                        return true
                }
                return false
        }

        func addMentor(p: Person) -> Bool {
                if p is Mentor {
                        list_persons.append(p)
                        return true
                }
                return false
        }

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
}
