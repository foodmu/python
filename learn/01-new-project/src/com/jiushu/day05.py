"""
  @ClassName day05
  @Description
  @Author 久书
  @Data 2024/6/17 21:25
  @Version 1.0
"""


class Animal:

    def __init__(self, name):
        self.__name__ = name

    def __str__(self):
        return '此动物为：' + self.__name__


dog = Animal('Dog')
print(dog)


