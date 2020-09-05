from restaurant import restaurant

restaurant_1 = restaurant('KFC','快餐')
print(restaurant_1.name)    #注意此处引用不是类restaurant而是restaurant_1
print(restaurant_1.type)
restaurant_1.open_restaurant()  #使用类中的方法和引用函数一样需要加括号
print("有" + str(restaurant_1.number_served) + "人在这家餐厅就餐过。")
restaurant_1.number_served = 1000
print("有" + str(restaurant_1.number_served) + "人在这家餐厅就餐过。")