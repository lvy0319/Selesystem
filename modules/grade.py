

from Day6.Selesystem.modules.student import Student

class Grade(object):
    '''班级类，定义班级名称,班级讲师，绑定班级课程,班级包含的学生'''
    def __init__(self ,grade_name ,grade_teacher ,grade_course):
        self.grade_name = grade_name
        self.grade_teacher = grade_teacher
        self.grade_course = grade_course
        self.grade_student = {}
        #班级-学员关系，调用增加班级学员接口，实例化学生，并和班级对应，学生姓名是key，学生实例是value

    def add_grade_student(self ,student_name ,student_passwd ,student_gender ,student_age):
        newstudent = Student(student_name ,student_passwd ,student_gender ,student_age)
        self.grade_student[student_name] = newstudent