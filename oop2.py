class Employee:
    def __init__(self,name,id_,salary,department):
        self.name=name
        self.id_=id_
        self.salary=salary
        self.department=department
        
    def set_department(self,department):
        self.department=department
        
    def print_employee_detail(self):
        return "name: {} , id: {} ,salary: {},department: {}".format(self.name,self.id_,self.salary,self.department)
    
    def calculate_emp_salary(self,salary,hour_week):
        overtime=hour_week-50
        if (hour_week>50):
            self.salary=salary+overtime
        else:
            self.salary=salary
E1=Employee('JONES','E7499',45000,'RESERSH')
E2=Employee('ADAMS','E7876',50000,'ACCOUNTING')

E1.set_department('MATH')
E2.set_department('IT')
print(E1.print_employee_detail())
print(E2.print_employee_detail())
E1.calculate_emp_salary(3000,70)
print(E1.salary)