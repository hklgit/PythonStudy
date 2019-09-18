from io import StringIO

f = StringIO()
f.write("python")

print(f.getvalue())


ff = StringIO("hello \n world \n python")
while True:
    s = ff.readline()
    if s == '':
        break
    print(s.strip())