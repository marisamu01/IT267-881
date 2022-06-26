class Student():
    def __init__(self,id:str,name:str,major="IT") -> None:
        self.id = id
        self.name = name
        self.major = major 

    def display_detail(self):
        print(f"ID: {self.id}")
        print(f"NAME: {self.name}")
        print(f"MAJOR: {self.major}")
 
    
    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    jessica = Student('111','jessica','IT')            
    jessica.display_detail()

    john = Student('112','john','MKT')            
    john.display_detail()

    james= Student('113','james',"ACC")            
    james.display_detail()


   
      
      