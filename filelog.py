# coding=utf-8
import os
import re
import traceback
from datetime import datetime

from pip._vendor.distlib.compat import raw_input


# def analy_dir():
#     try:
#         raw_input_dir = raw_input('please input dir_name: ')
#         raw_input_write = raw_input('please input dir_name_write: ')
#         for _file in os.listdir(raw_input_dir):
#             file_read = os.path.join(raw_input_dir,_file)
#             if os.path.isfile(file_read):
#                 print(u'执行日志文件{0}'.format(_file))
#                 analyse_log(file_read,raw_input_write)
#                 print(u'日志文件{0}执行完毕'.format(_file))
#     except Exception as e:
#         traceback.print_exc()

def analyse_log():
    file_log = open('/Users/lipeng/Desktop/hera/pass.txt', 'r')
    file_res = open('/Users/lipeng/Desktop/hera/pass_due.txt','a')
    a = 0
    b=0
    regx_business = re.compile('"serviceregister_id": "[0-9]{0,13}"')
    regex_user = re.compile('[0-9]{8}')
    while True:
        lines = file_log.readlines(100000)
        if lines:
            for line in lines:

                user=u''
                business_partener=u''
                _time =line[21:40]
                print(_time)
                res_business = regx_business.findall(line)
                if len(res_business) > 0:
                    business_partener = res_business[0][23:-1]
                    print(business_partener)
                res_user = regex_user.findall(line)
                if len(res_user) >1:
                    user=res_user[1]
                    print(user)
                b+=1
                time1 = datetime.strptime(_time,'%Y-%m-%d %H:%M:%S')
                if time1>=datetime.strptime('2016-07-29 19:51:00','%Y-%m-%d %H:%M:%S') and time1<=datetime.strptime('2016-08-01 18:11:54','%Y-%m-%d %H:%M:%S'):
                    str_res =_time+','+business_partener +','+user+ u'\n'
                    file_res.writelines(str_res)
                    a += 1
        else:
            break
    print(a)
    print(b)
    file_log.close()
    file_res.close()


analyse_log()
