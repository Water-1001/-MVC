"""
员工信息管理系统
MVC---架构------

"""
class Manage_Model:

    def __init__(self, CompanyID=0, name ="", wage=0, eid=0):
        self.CompanyID = CompanyID
        self.name = name
        self.wage = wage
        self.eid = eid

class Manage_View:
    """
    界面视图
    """
    def __init__(self):
        self.controal = Manage_controller(eid =0)

    def display_menu(self):
        print("按1键录入员工信息：")
        print("按2键显示员工信息：")

    def select_menu(self):
        number = input("请输入选项：")
        if number == "1":
            self.method_name()

        if "2" == number:
            self.Print_menu()

    def Print_menu(self):
        for item in self.controal.list_info:
            print("%s员工的编号是%s" % (item.name, item.eid))

    def method_name(self):
        data = Manage_Model()
        data.CompanyID = input("员工部门")
        data.name = input("员工姓名：")
        data.wage = int(input("员工工资"))
        self.controal.Add(data)

class Manage_controller:

    def __init__(self, eid):
        self.eid = 1001      # 实例变量是全局变量
        self.list_info = []  # type：list_info[new]

    def Add(self, new):
        self.eid += 1
        self.list_info.append(new)



view = Manage_View()
while True:
    view.display_menu()
    view.select_menu()







