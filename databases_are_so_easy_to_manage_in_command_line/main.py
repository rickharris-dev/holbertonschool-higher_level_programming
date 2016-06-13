from sys import argv
from models import *

def create_tables():
    ''' Function connects to database and created all tables'''
    my_models_db.connect()
    my_models_db.create_tables([School, Batch, User, Student])

def print_table():
    ''' Function prints each row of the given table '''
    if len(argv) == 3:
        if argv[2] == "school":
            rows = School.select()
            for row in rows:
                print row
        elif argv[2] == "batch":
            rows = Batch.select()
            for row in rows:
                print row
        elif argv[2] == "user":
            rows = User.select()
            for row in rows:
                print row
        elif argv[2] == "student":
            rows = Student.select()
            for row in rows:
                print row

def insert_record():
    ''' Inserts a new record into the given table with the give data '''
    try:
        with my_models_db.transaction():
            if argv[2] == "school":
                new = School.create(
                    name=argv[3]
                )
                print "New school: " + str(new)
            elif argv[2] == "batch":
                new = Batch.create(
                    school=argv[3],
                    name=argv[4],
                )
                print "New batch: " + str(new)
            elif argv[2] == "student":
                if len(argv) == 7:
                    new = Student.create(
                        batch=int(argv[3]),
                        age=int(argv[4]),
                        last_name=argv[5],
                        first_name=argv[6],
                    )
                else:
                    new = Student.create(
                        batch=int(argv[3]),
                        age=int(argv[4]),
                        last_name=argv[5],
                    )
                print "New student: " + str(new)
    except peewee.IntegrityError:
        flash('That username is already taken')

def delete_tables():
    '''Deletes the given record from the given table '''
    if argv[2] == "school":
        query = School.select().where(Schools.id == argv[3])
        if query.exists():
            target = query.get()
            School.delete().where(School.id == argv[3]).execute()
            print "Delete: " + str(target)
        else:
            print "Nothing to delete"
    elif argv[2] == "batch":
        query = Batch.select().where(Batch.id == argv[3])
        if query.exists():
            target = query.get()
            Batch.delete().where(Batch.id == argv[3]).execute()
            print "Delete: " + str(target)
        else:
            print "Nothing to delete"
    elif argv[2] == "student":
        query = Student.select().where(Student.id == argv[3])
        if query.exists():
            target = query.get()
            Student.delete().where(Student.id == argv[3]).execute()
            print "Delete: " + str(target)
        else:
            print "Nothing to delete"

def print_batch_by_school():
    ''' Prints the batch based on the given school '''
    query = (School
             .select()
             .where(School.id == argv[2]))
    if query.exists():
        data = (Batch
                .select()
                .where(Batch.school == argv[2]))
        for batch in data:
            print batch
    else:
        print "School not found"

def print_student_by_batch():
    ''' Prints students by the given batch '''
    query = (Batch
             .select()
             .where(Batch.id == argv[2]))
    if query.exists():
        data = (Student
                .select()
                .where(Student.batch == argv[2]))
        for student in data:
            print student
    else:
        print "Batch not found"

def print_student_by_school():
    ''' Prints students attending the given school '''
    query = (School
            .select()
            .where(School.id == argv[2]))
    if query.exists():
        data = (Student
                .select()
                .join(Batch)
                .where(Batch.school == argv[2]))
        for student in data:
            print student
    else:
        print "School not found"

def print_family():
    ''' Prints students by last name '''
    query = (Student
             .select()
             .where(Student.last_name == argv[2]))
    for student in query:
        print student

def age_average():
    ''' Prints the average age of all students or by batch '''
    if len(argv) == 3:
        query = (Student
                 .select(
                     peewee.fn.Avg(Student.age)
                     .alias('age_avg'))
                 .where(Student.batch == argv[2])).get()
        print query.age_avg
    else:
        query = (Student
                 .select(
                     peewee.fn.Avg(Student.age)
                     .alias('age_avg'))).get()
        print query.age_avg

def change_batch():
    ''' Moves student to a new batch '''
    student = (Student
               .select()
               .where(Student.id == argv[2]))
    batch = (Batch
             .select()
             .where(Batch.id == argv[3]))

    if student.exists():
        student = student.get()
        if batch.exists():
            batch = batch.get()
            print student.batch.id
            if student.batch != batch:
                student.batch = batch
                student.save()
                print str(student) + " has been moved to " + str(batch)
            else:
                print str(student) + " already in " + str(batch)
        else:
            print "Batch not found"
    else:
        print "Student not found"

def print_all():
    ''' Prints all Students by batch and School '''
    schools = School.select()
    batches = (Batch
               .select()
               .join(School))
    students = (Student.select()
                .join(Batch))
    for school in schools:
        print school
        school_batches = batches.where(School.id == school.id)
        for batch in school_batches:
            print '\t' + str(batch)
            batch_students = students.where(Batch.id == batch.id)
            for student in batch_students:
                print '\t\t' + str(student)

''' Initializes the action or prints error '''
if len(argv) < 2:
    print "Please enter an action"
elif argv[1] == "create":
    create_tables()
elif argv[1] == "print":
    print_table()
elif argv[1] == "insert":
    insert_record()
elif argv[1] == "delete":
    delete_tables()
elif argv[1] == "print_batch_by_school":
    print_batch_by_school()
elif argv[1] == "print_student_by_batch":
    print_student_by_batch()
elif argv[1] == "print_student_by_school":
    print_student_by_school()
elif argv[1] == "print_family":
    print_family()
elif argv[1] == "age_average":
    age_average()
elif argv[1] == "change_batch":
    change_batch()
elif argv[1] == "print_all":
    print_all()
else:
    print "Undefined action " + argv[1]
