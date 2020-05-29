


import os,sys,shelve,time

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from Day6.Selesystem.conf.config  import *
from Day6.Selesystem.modules.school  import School
from Day6.Selesystem.modules.course  import Course
from Day6.Selesystem.modules.grade   import Grade
from Day6.Selesystem.modules.student import Student
from Day6.Selesystem.modules.teacher import Teacher



class Mainprogram(object):

    def __init__(self):
        pass

    def run(self):
        '''循环主界面'''
        while True:
            mainpage = '''
                           欢迎进入选课系统
    
                           1.学员视图
                           2.讲师视图
                           3.管理员
                           q.退出
                       '''
            print('\033[1;35m{}\033[0m'.format(mainpage))
            yourinput = input("\033[1;35m请输入你的选择： \033[0m").strip()
            if yourinput == 'q':
                print('退出~')
                quit()
            elif yourinput == '1':
                pass
            elif yourinput == '2':
                pass
            elif yourinput == '3':
                admin = Admin_view()
                admin.run_admin_view()
            else:
                print('输入错误，请重新输入')



class Admin_view(object):
    '''管理视图，学校、班级、课程、讲师的创建/管理/删除等'''
    def __init__(self):
        '''初始化时打开文件，后续可以实例化管理视图类来打开数据文件，操作数据'''
        self.schooldata = shelve.open(SCHOOL_DATADIR + "school.db",writeback = True)

    def __del__(self):
        '''无调用实例时关闭文件操作'''
        self.schooldata.close()
    def run_admin_view(self):
        '''管理视图主程序'''
        while True:
            #定义个字符串，与后面的字典key对应
            admin_view_page = '''
                        1:添加学校
                        2:管理学校
                        3:查看学校列表
                        4:删除学校
                        r:返回上一级
                        q:退出 
                        '''
            admin_view_page_data = {
                '1': 'add_school',
                '2': 'manage_school',
                '3': 'school_list',
                '4': 'del_school',
                'q': 'exit_program'
            }
            print('\033[1;35m{}\033[0m'.format(admin_view_page))
            yourinput = input("\033[1;35m 请输入你的选择：\033[0m").strip()
            if yourinput == 'r':
                self.schooldata.close()
            elif yourinput in admin_view_page_data:
                if hasattr(self,admin_view_page_data[yourinput]):
                    #利用反射机制，判断这个类中是否有对应的字符串（实际就是方法名）
                    getattr(self,admin_view_page_data[yourinput])()
                    #如果条件为真，那么执行这个方法，方法名()
            else:
                print('输入错误，没有这个选项')
                continue#继续循环
    def add_school(self):
        '''添加学校'''
        school_name = str(input("\033[1;35m请输入学校名称: \033[0m").strip())
        if school_name in self.schooldata:
            print('学校已存在')
        else:
            school_addr = str(input("\033[1;35m请输入学校地址: \033[0m").strip())
            self.schooldata[school_name] = School(school_name,school_addr)
            print('学校创建成功！')

    def school_list(self):
        '''学校列表'''
        for index,school in enumerate(self.schooldata):
            print('序号：{}\t\t学校名称：{}'.format(index + 1,school))

    def del_school(self):
        '''删除学校'''
        school_name = str(input("\033[1;35m请输入学校名称: \033[0m").strip())
        if school_name in self.schooldata:
            your_comfirm = str(input("是否确认删除，yes or no").strip())
            if your_comfirm == 'yes' or your_comfirm == 'YES':
                self.schooldata.pop(school_name)
                print('学校：{}已删除'.format(school_name))
            else:
                print('取消删除')
        else:
            print('学校不存在')
    def exit_program(self):
        quit()
    def manage_school(self):
        '''管理学校'''
        getattr(self, "school_list")()  #反射，调用school_list方法
        your_choiseschool = str(input("\033[1;35m请输入你要管理的学校名称: \033[0m").strip())
        while True:
            if your_choiseschool in self.schooldata:
                self.school_obj = self.schooldata[your_choiseschool]
                #schooldata[your_choiseschool]是学校的实例
                # 并且也是一个变量，指向内存学校的内存空间
                #self.school_obj = self.schooldata[your_choiseschool]相当于把学校实例当成key，加入个学校-老师字典
                manage_school_page = '''

                                1:添加讲师
                                2:添加班级
                                3:添加课程
                                4:查看讲师列表
                                5:查看班级列表
                                6:查看学校开设课程列表
                                7:删除讲师
                                8:删除班级
                                9:删除课程
                                r:返回上级
                                q:退出程序

                                '''
                # 将序号与方法通过字典关系起来
                manage_school_page_data = {
                    '1': 'add_teacher',
                    '2': 'add_grade',
                    '3': 'add_course',
                    '4': 'see_teacher_list',
                    '5': 'see_grade_list',
                    '6': 'see_course_list',
                    '7': 'del_teacher',
                    '8': 'del_grade',
                    '9': 'del_course',
                    'q': 'exit_program'
                }
                print('\033[1;35m {} \033[0m'.format(manage_school_page))
                your_choise1 = str(input("\033[1;35m 请输入你的选择： \033[0m").strip())
                if your_choise1 == 'r':
                    break
                if hasattr(self, manage_school_page_data[your_choise1]):
                    getattr(self, manage_school_page_data[your_choise1])()
                else:
                    print("\033[1;31m您的输入有误\033[0m")

            else:
                print("\033[1;35m 您输入的学校不存在\033[0m")
                break
    def add_teacher(self):
        '''添加讲师'''
        getattr(self,'see_teacher_list')()


        while True:
            teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
            if teacher_name in self.school_obj.school_teacher:
                print('讲师已存在,请重新输入')
                break
            else:
                teacher_passwd = str(input("\033[1;35m请输入讲师登录密码:\033[0m").strip())
                teacher_gender = str(input("\033[1;35m请输入讲师性别:\033[0m").strip())
                teacher_age = str(input("\033[1;35m请输入讲师年龄:\033[0m").strip())
                teacher_salary = str(input("\033[1;35m请输入讲师工资:\033[0m").strip())
                teacher_phonenumber = str(input("\033[1;35m请输入讲师电话号码:\033[0m").strip())
                print('\033[1;35m你输入的信息如下: \n 姓名: {}\n性别: {}\n年龄: {}\n工资: {}\n电话号码: {}\033[0m'.format(teacher_name,
                                                                                                      teacher_gender,
                                                                                                      teacher_age,
                                                                                                      teacher_salary,
                                                                                                      teacher_phonenumber))
                your_input = str(input("\033[1;35m确认请输入yes|YES，重新输入请输入 r,退出请输入 q。 :\033[0m").strip())
                if your_input == "yes" or "YES":
                    self.school_obj.add_schoolteacher(teacher_name, teacher_passwd, teacher_gender, teacher_age,
                                                      teacher_salary, teacher_phonenumber)
                    print('\033[1;35m 添加讲师{}成功\033[0m'.format(teacher_name))
                    break
                elif your_input == "q":
                    getattr("exit_program")()
                else:
                    print("\033[1;35m您的输入有误 \033[0m")
                    break

    def add_grade(self):
        '''添加班级'''

        while True:
            grade_name = str(input("\033[1;35m请输入班级姓名:\033[0m").strip())
            if grade_name in self.school_obj.school_grade:
                print('班级已存在,请重新输入')
                break
            else:
                grade_teacher = str(input("\033[1;35m请输入班级讲师姓名:\033[0m").strip())
                grade_course = str(input("\033[1;35m请输入班级课程:\033[0m").strip())
                print('\033[1;35m你输入的信息如下: \n 班级: {}\n班级讲师: {}\n班级课程: {}\n\033[0m'.format(grade_name,
                                                                                                      grade_teacher,
                                                                                                      grade_course))
                your_input = str(input("\033[1;35m确认请输入yes|YES，重新输入请输入 r,退出请输入 q。 :\033[0m").strip())
                if your_input == "yes" or "YES":
                    self.school_obj.add_schoolgrade(grade_name, grade_teacher, grade_course)
                    print('\033[1;35m 添加班级{}成功\033[0m'.format(grade_name))
                    break
                elif your_input == "q":
                    getattr("exit_program")()
                else:
                    print("\033[1;35m您的输入有误 \033[0m")
                    break

    def add_course(self):
        '''添加课程'''

        while True:
            course_name = str(input("\033[1;35m请输入课程姓名:\033[0m").strip())
            if course_name in self.school_obj.school_course:
                print('课程已存在,请重新输入')
                break
            else:
                course_cycle = str(input("\033[1;35m请输入课程周期:\033[0m").strip())
                course_price = str(input("\033[1;35m请输入学费课程:\033[0m").strip())
                print('\033[1;35m你输入的信息如下: \n 课程: {}\n课程周期: {}\n课程学费: {}\n\033[0m'.format(course_name,
                                                                                                      course_cycle,
                                                                                                      course_price))
                your_input = str(input("\033[1;35m确认请输入yes|YES，重新输入请输入 r,退出请输入 q。 :\033[0m").strip())
                if your_input == "yes" or "YES":
                    self.school_obj.add_schoolcourse(course_name, course_cycle, course_price)
                    print('\033[1;35m 添加课程{}成功\033[0m'.format(course_name))
                    break
                elif your_input == "q":
                    getattr("exit_program")()
                else:
                    print("\033[1;35m您的输入有误 \033[0m")
                    break

    def see_teacher_list(self):
        '''查询讲师列表'''
        for index,taacher in enumerate(self.school_obj.school_teacher):
            print('讲师编号：{}\t讲师姓名：{}'.format(index + 1,taacher))
    def see_grade_list(self):
        '''查询班级列表'''
        for index,grade in enumerate(self.school_obj.school_grade):
            print('班级编号：{}\t班级：{}'.format(index + 1,grade))

    def see_course_list(self):
        '''查询讲师列表'''
        for index,course in enumerate(self.school_obj.school_course):
            print('课程编号：{}\t课程：{}'.format(index + 1,course))


    def del_teacher(self):
        '''删除讲师'''
        getattr(self,'see_teacher_list')()
        teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
        if teacher_name in self.school_obj.school_teacher:
            self.school_obj.school_teacher.pop(teacher_name)
            print('删除讲师：{}成功'.format(teacher_name))
        else:
            print('查无此人')
    def del_grade(self):
        '''删除班级'''
        getattr(self,'see_grade_list')()
        grade_name = str(input("\033[1;35m请输入班级名称:\033[0m").strip())
        if grade_name in self.school_obj.school_grade:
            self.school_obj.school_teacher.pop(grade_name)
            print('删除班级：{}成功'.format(grade_name))
        else:
            print('没有这个班级')
    def del_course(self):
        '''删除课程'''
        getattr(self,'see_course_list')()
        course_name = str(input("\033[1;35m请输入课程名称:\033[0m").strip())
        if course_name in self.school_obj.school_course:
            self.school_obj.school_teacher.pop(course_name)
            print('删除课程：{}成功'.format(course_name))
        else:
            print('没有这个课程')



class Student_view(object):
    pass


class Teacher_view(object):
    pass



if __name__ == '__main__':
    m = Mainprogram()
    m.run()