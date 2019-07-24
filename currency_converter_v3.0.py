'''
    作者:zqc
    功能：汇率兑换
    版本：2.0
    汇率计算小程序
    2.0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    3.0 增加功能：程序可以一直运行，直到用户选择退出
'''
#定义汇率常量，常量大写后一般不会在动了。
USD_VS_RMB= 6.77
i = 0
#定义输入变量
currency_str_value = input('请输入带单位的货币金额（推出程序请输入Q）：')

#死循环
#
while (currency_str_value != 'Q'):

    # = 一个等于号 是赋值符号，不是数学上的等于号
    i = i + 1

    #循环次数
    print("循环次数",i)

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
        print("人民币(CNY)输出金额是：",rmb_value2)

    else:
        #其他的情况
        print("该程序版本暂不支持此货币！")
    print("-----------------------------------------------------------")
    # 定义输入变量
    currency_str_value = input('请输入带单位的货币金额（推出程序请输入Q）：')


print("程序已退出！")