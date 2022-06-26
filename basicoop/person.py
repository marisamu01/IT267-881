class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
       self.name = name
       self.gender = gender
       self.profession = profession
       self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')
 
    def show(self):
        print(f'Name: {self.name} Gender:{self.gender} profession:{self.profession} study:{self.study}')

    def __del__(self):
        print("object was destroyed")
        
#person1
jessa = Person('Jessa','Female','Software Engineer',0)            
jessa.work()
jessa.show()

#person2
join = Person ('join', 'Male', 'Doctor',15)
join.work()
join.show()

#person3
Lisa = Person ('Lisa','Female','Single',10)
Lisa.work()
Lisa.show()