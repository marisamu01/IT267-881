#1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks

from cafe import cafe_module

desserts = Desserts()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drinks('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drinks('น้ำผลไม้')
print(drinks.show_drinks())