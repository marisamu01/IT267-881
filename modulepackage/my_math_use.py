#วิธีที่ 1
from my_math import sqrt,circle_area
print("****วิธีที่ 1****")
print(f'sqart of 5  = {sqrt(5)}')
print(f'circle area = {circle_area(2):,.2f}')

#วิธีที่ 2
import my_math as my
print("****วิธีที่ 2****")
print(f'sqart of 5  = {sqrt(5)}')
print(f'circle area = {my.circle_area(2):,.2f}')