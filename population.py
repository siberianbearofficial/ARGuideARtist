from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r

db_session.global_init("db/argid.sqlite")
nv = get_navigations()

l = 'left'
r = 'right'
u = 'up'
d = 'down'

for i in range(len(nv)):
    result_list = [v for k,v in nv[i].items()]
    for j in result_list:
        if j == result_list[1]:
            print('--------')
            for _ in j:
                if _ == 'l':
                    print(l)
                if _ == 'r':
                    print(r)
                if _ == 'u':
                    print(u)
                if _ == 'd':
                    print(d)
            print('--------')

