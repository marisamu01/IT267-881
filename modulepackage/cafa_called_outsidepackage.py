#1
from cafe_module import Drinks
from cafe_module import Desserts

desserts = Desserts()
print(desserts.show_desserts())

#2
drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drinks('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drinks('น้ำผลไม้')
print(drinks.show_drinks())