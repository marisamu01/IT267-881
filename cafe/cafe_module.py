class Desserts:
    def __init__(self) -> None:
        self.desserts = ['ข้าวเหนียวมะม่วง','ข้าวเหนียวทุกเรียน','ไอศรีม']

    def show_desserts(self):
        return f'Dessarts Menu: {self.desserts}'
        

class Drinks:
    def __init___(self) -> None:
        self.drinks = ['กาแฟ','ชา','น้ำอัดลม','ไวน์']

    def add_drinks(self,new_drink):
        self.drinks.append(new_drink)
    
    def show_drinks(self):
        return f'Drink Menu: {self.drinks}'