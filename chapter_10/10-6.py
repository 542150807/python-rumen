print('请输入两个整数')
while True:
    try:
        a = int(input('输入第一个整数：\n'))
    except ValueError:
        print('请输入数字！\n')
    else:
        try:
            b = input('输入第二个整数：\n')
            b = int(b)
        except ValueError:
            print('请输入数字！\n')
        else:
            print('两个数的和是：' + str(a+b))
    
            

    