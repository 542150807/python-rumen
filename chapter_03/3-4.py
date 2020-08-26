guests = ['刘秀', '李世民', '毛泽东','周恩来','吴绍迪']
for guest in guests:
    print("在下诚挚邀请" + guest + "与我共进晚餐。")

# 3-5
print("由于时间关系，吴绍迪不能参加晚宴。")
guests[-1] = '洪岩'
for i in range(len(guests)):
    print("在下诚挚邀请" + guests[i] + "与我共进晚餐。")

# 3-6
guests.insert(0,'刘邦')
guests.insert(3,'苏毅')
guests.append('wsd')
for i in range(len(guests)):
    print("在下诚挚邀请" + guests[i] + "与我共进晚餐。")

# 3-7
print('很遗憾，由于新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。')
for i in range(len(guests)-1,1,-1):
    print(guests[i] + '，非常抱歉，由于餐桌不够，我无法邀请您前来共进晚餐。')
    guests.pop()
print(guests)
for i in range(len(guests)):
    print(guests[i] + '，您依然在受邀嘉宾之中，恭候您的光临。')
del guests[0]
del guests[0]
print(guests)
