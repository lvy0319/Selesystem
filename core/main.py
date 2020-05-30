


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
                student = Student_view()
                student.run_student_view()
            elif yourinput == '2':
                teacher = Teacher_view()
                teacher.run_teacher_view()
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
            #实例化学校，写到文件中类似这样，学校字符串（对象）：学校实例
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
                #schooldata[your_choiseschool]是学校的实例，school_obj是学校的实例化对象
                # 并且也是一个变量，指向内存学校的内存空间
                #self.school_obj = self.schooldata[your_choiseschool]相当于把学校实例当成key，学校-老师字典整体是个value
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
                    #这一步做了，add_schoolteacher实例化老师对象，生成一个讲师名称：讲师实例的字典key-value
                    #通过school_obj，意思是与学校建立了关系{'学校实例':{'老师':'老师实例'}}类似这样
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
    '''学生视图，学生注册，选择学校，选择班级'''

    def __init__(self):
        '''初始化时打开文件，后续可以实例化管理视图类来打开数据文件，操作数据'''
        self.admin_view_obj = Admin_view()

    def __del__(self):
        '''无调用实例时关闭文件操作'''
        self.admin_view_obj.schooldata.close()

    def run_student_view(self):
        '''学生视图主程序入口'''
        self.admin_view_obj.school_list()
        self.your_choiceschool = str(input("\033[1;35m 请输入你要进入的学校：\033[0m").strip())
        self.your_choiseschool_obj = self.admin_view_obj.schooldata[self.your_choiceschool]
        #self.admin_view_obj.schooldata[self.your_choiceschool]表示学校实例，同时也是key
        #把学校实例赋值给一个变量，使他可以使用学校key的value
        for i in self.your_choiseschool_obj.school_grade:
            grade_obj = self.your_choiseschool_obj.school_grade[i]
            print('''\033[1;35m
                        班级名称: {}
                        班级所开课程: {}
                        班级讲师: {}
                        \n\n\033[0m'''.format(grade_obj.grade_name,
                                              grade_obj.grade_course,
                                              grade_obj.grade_teacher))
        self.your_choisegrade = str(input("\033[1;35m请输入你要选择的班级: \033[0m").strip())

        self.grade_obj = self.your_choiseschool_obj.school_grade[self.your_choisegrade]
        #self.your_choiseschool_obj.school_grade[self.your_choisegrade]通过学校实例找到对应学校-班级字典
        #再通过班级找对应value，赋值给一个变量，value也是一个实例，是班级的实例，相当于实例化班级
        print('\033[1;35m欢迎来到 {}学校 \033[0m'.format(self.your_choiceschool))
        while True:
            student_view_page = '''
                    1:学员注册
                    2:学员缴费
                    3:学员注销
                    r:返回上一级
                    q:退出登录
                    '''
            student_view_page_data = {
                '1': 'student_registered',
                '2': 'studen_paycost',
                '3': 'student_del',
            }
            print('\033[1;35m\n\n{}\n\n\033[0m'.format(student_view_page))
            your_input = str(input("\033[1;35m请选择：  \033[0m").strip())
            if your_input == "r":
                self.admin_view_obj.schooldata.close()
                #这里的返回上一级，也相当于跳出学生视图，不在这个类中，文件不能一直是打开状态
                break
            elif your_input == "q":
                quit()
            if hasattr(self, student_view_page_data[your_input]):
                getattr(self, student_view_page_data[your_input])()
            else:
                print("\033[1;35m您的输入有误 !\033[0m")

    def student_registered(self):
        '''学生注册'''
        student_name = str(input("\033[1;35m请输入你的姓名 \033[0m").strip())
        if student_name in self.grade_obj.grade_student:
            #班级对象grade_obj，实例化班级类的时候，里面有班级和学生的对应字典

            print("\033[1;35m该学生已经存在。 \033[0m")
        else:
            student_passwd = str(input("\033[1;35m请设置你的用户密码: \033[0m").strip())
            student_gender = str(input("\033[1;35m请设置你的性别: \033[0m").strip())
            student_age = str(input("\033[1;35m请输入你的年龄: \033[0m").strip())
            self.grade_obj.add_grade_student(student_name, student_passwd, student_gender, student_age)
            #创建学生实例的时候，同时与班级建立对应关系
            #这里是最绕的，学校-班级-学生的对应关系是如何建立，还有数据的结构：
            #1.实例化学校时，实际上创建了学校，并以key-value形式写到文件db中，学校：学校实例 存储
            #2.学校实例中有三个方法，可以创建班级、课程、讲师，并保存到对应字典，以对象：实例 方式存储
            #3.创建班级、课程、讲师时文件还是打开和写入状态，这时存在对应关系学校-班级等，学校：{班级：班级实例}方式存储
            #4.学生的时候可以通过班级类创建，保存班级-学生的对应关系，大概的关系如下：
            # {'学校名': 学校实例':{
            #             '班级名'：{（班级实例）:{'学生': 学生实例}
            # }
            # {'讲师': 讲师实例}
            # {'课程': 课程实例}
            # }

            print('''\033[1;35m\n恭喜添加{}用户成功.\n\n
                    您所在的班级是: {}
                    您报名的课程是: {}
                    您的班级讲师是: {}\033[0m'''.format(student_name, self.your_choisegrade, self.grade_obj.grade_course,
                                                 self.grade_obj.grade_teacher))

    def student_del(self):
        '''学员注销'''
        print("学员注销")
        input_name = str(input("\033[1;35m请输入注销用户的用户名: \033[0m").strip())
        input_passwd = str(input("\033[1;35m请输入注销用户的用户密码: \033[0m").strip())
        if input_name in self.grade_obj.grade_student and input_passwd == self.student_obj.student_passwd:
            self.grade_obj.grade_student.pop[input_name]
            print("\033[1;35m学生{}删除成功 \033[0m".format(input_name))
        else:
            print("\033[1;35m您输入的用户不存在或者密码错误. \033[0m".format(input_name))

    def studen_paycost(self):
        '''学员缴费'''
        input_name = str(input("\033[1;35m请输入注销用户的用户名: \033[0m").strip())
        input_passwd = str(input("\033[1;35m请输入注销用户的用户密码: \033[0m").strip())
        self.student_obj = self.grade_obj.grade_student[input_name]
        if input_name in self.grade_obj.grade_student and input_passwd == self.student_obj.student_passwd:
            course_price = self.your_choiseschool_obj.school_course[self.grade_obj.grade_course].course_price
            #1.self.your_choiseschool_obj是学校实例
            #2.学校实例访问学校-课程字典，需要拿到对应的课程实例
            #3.self.grade_obj实际是self.your_choiseschool_obj.school_grade[班级]，也就是班级实例
            #4.self.grade_obj.grade_course也就是班级课程字段，拿到课程实例
            #5.课程类中有课程价格course_price
            print("\033[1;35m你报名的课程是{},需要支付{}元 \033[0m".format(self.grade_obj.grade_course,course_price))
            your_input6 = str(input("\033[1;35m确认支付请输入yes|YES，输入其他视为放弃支付。 \033[0m").strip())
            if your_input6 == "yes" or "YES":
                self.student_obj.paycost_status = True
                print("\033[1;34m 恭喜你 ，支付完成，你已经缴费成功\033[0m")
            else:
                print("\033[1;34m 您的输入有误。\033[0m")
        else:
            print("\033[1;34m 您的输入有误。\033[0m")







