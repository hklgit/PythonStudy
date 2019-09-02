def  test01():
    print("*"*10)



test01()
print(id(test01()))


a = 100
def f1():
    global a
    print(a)
    a = 300

f1()
print(a)

print(locals())
print(globals())