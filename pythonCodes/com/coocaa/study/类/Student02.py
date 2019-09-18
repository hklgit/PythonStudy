
# 我们要限定属性的范围范围。
# 只需要加上__ 注意，这里是两个下划线

class Student02(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def printAttribute(self):
        print('%s: %s' % (self.__name,self.__age))

stu = Student02("kerven",20)

print(stu.name)
# AttributeError: 'Student02' object has no attribute 'name'