peoples = {
    'Zhixian':{
        'first_name':'Zhixian',
        'last_name':'Cao',
        'age':23,
        'city':'Shanghai',
        },
    'Shaodi':{
        'first_name':'Shaodi',
        'last_name':'Wu',
        'age':22,
        'city':'Hangzhou',
        },
    'Su Yi':{
        'first_name':'Yi',
        'last_name':'Su',
        'age':22,
        'city':'Quanzhou',
        },
    }
for people,people_info in peoples.items():
    print('\nPeople: ' + people)
    fullname = people_info['first_name'] + ' ' + people_info['last_name']
    location = people_info['city']
    print('\tFull name: ' + fullname.title())
    print('\tLocation:' + location)