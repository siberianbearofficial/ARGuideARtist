from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r

db_session.global_init("db/argid.sqlite")
nv = get_navigations()
print(nv)
l = 'left'
r = 'right'
u = 'up'
d = 'down'

def get_naprav(A, B):
    c = []
    for i in range(len(nv)):
        result_list = [v for k,v in nv[i].items()]
        for j in result_list:
            if j == result_list[1]:
                c.append(j)


    return c

def get_marsh():
    c1 = []
    c2 = []
    r = get_routs()

    for i in range(len(r)):
        res_ls = [v for k,v in r[i].items()]
        for j in res_ls:
            if j == res_ls[1]:
                c1.append(j)
            if j == res_ls[2]:
                c2.append(j)

    return c1, c2

print(get_marsh(),get_naprav())