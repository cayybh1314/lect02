'''
    作者:zqc
    功能：汇率兑换
    版本：1.0
汇率计算小程序
'''

#定义输入变量
rmb_str_value = input('请输入人民币(CNY)金额：')
#将字符串转换成数字
rmb_value = eval(rmb_str_value)
#美元兑人民币的汇率
usd_vs_rmb = 6.77
#汇率计算
usd_value = rmb_value / usd_vs_rmb

print('美元(USD)金额是：',usd_value)