class Item:
    def __init__(self,name:str,price:float,quantity = 1) -> None:
        #ตรวจสอบ price, quantity ว่าต้อง > 0
        assert price > 0,f"price {price} must greater than 0"
        assert quantity > 0,f"Quantity {quantity} must greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    #instance methood ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ meyhood นี้ได้ต้องมีการสร้าง odject
    def total_price(self):
        return self.price*self.quantity
        #self.toal = self.price * self.quantity
        #return self.total

    def __del__(self):
        print("odject was destroyed")

if __name__ == "__main__":
    item1 = Item("Monitor",5600)
    item2 = Item("Monitor",1500,2)
    print("===Total Price ==")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")