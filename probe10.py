
d=dict()
menu = input('메뉴: ')

if menu == '오뎅':
    d={'오뎅':300}
elif menu == '순대':
    d={'순대':400}
elif menu == '만두':
    d={'만두':500}
else:
    d[menu] = 0

print('가격:{0}'.format(d[menu]))
