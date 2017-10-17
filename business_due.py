# coding=utf-8
import json


def analy_data():
    file_data = open('/Users/lipeng/Documents/hera1_list.log','r')
    file_business = open('/Users/lipeng/Documents/business_doctors.txt','r')
    dict_business_doctor=json.loads(file_business.read())
    print len(dict_business_doctor)
    print dict_business_doctor
    dict_doctor_business={}
    while True:
        lines=file_data.readlines(10000)
        if lines:
            for line in lines:
                item_data = line.split(':')
                print item_data[1]
        else:
            break

analy_data()