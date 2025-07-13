# 打印到7结束
import math

for i in range(1,20):
    if i > 7:
        break
    print("数字：",i)


# 打印 1-100的圆的面积,找到第一个面积大于200的半径

for r in range(1,101):
    area = math.pi * r * r
    if area > 200:
        print("第一个面积大于200的半径为：",r)
        print("半径为：", r, "的圆的面积为：", area)
        break
