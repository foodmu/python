# # 使用元组
# person = ('程茂强', 21, '男')
# for elem in person:
#     print(elem)
# print(person)
# # 元组转化为列表
# person_list = list(person)
# print(person_list)
# person_list[0] = '程久书'
# print(person_list)
# # 列表转化为元组
# person_tuple = tuple(person_list)
# print(person_tuple)

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
print(set2.pop())
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)

set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)

print(set3)
print(set3.pop())  # 移除并返回第一个元素
print(set3)


class Student(object):

    # 构造器
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        if self.age < 5:
            print('开心的玩吧')
        else:
            print('快去学习吧')

    def sleep(self, age):
        if age < self.age:
            print('你应该睡午觉')
        else:
            print('你应该学习')


cmq = Student('程茂强', 11)
cmq.study()
cmq.sleep(10)


class Teacher(object):

    def __init__(self, course):
        self.__course = course

    def teach(self):
        print('老师教的是' + self.__course)

    def get_course(self):
        return self.__course


teacher = Teacher('python')
teacher.teach()
# 高阶函数：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
t = teacher.get_course()
print(t)
print(teacher.get_course())
