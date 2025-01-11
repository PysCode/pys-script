# pys script
__A language of the computer__


项目名称：Pys-scipt (1.0)
创建时间：2024/12/28
完成时间：-/-/-

# 结构：

功能根 :: 功能 参数 参数
功能根 :: 功能 参数 参数 <!receive> 布尔值
功能 参数

# 功能根：
@content ：创建文字区
@set ：设置信息
@input ：输入
@run ：运行
……

# 功能：
#content ：内容
style ：样式（颜色，显示）
variable ：变量
run ：运行
send ：发送信息
get ：接收信息
……

# 参数：
1.数字
2.auto ：默认
3.none ：空白

__本程序所用的方式是“日志法”，__
__所谓日志法，即是将书写代码格式改为Jason格式，__
__最后经过程序函数解析Jason脚本，转化为外向显示，__
__相当于比其它的程序语言多了一个日志区。__

__其中，日志是以程序主环境、单脚本区、日志主功能、日志功能及参数，__
__如下方代码展示__

python ‘‘‘
main_1 = "@XXX"
parameter_2 = "XXX XXX XXX => into XXX"

main_2 = "@XXX"
parameter_2 = "XXX XXX XXX => into XXX"

instruction_1 = [
    main_1,
    parameter_1
]

instruction_2 = [
    main_2,
    parameter_2
]

root = [
    instruction_1,
    instruction_2
]

###
root [
    instruction [
        main,
        parameter
    ],
    
    insrtruction [
        main,
        parameter
    ]
]

###

#解析

for instructions in root:
    for 

’’’