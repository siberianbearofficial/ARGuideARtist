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

    c = {'Exp 1': round((sum(exp1)/len(exp1)), 2),
         'Exp 2': round((sum(exp2)/len(exp2)), 2),
         'Exp 3': round((sum(exp3)/len(exp3)), 2),
         'Exp 4': round((sum(exp4)/len(exp4)), 2),
         'Exp 5': round((sum(exp5)/len(exp5)), 2),
         'Exp 6': round((sum(exp6)/len(exp6)), 2),
         'Exp 7': round((sum(exp7)/len(exp7)), 2),
         'Exp 8': round((sum(exp8)/len(exp8)), 2)}

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

def like_exp_sr():
    rec = get_rec()
    exp1_1 = []
    exp1_2 = []
    exp1_3 = []
    exp2_1 = []
    exp2_2 = []
    exp2_3 = []
    exp3_1 = []
    exp3_2 = []
    exp3_3 = []
    exp4_1 = []
    exp4_2 = []
    exp4_3 = []
    exp5_1 = []
    exp5_2 = []
    exp5_3 = []
    exp6_1 = []
    exp6_2 = []
    exp6_3 = []
    exp7_1 = []
    exp7_2 = []
    exp7_3 = []
    exp8_1 = []
    exp8_2 = []
    exp8_3 = []

    for i in range(len(rec)):
        result_list = [v for k, v in rec[i].items()]
        for j in result_list:
            if j == result_list[2] and j == 1:
                exp1_1.append(result_list[4])
                exp1_2.append(result_list[5])
                exp1_3.append(result_list[6])
            elif j == result_list[2] and j == 2:
                exp2_1.append(result_list[4])
                exp2_2.append(result_list[5])
                exp2_3.append(result_list[6])
            elif j == result_list[2] and j == 3:
                exp3_1.append(result_list[4])
                exp3_2.append(result_list[5])
                exp3_3.append(result_list[6])
            elif j == result_list[2] and j == 4:
                exp4_1.append(result_list[4])
                exp4_2.append(result_list[5])
                exp4_3.append(result_list[6])
            elif j == result_list[2] and j == 5:
                exp5_1.append(result_list[4])
                exp5_2.append(result_list[5])
                exp5_3.append(result_list[6])
            elif j == result_list[2] and j == 6:
                exp6_1.append(result_list[4])
                exp6_2.append(result_list[5])
                exp6_3.append(result_list[6])
            elif j == result_list[2] and j == 7:
                exp7_1.append(result_list[4])
                exp7_2.append(result_list[5])
                exp7_3.append(result_list[6])
            elif j == result_list[2] and j == 8:
                exp8_1.append(result_list[4])
                exp8_2.append(result_list[5])
                exp8_3.append(result_list[6])

    c = {'Exp 1': [(sum(exp1_1)/len(exp1_1)), sum(exp1_2)/len(exp1_2), sum(exp1_3)/len(exp1_3)],
         'Exp 2': [(sum(exp2_1)/len(exp2_1)), sum(exp2_2)/len(exp2_2), sum(exp2_3)/len(exp2_3)],
         'Exp 3': [(sum(exp3_1)/len(exp3_1)), sum(exp3_2)/len(exp3_2), sum(exp3_3)/len(exp3_3)],
         'Exp 4': [(sum(exp4_1)/len(exp4_1)), sum(exp4_2)/len(exp4_2), sum(exp4_3)/len(exp4_3)],
         'Exp 5': [(sum(exp5_1)/len(exp5_1)), sum(exp5_2)/len(exp5_2), sum(exp5_3)/len(exp5_3)],
         'Exp 6': [(sum(exp6_1)/len(exp6_1)), sum(exp6_2)/len(exp6_2), sum(exp6_3)/len(exp6_3)],
         'Exp 7': [(sum(exp7_1)/len(exp7_1)), sum(exp7_2)/len(exp7_2), sum(exp7_3)/len(exp7_3)],
         'Exp 8': [(sum(exp8_1)/len(exp8_1)), sum(exp8_2)/len(exp8_2), sum(exp8_3)/len(exp8_3)]}

    return c