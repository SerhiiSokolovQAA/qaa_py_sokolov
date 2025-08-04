from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"<Student(name={self.name})>"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"<Course(name={self.name})>"

engine = create_engine('sqlite:///students.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

course_names = ["Math", "Physics", "Biology", "History", "Programming"]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()

for i in range(1, 21):
    student = Student(name=f"Student_{i}")
    student.courses = random.sample(courses, k=random.randint(1, 3))
    session.add(student)

session.commit()

def add_student(name, course_ids):
    new_student = Student(name=name)
    new_student.courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    session.add(new_student)
    session.commit()
    print(f"Student '{name}' added to the courses: {course_ids}")

add_student("New_Student", [1, 3])

def get_students_in_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        print(f"Students on the course '{course.name}':")
        for student in course.students:
            print("-", student.name)
    else:
        print("Course not found.")

get_students_in_course("Math")

def get_courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Students courses '{student.name}':")
        for course in student.courses:
            print("-", course.name)
    else:
        print("Can not find student.")

get_courses_of_student("New_Student")

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Name of the student updated from '{old_name}' to '{new_name}'")
    else:
        print("Can not find student.")

update_student_name("New_Student", "Updated_Student")

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student '{name}' deleted.")
    else:
        print("Can not find student.")

delete_student("Updated_Student")
