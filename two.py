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
    c = {'Exp 1':'Max: ' + str(max(exp1)) + '   Min: ' + str(min(exp1)) + '  Sr: ' + str(sum(exp1)/len(exp1)),
         'Exp 2':'Max: ' + str(max(exp2)) + '   Min: ' + str(min(exp2)) + '  Sr: ' + str(sum(exp2)/len(exp2)),
         'Exp 3':'Max: ' + str(max(exp3)) + '   Min: ' + str(min(exp3)) + '  Sr: ' + str(sum(exp3)/len(exp3)),
         'Exp 4':'Max: ' + str(max(exp4)) + '   Min: ' + str(min(exp4)) + '  Sr: ' + str(sum(exp4)/len(exp4)),
         'Exp 5':'Max: ' + str(max(exp5)) + '   Min: ' + str(min(exp5)) + '  Sr: ' + str(sum(exp5)/len(exp5)),
         'Exp 6':'Max: ' + str(max(exp6)) + '   Min: ' + str(min(exp6)) + '  Sr: ' + str(sum(exp6)/len(exp6)),
         'Exp 7':'Max: ' + str(max(exp7)) + '   Min: ' + str(min(exp7)) + '  Sr: ' + str(sum(exp7)/len(exp7)),
         'Exp 8':'Max: ' + str(max(exp8)) + '   Min: ' + str(min(exp8)) + '  Sr: ' + str(sum(exp8)/len(exp8))}
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

    c = {'Exp 1': 'Sr: ' + str(sum(exp1)/len(exp1)),
         'Exp 2': 'Sr: ' + str(sum(exp2)/len(exp2)),
         'Exp 3': 'Sr: ' + str(sum(exp3)/len(exp3)),
         'Exp 4': 'Sr: ' + str(sum(exp4)/len(exp4)),
         'Exp 5': 'Sr: ' + str(sum(exp5)/len(exp5)),
         'Exp 6': 'Sr: ' + str(sum(exp6)/len(exp6)),
         'Exp 7': 'Sr: ' + str(sum(exp7)/len(exp7)),
         'Exp 8': 'Sr: ' + str(sum(exp8)/len(exp8))}

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

    return c

def pos_zal():
    pass