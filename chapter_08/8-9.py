def show_magicians(magicians):
    print(magicians)

# def make_great(magicians):
#     for magician in magicians:
#         magician = 'The Great ' + magician
#     return magicians
#上述做法仅仅修改了magician的值，但是对于magicians这个列表并未做修改。
#正确做法是1、使用enumerate函数；2、使用ranger对列表进行遍历

def make_great(magicians):
    for index,value in enumerate(magicians):
        magicians[index] = 'The Great ' + magicians[index]
    return magicians

magicians = ['刘谦', 'David Copperfield','Harry Houdini']
show_magicians(make_great(magicians[:]))
show_magicians(magicians)