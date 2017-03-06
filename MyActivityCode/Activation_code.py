import time
import re
import random
"""
生成密码中前10位为加密的时间戳,后9位采用生成随机数字转ASCII码,若数字大于90,则减去90转成相应的数字.
最后一位为校验相关位,通过计算后9位的ASCII码序号和以及相关数字的相加,使加上最后一位后等于加密的时间戳的最后一位.
最后一位先是数字,后加上65变成相应的字母.
解密:
按照加密的规则解密生成的密码,先获得当前的时间戳,若当前时间戳减去加密的时间戳大于指定时间,则激活码失效.
若解密后,检验和计算不对也出错.
"""

def create_activation_code():
    str_time_stamp = str(int(time.time()))

    split_str_time_stamp = re.findall('\d', str_time_stamp)
    secure_time_stamp = ''
    final_of_time_stamp = split_str_time_stamp[-1]
    sum_of_code = 0
    for each in split_str_time_stamp:
        temp = int(each) + 65
        secure_time_stamp += chr(temp)

    for i in range(9):
        temp_ascii_code = random.randint(65, 99)
        sum_of_code += temp_ascii_code
        if temp_ascii_code > 90:
            secure_time_stamp += str(temp_ascii_code - 90)
        else:
            secure_time_stamp += chr(temp_ascii_code)
    sum_of_code %= 10
    if sum_of_code > int(final_of_time_stamp):
        check_bit = 10 + int(final_of_time_stamp) - sum_of_code
        check_bit %= 10
    elif sum_of_code < final_of_time_stamp:
        check_bit = int(final_of_time_stamp) - sum_of_code
    else:
        check_bit = sum_of_code
    secure_time_stamp += chr(check_bit + 65)
    return secure_time_stamp


def decode_activation_code(ac_code):
    flag = True
    ac_length = len(ac_code)
    time_stamp_for_decode = ''
    sum_of_real_checknum = 0
    for nums in range(10):
        time_stamp_for_decode += str((ord(ac_code[nums])) - 65)
    interval_time = int(time.time()) - int(time_stamp_for_decode)
    # print time_stamp_for_decode
    if interval_time > 30:
        flag = False
        return flag

    for nums in range(10, ac_length - 1):
        # print ac_code[nums],
        if ord(ac_code[nums]) < 65:
            sum_of_real_checknum += (int(ac_code[nums]) + 90)
        else:
            sum_of_real_checknum += ord(ac_code[nums])
    # print sum_of_real_checknum
    sum_of_real_checknum += (ord(ac_code[ac_length - 1]) - 65)
    check_code = sum_of_real_checknum % 10
    # print check_code
    # print int(time_stamp_for_decode[-1])
    if check_code != int(time_stamp_for_decode[-1]):
        flag = False
        return flag
    return flag

if __name__ == '__main__':
    for i in range(5):
        code = create_activation_code()
        print code
    flag = decode_activation_code('BEIIIAJJAINJOL8A3OSD')
    if flag:
        print "Okay."
    else:
        print "Fuck the hell."