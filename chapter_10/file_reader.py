#filename = 'c:/Users/54215/Documents/GitHub/pcc/chapter_10/pi_digits.txt'  # 直接用绝对路径
filename = 'chapter_10/pi_digits.txt'   #或者是在前面加上chapter10，因为默认的文件路径为主目录pcc,或者使用pycharm,默认路径为文件所在文件夹

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
