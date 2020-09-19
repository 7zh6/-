# coding = utf-8

print("【 计算圆柱表面积 】\n")                                                     # 声明
print("欢迎使用由 7仔 编写的Python程序！\n")
print("此程序仅供学习、交流与技术测试！\n\n")

pai = 3.14
Continue_2 = True


def calculate():                                                                   # 创建函数 calculate
    global pai                                                                     # 设置全局变量
    radius = input("\n\n请输入半径：", )
    height = input("请输入高：", )
    continue_1 = 1
    while continue_1 == 1:
        pai = input("请输入π值选项（输入 list 获取选项列表）：", )
        if pai == "list":
            print("\n1,保留π")
            print("2,π取3")
            print("3,π取3.1")
            print("4,π取3.14")
            print("5,π取3.141")
            print("6,π取3.14159\n")
        elif pai == str(1):
            pai = "π"
            continue_1 = 0
        elif pai == str(2):
            pai = 3
            continue_1 = 0
        elif pai == str(3):
            pai = 3.1
            continue_1 = 0
        elif pai == str(4):
            pai = 3.14
            continue_1 = 0
        elif pai == str(5):
            pai = 3.141
            continue_1 = 0
        elif pai == str(6):
            pai = 3.14159
            continue_1 = 0
        else:
            print("选项错误！请重新输入！\n")
    if pai == "π":                                                                                       # 保留π计算
        result = str(2 * float(radius) * float(height) + 2 * float(radius) ** 2) + "π"
        equation = "2π × " + str(radius) + "² + " + "2π × " + str(radius) + " × " + str(height) + " = "
        print("\n\n计算算式为：", equation)
        print("计算结果为：", result)
    else:                                                                                               # 带π计算，最后算π
        result_1 = 2 * float(radius) * float(height) + 2 * float(radius) ** 2
        equation = "2π × " + str(radius) + "² + " + "2π × " + str(radius) + " × " + str(height) + " = " + str(result_1)\
                   + "  " + str(result_1) + " × " + str(pai) + " = "
        result_2 = 2 * pai * float(radius) * float(height) + 2 * pai * float(radius) ** 2
        print("\n\n计算算式为：", equation)
        print("计算结果为：", result_2)


while Continue_2 is True:
    calculate()
    Continue_4 = True
    while Continue_4 is True:
        Continue_3 = input("\n\n是否需要继续计算？是请输入 Y ；否请输入 N ",)
        if Continue_3 == "Y":
            Continue_2 = True
            Continue_4 = False
        elif Continue_3 == "N":
            Continue_2 = False
            Continue_4 = False
            print("欢迎下次使用！（请尽量人工计算~不要用过多次的计算工具哦~）")
        else:
            print("参数错误！请重新输入！")
            Continue_4 = True
