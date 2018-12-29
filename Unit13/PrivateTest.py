# 一个
class Person(object):

    def __init__(self, id, name):
        self.__id = id
        self._name = name

    def show_id(self):
        print(self.__id)

    def show_name(self):
        print(self._name)


class Student(Person):

    def show_id(self):
        print(self.__id)

    def show_name(self):
        print(self._name)

student = Student(11, 'haha')
student.show_id()
student.show_name()
