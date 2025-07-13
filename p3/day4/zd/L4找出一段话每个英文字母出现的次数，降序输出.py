question = """
例子1：输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
"""

print(question)

input_str = input("请开始你的输入:")

dict = {}

for ch in input_str:
    if ch.isalpha():
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1

#字典排序
dict_sort = sorted(dict,key=dict.get,reverse=True)
for i in dict_sort:
    print(i," = ",dict[i])