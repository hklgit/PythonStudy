class Student(object):
    # 把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

    # 这个跟构造器很类似
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Student的一个对象
# stu = Student()

# 注意： 我竟然犯了一个错误，__int__ 然后就是报错：
# TypeError: object() takes no parameters



stu = Student('kerven',20)

print(stu.age)
# print(stu)

# <__main__.Student object at 0x00000000026A8128>



