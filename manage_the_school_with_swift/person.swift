enum Subject {
        case Math
        case English
        case French
        case History
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

protocol Classify {
        func isStudent() -> Bool
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
