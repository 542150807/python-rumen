from random import randint

class Die(): #类的名字大写

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        side_new = randint(1,self.sides)
        print(side_new)

die_1 = Die(6)
for i in range(10):
    die_1.roll_die()

die_1 = Die(10)
for i in range(10):
    die_1.roll_die()

