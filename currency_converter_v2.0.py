'''
    作者:zqc
    功能：汇率兑换
    版本：2.0
    汇率计算小程序
'''
#定义汇率常量，常量大写后一般不会在动了。
USD_VS_RMB= 6.77

#定义输入变量
currency_str_value = input('请输入带单位的货币金额：')

#获取货币单位
unit = currency_str_value[-3:]

#分支语句，选择结构，
#pass 占位符，用于占位
if unit == 'CNY':
    #输入的是人民币
    rmb_str_value = currency_str_value[:-3]
    #将字符转换为数字
    rmb_value = eval(rmb_str_value)
    #汇率计算
    usd_value = rmb_value / USD_VS_RMB

    #输出结果
    print("美元(USD)输出金额是：",usd_value)
elif unit == 'USD':
    usd_str_value = currency_str_value[:-3]
    usd_value = eval(usd_str_value)
    #汇率计算
    rmb_value2 = usd_value * USD_VS_RMB

    #输出结果
    print(rmb_value2)

else:
    #其他的情况
    print("该程序版本暂不支持此货币！")