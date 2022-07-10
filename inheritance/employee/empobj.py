#IT
from empIT import EmpIT

mike = EmpIT('001','Mike','60000')
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#MKT
from empmkt import EmpMKT

Anna = EmpMKT('002','Anna','35000')
Anna.emp_detail()
Anna._emp_salary()
Anna.emp_detail()
Anna.mkt_salary()

Jess = EmpMKT('003','Jess','45000')
Jess.add_location('Chiang Mai')
Jess.add_commission (35)
Jess.emp_detail()
Jess.mkt_salary()
