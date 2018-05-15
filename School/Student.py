class Student:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print('My name is %s and come from %s' %(name,city))
    def talk(self):
        print('Hello EveryOne')

#stu1=Student('jack','BeiJing')
#stu1.talk()