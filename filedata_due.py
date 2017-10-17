# coding=utf-8
import json
from datetime import datetime
from operator import itemgetter


def analy_data():
    dict_result = {}
    # raw_input_file = raw_input('please input file_name: ')
    _file = open('/Users/lipeng/Documents/hera1.log', 'r')
    a = 0
    while True:
        lines = _file.readlines(100000)
        if lines:
            for line in lines:
                item_data = line.strip('\n').split(',')
                item_data[0] = datetime.strptime(item_data[0], '%Y-%m-%d %H:%M:%S')
                if item_data[2].strip() != '' and item_data[1].strip() != '':
                    if item_data[1] in dict_result.keys():
                        dict_result[item_data[1]].append(item_data)
                    else:
                        dict_result[item_data[1]] = []
                        dict_result[item_data[1]].append(item_data)
        else:
            break
    for _key, _value in dict_result.items():
        dict_result[_key] = sorted(_value, key=itemgetter(0))

    for _key, _value in dict_result.items():
        business_id = ''
        list_data = dict_result[_key]
        list_data_due = []
        for i in range(0, len(list_data)):
            if list_data[i][2] != business_id:
                business_id = list_data[i][2]
                list_data_due.append(list_data[i])
        dict_result[_key] = sorted(_value, key=itemgetter(0), reverse=True)

    # print dict_result[dict_result.keys()[0]]
    # print dict_result.keys()[0]
    _file.close()
    # print len(dict_result)
    return dict_result


def analy_data_business_doctor():
    """
    获取美购的医生信息

    """
    file_business = open('/Users/lipeng/Documents/business_doctors.txt', 'r')
    dict_business_doctor = json.loads(file_business.read())
    # print len(dict_business_doctor)
    return dict_business_doctor


def due_to_data():
    """
    获取最终数据
    """
    dict_data = analy_data()
    dict_business_doctor = analy_data_business_doctor()
    dict_liuyue = {}
    sum_new=0
    for _key, _value in dict_business_doctor.items():
        sum_new+=len(_value)
        if len(_value) > 0:
            for item in _value:
                dict_liuyue[item] = _key
    print sum_new
    # print len(dicti_wuyue)
    # for _key,_value in dicti_wuyue.items():
    #     print(_key+','+_value)

    # for _key_dict_data ,_value_dict_data in dict_data.items():
    #     for i in range(0,len(_value_dict_data)):
    dict_result_data = {}
    for _key, _value in dict_liuyue.items():
        _businesses = dict_data.get(_key, None)
        if _businesses:
            business_dic = {}
            flag = 6
            for item in _businesses:
                # print item[2]
                m = item[0].month
                if m not in [1, 2, 3, 4, 5]:
                    m = 0
                for i in range(0, flag - m):
                    j = i + 1
                    business_dic[str(flag - j)] = item[2]
                flag = m
            dict_result_data[_key] = business_dic
        else:
            business_dic = {}
            business_dic['2'] = _value
            business_dic['3'] = _value
            business_dic['4'] = _value
            business_dic['5'] = _value
            dict_result_data[_key] = business_dic
    for _key, _value in dict_result_data.items():
        list_key = []
        for item_key, item_value in _value.items():
            list_key.append(int(item_key))
        list_key = sorted(list_key, reverse=True)
        if len(list_key) and list_key[0] != 5:
            for i in range(0, 5 - list_key[0]):
                dict_result_data[_key][str(5 - i)] = dict_result_data[_key][str(list_key[0])]
    dict_data_5 = {}
    dict_data_4 = {}
    dict_data_3 = {}
    dict_data_2 = {}
    for _key, _value in dict_result_data.items():
        data_5 = _value.get('5', None)
        if data_5:
            if data_5 not in dict_data_5.keys():
                dict_data_5[data_5] = []
            dict_data_5[data_5].append(_key)

        data_4 = _value.get('4', None)
        if data_4:
            if data_4 not in dict_data_4.keys():
                dict_data_4[data_4] = []
            dict_data_4[data_4].append(_key)

        data_3 = _value.get('3', None)
        if data_3:
            if data_3 not in dict_data_3.keys():
                dict_data_3[data_3] = []
            dict_data_3[data_3].append(_key)

        data_2 = _value.get('2', None)
        if data_2:
            if data_2 not in dict_data_2.keys():
                dict_data_2[data_2] = []
            dict_data_2[data_2].append(_key)
    _sum_5 = 0
    for _key, _value in dict_data_5.items():
        _sum_5 += len(_value)
        if len(_key)<8:
            print _key
    print _sum_5

    _sum_4 = 0
    for _key, _value in dict_data_4.items():
        _sum_4 += len(_value)
        if len(_key)<8:
            print _key
    print _sum_4

    _sum_3 = 0
    for _key, _value in dict_data_3.items():
        _sum_3 += len(_value)
        if len(_key)<8:
            print _key
    print _sum_3

    _sum_2 = 0
    for _key, _value in dict_data_2.items():
        _sum_2 += len(_value)
        if len(_key)<8:
            print _key
    print _sum_2
    # print len(dict_result_data.keys())
    # print dict_result_data.keys()[0]
    # print dict_result_data[dict_result_data.keys()[0]]
    # txt_5=open('/Users/lipeng/Documents/business_result.txt','w')
    # txt_5.writelines(json.dumps(dict_data_5)+'\n')
    # txt_5.writelines(json.dumps(dict_data_4)+'\n')
    # txt_5.writelines(json.dumps(dict_data_3)+'\n')
    # txt_5.writelines(json.dumps(dict_data_2)+'\n')
    # txt_5.close()
due_to_data()
