from cusorder import customer,order
from modulepackage.cusorder.customer import Customer
from modulepackage.cusorder.order import Order

cus = customer,Customer( "Jame","Nontaburi")
ord = order,Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} on {order.date} is {order.status}')