# Pys - script (1.0)

## 一、项目概述
 - **项目名称**：Pys - script (1.0)
 - **创建时间**：2024/12/28
 - **完成时间**：未完成（-/-/-）

## 二、结构
1. **功能根与功能、参数关系**
   - 功能根 :: 功能 参数 参数
   - 功能根 :: 功能 参数 参数 <!receive> 布尔值
   - 功能 参数
2. **功能根详情**
   - **@content**：创建文字区
   - **@set**：设置信息
   - **@input**：输入
   - **@run**：运行
   - ……
3. **功能详情**
   - **#content**：内容
   - **style**：样式（颜色、显示相关）
   - **variable**：变量
   - **run**：运行
   - **send**：发送信息
   - **get**：接收信息
   - ……
4. **参数详情**
   - 1. 数字
   - 2. **auto**：默认值
   - 3. **none**：空白

## 三、程序特色 - 日志法
 - 本程序采用“日志法”。所谓日志法，就是将书写代码格式转换为Jason格式，最后通过程序函数解析Jason脚本，转换为外向显示，这相当于比其他程序语言多了一个日志区。
 - 在这个日志法中，日志包含程序主环境、单脚本区、日志主功能、日志功能及参数，如下方代码展示：

```python
main_1 = "@XXX"
parameter_1 = "XXX XXX XXX => into XXX"
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

# JSON 格式
root = [
    {
        "instruction": {
            "main": {
                "content": "",
            },
            "parameter": {
                "content": "",
            }
        }
    },
    {
        "instruction": {
            "main": {
                "content": "",
            },
            "parameter": {
                "content": "",
            }
        }
    }
]
```