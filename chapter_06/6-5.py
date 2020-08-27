rivers = {
    'nile': 'egypt',
    'changjiang': 'China',
    'Danube': 'German',
}
for river,country in rivers.items():  # 后缀items,key,value
    print('The ' + river.title() + ' runs through ' + country.title())