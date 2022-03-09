from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r
from json import dumps

db_session.global_init("db/argid.sqlite")
nv = get_navigations()
print(nv)
l = 'left'
r = 'right'
u = 'up'
d = 'down'

def get_naprav(A, B):
    A, B = A - 1, B - 1
    try:
        for i in range(len(nv)):
            result_list = [v for k,v in nv[i].items()]
            for j in result_list:
                if j == result_list[2] and j == A:
                    for z in result_list:
                        if z == result_list[3] and z == B:
                            a = result_list[1]
        return a
    except:
        print('ошибка')

def get_marsh():
    c1 = []
    r = get_routs()

    for i in range(len(r)):
        res_ls = [v for k,v in r[i].items()]
        for j in res_ls:
            if j == res_ls[1]:
                c1.append(j)

    return dumps(c1)

print(get_marsh(),get_naprav(1, 9))