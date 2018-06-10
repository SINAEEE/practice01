
d=dict()
menu = input('메뉴: ')

if menu == '오뎅':
    #d={menu:300}
    d[menu]=300
elif menu == '순대':
    #d={menu:400}
    d[menu]=400
elif menu == '만두':
    #d={menu:500}
    d[menu]=500
else:
    d[menu] = 0

print('가격:{0}'.format(d[menu]))

print()

