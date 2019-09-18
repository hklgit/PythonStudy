
# isInstance
# 继承
class Animal(object):
    def run(self):
        print("animal is running ...")

class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
dog.run()

print(type(dog))
print(id(dog))

print(isinstance(dog,Animal))

print(isinstance(dog,(Animal,Cat)))  #true  判断是不是某几个类型里的一个。只要有一个就是成立的