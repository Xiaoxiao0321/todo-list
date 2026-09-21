#命令行待办清单
待办=[]
    # {"序号": 1, "任务":"学习","状态":"未完成"},
    # {"序号": 2, "任务":"读书","状态":"未完成"},

菜单=["添加待办","查看待办","标记完成","删除待办","退出"]
def 查看待办():
    # if "状态"=="已完成":
    #     待办.pop(待办.index({"状态":"已完成"}))
    print("当前待办清单为：")
    for item in 待办:
        print(item["序号"],item["任务"],item["状态"])


def 添加待办():
    任务=input("请输入待办事项：")
    if 待办:
        新序号=max(item["序号"] for item  in 待办)+1
    else:
        新序号=1
    待办.append({"序号":新序号,"任务":任务,"状态":"未完成"})
    print("添加成功！")
    保存待办()

def  删除待办():
    序号=int(input("请输入要删除待办事项的序号"))
    for item in 待办:
        if item["序号"]==序号:
            待办.pop(待办.index(item))
    print("删除成功！")
    保存待办()

def 标记完成():
    序号=int(input("请输入完成事项的序号"))
    for item in 待办:
        if item["序号"]==序号:
            item["状态"]="已完成"
    print("恭喜完成此待办事项！")
    保存待办()

#启动时读取
def 读取待办():
    try:
        with open("C:/Users/38952/Desktop/待办清单.txt","r",encoding="utf-8") as f:
            for line in f:
                序号,任务,状态=line.strip().split(",")
                待办.append({"序号":int(序号),"任务":任务,"状态":状态})
    except FileNotFoundError:
        pass 

#每次操作后保存
def 保存待办():
    with open("C:/Users/38952/Desktop/待办清单.txt", "w", encoding="utf-8") as f:
        for item in 待办:
            f.write(f"{item['序号']},{item['任务']},{item['状态']}\n")


读取待办()
while True:
    print("\n",菜单)
    选择=input("请按照序号1-5选择对应功能:")
    if 选择=="1":
        添加待办()
    elif 选择=="2":
        查看待办()
    elif 选择=="3":
        标记完成()
    elif 选择=="4":
        删除待办()
    elif 选择=="5":
        print("再见！")
        break




