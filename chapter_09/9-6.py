class restaurant():
    """创建一个餐馆"""

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print("The restaurant" + self.name + " is opening")

class icecream(restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = []
    
    def add_flavor(self, flavor):
        self.flavors.append(flavor)  #此处注意直接.append而并非self.flavors = self.flavors.append(flavor)，这样返回的结果是none
        
restaurant_1 = restaurant('KFC','快餐')
print(restaurant_1.name)    #注意此处引用不是类restaurant而是restaurant_1
print(restaurant_1.type)
restaurant_1.open_restaurant()  #使用类中的方法和引用函数一样需要加括号
print("有" + str(restaurant_1.number_served) + "人在这家餐厅就餐过。")
restaurant_1.number_served = 1000
print("有" + str(restaurant_1.number_served) + "人在这家餐厅就餐过。")
icecream_1 = icecream('KFC','快餐')
icecream_1.add_flavor('starwberry')
print(icecream_1.flavors)