from socketserver import TCPServer


class Person(object):

    # __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name


jiu_shu = Person('jiu_shu', 21)
print(jiu_shu.name)
jiu_shu._gander = '男'
print(jiu_shu._gander)


class Student(Person):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self._gender = gender


# 多继承
class JiuShu(Student, TCPServer):
    pass
