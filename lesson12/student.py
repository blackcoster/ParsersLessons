class Student:
    def __init__(self,name, last_name,age,num_class,level):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.num_class = num_class
        self.level = level

    eye_color = ''
    
    def do_homework(self):
        print('я делаю уроки')

    def answer_in_class(self):
        print('Я отвечаю')

student1 = Student('Полина','Крупенина')
student1.do_homework()