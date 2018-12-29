# 一个_代表import禁止导入，但子类和类对象可以访问
# 两个_代表无法在外部直接访问，因为名字重整
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
