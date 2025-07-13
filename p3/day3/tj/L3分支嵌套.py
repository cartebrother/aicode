from id_validator import validator

id_number = input("请输入身份证号码：")
if len(id_number) != 18:
    print("身份证号码长度错误！请重新输入！")
    exit()

#检查和校验身份证号码

if not validator.is_valid(id_number):
    print("身份证号码错误！")
    exit()

sex_number = int(id_number[16]) % 2
if sex_number == 1:
    print("性别：男")
else:
    print("性别：女")


#得到出生年月日
birth_year = int(id_number[6:10])
birth_month = int(id_number[10:12])
birth_day = int(id_number[12:14])
print(f"出生年份：{birth_year} 出生月份：{birth_month} 出生日：{birth_day}")

#计算年龄 当前日期减去出生日期
from datetime import date
now = date.today()
age = now.year - birth_year
if now.month < birth_month or (now.month == birth_month and now.day < birth_day):
    age -= 1


print(f"年龄：{age}")

info = validator.get_info(id_number)
print(f"地址信息：{info}")
address = info['address']
pcs_name = id_number[-4:-2]
print(f"地址：{address},派出所编号：{pcs_name}")


