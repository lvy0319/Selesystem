
from Day6.Selesystem.modules.course import Course
from Day6.Selesystem.modules.teacher import Teacher
from Day6.Selesystem.modules.grade import Grade

class School(object):

    def __init__(self,school_name,school_addr):
        '''学校类，学校名称、学校地址'''
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        # 学校-课程关系，调用增加学校讲师接口，实例化讲师类，并和学校对应，课程名称是key，课程实例是value（内存地址）
        self.school_grade = {}
        # 学校-班级关系，调用增加学校课程接口，实例化课程类，并和学校对应，班级名称是key，班级实例是value
        self.school_teacher = {}
        # 学校-讲师关系，调用增加学校班级接口，实例化班级类，并和学校对应，讲师名称是key，讲师实例是value

    def add_schoolteacher(self,teacher_name,teacher_passwd,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber):
        '''添加学校讲师对象到self.school_teacher字典中'''
        newteacher = Teacher(teacher_name,teacher_passwd,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber)
        self.school_teacher[teacher_name] = newteacher

    def add_schoolcourse(self, course_name, course_cycle, course_price):
        '''添加课程对象到self.school_course字典中'''
        newcourse = Course(course_name, course_cycle, course_price)
        self.school_course[course_name] = newcourse

    def add_schoolgrade(self, grade_name, grade_teacher, grade_course):
        '''添加班级对象到self.school_grade字典中'''
        newgrade = Grade(grade_name, grade_teacher, grade_course)
        self.school_grade[grade_name] = newgrade