class Teacher_view(object):
    '''讲师视图，查看学生成绩，查看个人信息，查看班级学生列表'''

    def __init__(self):
        self.admin_view_obj = Admin_view()

    def __del__(self):
        self.admin_view_obj.schooldata.close()
    def run_teacher_view(self):
        '''讲师视图主程序入口'''
        self.admin_view_obj.school_list()
        self.your_choiseschool = input("\033[1;35m 请输入你要进入的学校：\033[0m").strip()
        if self.your_choiseschool in self.admin_view_obj.schooldata:
            self.your_choiseschool_obj = self.admin_view_obj.schooldata[self.your_choiseschool]
            #实例化学校
            teacher_name = str(input("\033[1;35m 请输入你的讲师姓名：\033[0m").strip())
            teacher_passwd = str(input("\033[1;35m 请输入你的登录密码：\033[0m").strip())
            if teacher_name in self.your_choiseschool_obj.school_teacher and teacher_passwd ==\
                    self.your_choiseschool_obj.school_teacher[teacher_name].teacher_passwd:
                self.teacher_obj = self.your_choiseschool_obj.school_teacher[teacher_name]
                # 实例化讲师对象,通过学校实例找到学校-讲师字典，拿到对应讲师实例
                print("\033[1;35m{}讲师,欢迎你\033[0m".format(teacher_name))
                while True:
                    teacher_page = '''
                                        1.查看个人信息
                                        2.查看班级学生名单
                                        r.返回上一级
                                        q.退出登录
                                    '''
                    teacher_page_data = {
                        '1': 'teacher_info',
                        '2': 'student_list',
                    }

                    print("\033[1;35m{}\033[0m".format(teacher_page))
                    your_input = str(input("\033[1;35m 请输入你的选择：\033[0m").strip())
                    if your_input == "r":
                        self.admin_view_obj.schooldata.close()
                        break
                    if your_input == "q":
                        self.admin_view_obj.exit_program()
                    if hasattr(self, teacher_page_data[your_input]):
                        getattr(self, teacher_page_data[your_input])()
                    else:
                        print("\033[1;35m您的输入有误。\033[0m")
            else:
                print("\033[1;35m您的输的账户不存在或者密码错误。\033[0m")
        else:
            print("\033[1;35m您的输入有误。\033[0m")

    def teacher_info(self):
        '''讲师个人信息'''
        print('''\033[1;35m\n讲师个人信息如下:  
        讲师名称：{}
        讲师性别：{}
        讲师年龄：{}
        讲师工资：{}
        讲师电话号码：{}
        \033[0m'''.format(self.teacher_obj.teacher_name, self.teacher_obj.teacher_gender, self.teacher_obj.teacher_age,
                          self.teacher_obj.teacher_salary, self.teacher_obj.teacher_phonenumber))

    def student_list(self):
        '''学生列表'''
        print('当前班级如下：')
        self.grade_obj = self.your_choiseschool_obj.school_grade
        for i in self.grade_obj:
            print("\033[1;34m{}\033[0m".format(i))
        your_input = str(input("\033[1;35m请输入你要查看的班级名: \033[0m").strip())
        if your_input in self.grade_obj:
            self.grade_obj1 = self.grade_obj[your_input]
            print("\033[1;34m\n\n{}班级的学生列表如下: \033[0m".format(your_input))
            for j in self.grade_obj1.grade_student:
                student_obj = self.grade_obj1.grade_student[j]
                print('''\033[1;35m姓名: {}  性别: {}  年龄: {}  缴费状态: {}\033[0m'''.format(student_obj.student_name,
                                                                                     student_obj.student_gender,
                                                                                     student_obj.student_age,
                                                                                     student_obj.paycost_status))
        else:
            print("\033[1;35m您的输入有误。\033[0m")




if __name__ == '__main__':
    m = Mainprogram()
    m.run()