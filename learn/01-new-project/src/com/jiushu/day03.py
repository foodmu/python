class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # getter方法
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 18:
            print(f'{self._name}正在玩耍')
        else:
            print(f'{self._name}正在学习')


jiu_shu = Person('久书', 20)
jiu_shu.play()
jiu_shu.age = 10
jiu_shu.play()

print(jiu_shu.__eq__(Person))

