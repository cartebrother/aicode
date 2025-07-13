import random

a = 0,0,0,0,0,0

a1,a2,a3,a4,a5,a6 = a

print(f"""a1={a1} ,a2={a2} ,a3={a3} ,a4={a4} ,a5={a5} ,a6={a6}""")

for i in range(1,6001):
    r = random.randint(1,6)
    if r == 1:
        a1 += 1
    elif r == 2:
        a2 += 1
    elif r == 3:
        a3 += 1
    elif r == 4:
        a4 += 1
    elif r == 5:
        a5 += 1
    elif r == 6:
        a6 += 1
    else:
        print("error")
print(f"""a1={a1} ,a2={a2} ,a3={a3} ,a4={a4} ,a5={a5} ,a6={a6}""")

sum = a1+a2+a3+a4+a5+a6
print(f"""sum={sum}""")