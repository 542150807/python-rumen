sandwich_orders = ['mushrooms','pastrami','extra cheese','pastrami','pastrami','spicy']
finished_sandwiches = []
print('The pastrami is sold out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:  #此章节学习用while进行列表遍历
    sandwich_order = sandwich_orders.pop()
    print('I made your ' + sandwich_order + " sandwich.")
    finished_sandwiches.append(sandwich_order)
print('All sandwich orders are completed: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
