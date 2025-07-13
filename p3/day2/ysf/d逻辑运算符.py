yu = 150
shu = 130

r1 = (yu ==150 and shu ==150)

if r1:
    print("拿到奖品A")
else:
    print("没拿到奖品A")



r2 = (yu ==150 or shu ==150)
if r2:
    print("拿到奖品B")
else:
    print("没拿到奖品B")


age = 20

hire = ( 20 <= age <=35)

print(hire)
