
f = open('C:\\Users\\Administrator\\Desktop\\hklgithub\\PythonStudy\\pythonCodes\\test.txt')
print(f.read()) #hello python
f.close()


# wan zheng ban

try:
    f = open('C:\\Users\\Administrator\\Desktop\\hklgithub\\PythonStudy\\pythonCodes\\test.txt')
    print(f.read())
finally:
    f.close()
