class Person:
    def __init__(self,name,age,sex):
        self._name = name  #加下划线的意思代表属性是私有的不允许访问
        self._age = age
        self._sex = sex
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age


s=Person('yyj',29,'man')
print(s.get_age())

class Student(Person):
    pass

p = Student('lili','29','woman')

print(p.get_name())