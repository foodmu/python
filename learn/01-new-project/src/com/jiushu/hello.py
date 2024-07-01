# a = 'A'
# print(ord(a))

# a = int(input("请输入被加数："))
# b = int(input("请输入加数："))
# c = a + b
# if c > 10:
#     print(c)
# elif c > 5:
#     print(c+50)
# else:
#     print(c+100)
# sum = 0
# for i in range(101):
#     sum += i
# print('1到100自加等于%d' % sum)
#
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
#
#
# def jie_cheng(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# print('10的阶乘：%d' % jie_cheng(10))


# def add(a=0, b=0, c=0):
#     return a + b + c
#
#
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))


# def add(*args):
#     sum1 = 0
#     for arg in args:
#         sum1 += arg
#     return sum1
#
#
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3))
# print(add(1, 3))
#

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2)
#
# s3 = 10
# print('%s' % s3)
# print(f'{s3}')
# print(type(s3))
#
# list1 = [1, 2, 3, 4]
# list2 = ['hello', 'world', 'apple']
# print(list1)
# print(list2 * 3)
# print(len(list1))
# print(list1[0:3])
# for index in range(len(list2)):  # 获取索引
#     print('%d' % index + ' ' + list2[index])
# for elem in list1:  # 获取元素
#     print(elem)
# for index, elem in enumerate(list2):  # 获取索引和元素
#     print(index, elem)
#
# list1.append(200)  # 列表后加元素
# list1.extend([1, 2])  # 合并列表
# list1.insert(0, 340)  # 指定位置加元素
# print(list1)
#
# if 2 in list1:
#     list1.remove(2)  # 删除元素
# print(list1)
#
# list1.pop(-1)  # 指定位置删除元素
# print(list1)
#
# list1.reverse()
# print(list1)
#
# list1.clear()
# print(list1)

# 字典（Java中的Map）
# person = {'name': '久书', 'age': 21, 'sex': '男'}
# print(person['name'])
# print(person['age'])
# print(person['sex'])
#
# # 通过get(key)获取value
# print(person.get('name'))
# # 如果key不存在返回设定的值
# print(person.get('score', 0))
# # 通过key添加value
# person['score'] = 100
# print(person.get('score', 0))
#
# if 'age' in person:
#     if person['age'] > 7:
#         print('要努力学习哦')
#     else:
#         print('快乐的玩耍吧')
# else:
#     print('年龄查找失败')
#
#
# print(person)
# # 查找后会删除
# print(person.pop('sex'))
# print(person)

list = ['apple', 'banana', 'orange']
set = {['apple', 'banana', 'orange']}
print(set)
