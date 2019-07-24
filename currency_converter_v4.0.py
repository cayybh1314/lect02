'''
    作者:zqc
    功能：汇率兑换
    版本：2.0
    汇率计算小程序
    2.0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    3.0 增加功能：程序可以一直运行，直到用户选择退出
    4.0 增加功能：将汇率兑换功能封装到函数中
'''

def convert_currency(im,er):
    '''
        汇率兑换函数，
        im，er 是参数，定时函数时的形参
    '''
    out = im * er
    return out

#定义汇率常量，常量大写后一般不会在动了。
USD_VS_RMB= 6.77
#定义输入变量
currency_str_value = input('请输入带单位的货币金额:')
#获取货币单位
unit = currency_str_value[-3:]
#分支语句，选择结构，
#pass 占位符，用于占位
if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    im_money = eval(currency_str_value[:-3])
    #调用该函数
    out_money  = convert_currency(im_money,exchange_rate)
    print("转换后的金额:",out_money)

else:
    print("不支持该种货币！")
