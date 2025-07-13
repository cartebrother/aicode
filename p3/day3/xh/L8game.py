while True:
    c1 = input("""
    游戏第一关，请选择：
    1. 进攻
    2. 切换地图
    """)

    if c1 == "1":
        print("开始战斗")
    elif c1 == "2":
        print("切换地图")

    c2 = input("""
        下一步，请选择：
        1. 继续第一关
        2. 结束
        3. 进入第二关
        """)

    if c2 == "1":
        continue
    elif c2 == "2":
        print("游戏结束")
        break
    elif c2 == "3":
        print("进入第二关")


    c3 = input("""
        游戏第二关，请选择：
        1. 后退
        2. 回城
        """)

    if c3 == "1":
        print("后退")
    elif c3 == "2":
        print("回城")

    break