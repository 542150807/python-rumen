sandwich_orders = ['sandwich one','sandwich two','sandwich three']
finished_sandwiches = []
while sandwich_orders:  #此章节学习用while进行列表遍历
    sandwich_order = sandwich_orders.pop()
    print('I made your ' + sandwich_order)
    finished_sandwiches.append(sandwich_order)
print('All sandwich orders are completed: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
