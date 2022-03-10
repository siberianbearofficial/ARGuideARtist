from data.records import Records
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from data import db_session
from one import get_rec

def sec_exp():
    rec = get_rec()
    exp1 = []
    exp2 = []
    exp3 = []
    exp4 = []
    exp5 = []
    exp6 = []
    exp7 = []
    exp8 = []
    for i in range(len(rec)):
        result_list = [v for k, v in rec[i].items()]
        for j in result_list:
            if j == result_list[2] and j == 1:
                for z in result_list:
                    if z == result_list[3]:
                        exp1.append(z)
            elif j == result_list[2] and j == 2:
                for z in result_list:
                    if z == result_list[3]:
                        exp2.append(z)
            elif j == result_list[2] and j == 3:
                for z in result_list:
                    if z == result_list[3]:
                        exp3.append(z)
            elif j == result_list[2] and j == 4:
                for z in result_list:
                    if z == result_list[3]:
                        exp4.append(z)
            elif j == result_list[2] and j == 5:
                for z in result_list:
                    if z == result_list[3]:
                        exp5.append(z)
            elif j == result_list[2] and j == 6:
                for z in result_list:
                    if z == result_list[3]:
                        exp6.append(z)
            elif j == result_list[2] and j == 7:
                for z in result_list:
                    if z == result_list[3]:
                        exp7.append(z)
            elif j == result_list[2] and j == 8:
                for z in result_list:
                    if z == result_list[3]:
                        exp8.append(z)
    c = {'Exp 1':[max(exp1),min(exp1), sum(exp1)/len(exp1)],
         'Exp 2':[max(exp2),min(exp2), sum(exp2)/len(exp2)],
         'Exp 3':[max(exp3),min(exp3), sum(exp3)/len(exp3)],
         'Exp 4':[max(exp4),min(exp4), sum(exp4)/len(exp4)],
         'Exp 5':[max(exp5),min(exp5), sum(exp5)/len(exp5)],
         'Exp 6':[max(exp6),min(exp6), sum(exp6)/len(exp6)],
         'Exp 7':[max(exp7),min(exp7), sum(exp7)/len(exp7)],
         'Exp 8':[max(exp8),min(exp8), sum(exp8)/len(exp8)]}
    return c

def like_exp():
    rec = get_rec()
    exp1 = []
    exp2 = []
    exp3 = []
    exp4 = []
    exp5 = []
    exp6 = []
    exp7 = []
    exp8 = []
    for i in range(len(rec)):
        result_list = [v for k, v in rec[i].items()]
        for j in result_list:
            if j == result_list[2] and j == 1:
                exp1.append(result_list[4])
                exp1.append(result_list[5])
                exp1.append(result_list[6])
            elif j == result_list[2] and j == 2:
                exp2.append(result_list[4])
                exp2.append(result_list[5])
                exp2.append(result_list[6])
            elif j == result_list[2] and j == 3:
                exp3.append(result_list[4])
                exp3.append(result_list[5])
                exp3.append(result_list[6])
            elif j == result_list[2] and j == 4:
                exp4.append(result_list[4])
                exp4.append(result_list[5])
                exp4.append(result_list[6])
            elif j == result_list[2] and j == 5:
                exp5.append(result_list[4])
                exp5.append(result_list[5])
                exp5.append(result_list[6])
            elif j == result_list[2] and j == 6:
                exp6.append(result_list[4])
                exp6.append(result_list[5])
                exp6.append(result_list[6])
            elif j == result_list[2] and j == 7:
                exp7.append(result_list[4])
                exp7.append(result_list[5])
                exp7.append(result_list[6])
            elif j == result_list[2] and j == 8:
                exp8.append(result_list[4])
                exp8.append(result_list[5])
                exp8.append(result_list[6])

    c = {'Exp 1': (sum(exp1)/len(exp1)),
         'Exp 2': (sum(exp2)/len(exp2)),
         'Exp 3': (sum(exp3)/len(exp3)),
         'Exp 4': (sum(exp4)/len(exp4)),
         'Exp 5': (sum(exp5)/len(exp5)),
         'Exp 6': (sum(exp6)/len(exp6)),
         'Exp 7': (sum(exp7)/len(exp7)),
         'Exp 8': (sum(exp8)/len(exp8))}

    return c

def pos_exp():
    rec = get_rec()
    exp1 = []
    exp2 = []
    exp3 = []
    exp4 = []
    exp5 = []
    exp6 = []
    exp7 = []
    exp8 = []
    for i in range(len(rec)):
        result_list = [v for k, v in rec[i].items()]
        for j in result_list:
            if j == result_list[2] and j == 1:
                for z in result_list:
                    if z == result_list[1]:
                        exp1.append(z)
            elif j == result_list[2] and j == 2:
                for z in result_list:
                    if z == result_list[1]:
                        exp2.append(z)
            elif j == result_list[2] and j == 3:
                for z in result_list:
                    if z == result_list[1]:
                        exp3.append(z)
            elif j == result_list[2] and j == 4:
                for z in result_list:
                    if z == result_list[1]:
                        exp4.append(z)
            elif j == result_list[2] and j == 5:
                for z in result_list:
                    if z == result_list[1]:
                        exp5.append(z)
            elif j == result_list[2] and j == 6:
                for z in result_list:
                    if z == result_list[1]:
                        exp6.append(z)
            elif j == result_list[2] and j == 7:
                for z in result_list:
                    if z == result_list[1]:
                        exp7.append(z)
            elif j == result_list[2] and j == 8:
                for z in result_list:
                    if z == result_list[1]:
                        exp8.append(z)
    c = {'Exp 1': int(len(exp1)),
         'Exp 2': int(len(exp2)),
         'Exp 3': int(len(exp3)),
         'Exp 4': int(len(exp4)),
         'Exp 5': int(len(exp5)),
         'Exp 6': int(len(exp6)),
         'Exp 7': int(len(exp7)),
         'Exp 8': int(len(exp8))}
    print(exp1)

    return c

def pos_zal():
    rec = get_rec()
    exp1 = []
    exp2 = []
    exp3 = []
    exp4 = []
    exp5 = []
    exp6 = []
    exp7 = []
    exp8 = []
    for i in range(len(rec)):
        result_list = [v for k, v in rec[i].items()]
        for j in result_list:
            if j == result_list[2] and j == 1:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp1.append(z)
            elif j == result_list[2] and j == 2:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp2.append(z)
            elif j == result_list[2] and j == 3:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp3.append(z)
            elif j == result_list[2] and j == 4:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp4.append(z)
            elif j == result_list[2] and j == 5:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp5.append(z)
            elif j == result_list[2] and j == 6:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp6.append(z)
            elif j == result_list[2] and j == 7:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp7.append(z)
            elif j == result_list[2] and j == 8:
                for z in result_list:
                    if z == result_list[1] and z[:10] == '2022-03-10':
                        exp8.append(z)

    c = {
        'Room 1': int(len(exp1)+len(exp2)),
        'Room 2': int(len(exp3)+len(exp4)),
        'Room 3': int(len(exp5)+len(exp6)+len(exp7)+len(exp8)),
         }

    return c
