'''程序名：PYS 程序语言'''

import sys, re
print(sys.version)

'''

项目名称：Pys-scipt (1.0)
创建时间：2024/12/28
完成时间：-/-/-

结构：

功能根 :: 功能 参数 参数
功能根 :: 功能 参数 参数 <!receive> 布尔值
功能 参数

功能根：
@content ：创建文字区
@set ：设置信息
@input ：输入
@run ：运行
……

功能：
content ：内容
style ：样式（颜色，显示）
variable ：变量
run ：运行
send ：发送信息
get ：接收信息
……

指针：
into ：目标

参数：
1.数字
2.auto ：默认
3.none ：空白

本程序所用的方式是“日志法”，
所谓日志法，即是将书写代码格式改为Jason格式，
最后经过程序函数解析Jason脚本，转化为外向显示，
相当于比其它的程序语言多了一个日志区。

其中，日志是以程序主环境、单脚本区、日志主功能、日志功能及参数，
如下方代码展示

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

'''

line = 1

# 创建一个空字典来存储变量
variables = {}

roots = ["@content", "@set", "@input", "@send", "@add"]

root = []

event = ""

def match(text):
    matches = re.findall(r'%([^%]+)%', text)
    if not matches:  # 如果没有匹配项
        return text.replace("\\n", "\n")  # 返回原始文本
    for i in matches:
        return get_variable(i).replace("\\n", "\n")  # 否则返回匹配到的内容

# 添加变量
def add_variable(name, content):
    # 将变量名和内容添加到字典中
    variables[name] = content

# 获取变量
def get_variable(name):
    # 从字典中获取变量内容
    return variables.get(name)

def receive_condition(condition):
    if condition.split(":")[0] == "true":
        if match(condition.split(":")[1]) == match(event):
            return True
        else:
            return False

# 文本函数
def content_function(p, event):
    text = code.split("<!receive>")[0]
    if code.split("<!receive>") == 2:
        receive = code.split("<!receive>")[1]
        if receive_condition(receive):
            print(text)
    else:
        print(text)
    
#设置函数
def set_function(p, event):
    pass

#输入函数
def input_function(p, event):
    pass

def send_function(p, event):
    pass

#报错函数
def error(ErrorReason, ErrorContent):
    print("Traceback (most recent call last):")
    print(f"  {ErrorReason}: name '{ErrorContent}' is not exist")

# 判断主函数区
def judging_main(main, parameter, event):
    # print(main, parameter)
    result = ""
    if main in roots:
        if main == "@content":
            result = content_function(parameter, event)
        if main == "@set":
            result = set_function(parameter, event)
        if main == "@input":
            result = input_function(parameter, event)
        if main == "@send":
            event = send_function(parameter, event)
        if main == "@add":
            key = parameter.split("=")[0] + "="
            name = parameter.split("=")[0].strip()
            content = parameter.replace(key, "")
            add_variable(name, content)
    else:
        if main == "":
            print(error("StructuralError", "MainName"))
        else:
            print(error("NameNotFound", main))
    print()
    return result

# 创建日志
def create_note(code):
    main = ""
    parameter = ""
        
    for num in range(len(code.split("::"))):
        if num == 0:
            main = code.split("::")[num]
        else:
            parameter += code.split("::")[num]
    instruction = [main, parameter]
    root.append(instruction)

# 解包
def unpack(event):
    program_result = ""
    print("\033c[The program starts]\n")
    program_result = ""
    main = ""
    i = ""
    for instructions in root:
        for i in instructions:
            if len(i.split("@")) == 2:
                main = i
            else:
                program_result += str(judging_main(main, i, event))
    print(f"Program result:\n{program_result}\n")
    input("[Process completed - press Enter]")
    print(f"\033c{sys.version}")
    return 1

class Help:
    
    infor = ""
    roots = ["@content", "@set", "@input", "@add"]
    help_dic = {"@content":"Create a content for the window.", "@set":"A setting of the class and the parameter.", "@input":"It can allow the window to recive your information thet you input.", "@add":"Add a variable."}
    
    def __init__(self, information_class):
        
        print() # start
        
        Help.infor = information_class
        
        if len(Help.infor) == 1 and Help.infor[0] == "?":
            print("Help: All Types")
        else:
            if len(Help.infor) != 1:
                j = ""
                for i in Help.infor:
                    j += f" {i}"
                print(f"Help:{j}")
            else:
                print(f"Help: {Help.infor[0]}")
        
        
        for i in Help.infor:
            if i == "?":
                for j in Help.roots:
                    print(f"   |{j}: {Help.help_dic[j]}")
                return    
            for j in Help.infor:
                if i == j:
                    print(f"   |{i}: {Help.help_dic[j]}")
        

if __name__ == "__main__":
    while True:
        code = input(f"{' '*(3 - len(str(line)))}{line}|")
        line += 1
        
        if code == "clear":
            root = []
        
        if code == "exit":
            break
        
        if len(code) > 0 and code.split()[0] == "help":
            HelpProgram = Help(code.split()[1:])
            code = ""
            print()
            
        if code == "run":
            print("\033cRun")
            line = unpack(event)
        else:
            if code.replace(" ", "") != "":
                create_note(code)
        
        print(root)