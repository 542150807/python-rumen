filename = 'chapter_10/10-1.txt'   #或者是在前面加上chapter10，因为默认的文件路径为主目录pcc,或者使用pycharm,默认路径为文件所在文件夹

with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('python', 'C++')
    print(contents.strip())

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('python', 'C++')
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('python', 'C++')
    print(line.strip())