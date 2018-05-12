from src.final_exam.q_employee.hourly_employee import HourlyEmployee
from src.final_exam.q_employee.salaried_employee import SalariedEmployee

employees = {1: HourlyEmployee(1, 'joe', 10, 80), 2:SalariedEmployee(2, 'Mike', 80000)}

for e in employees.values():
    print(format(e.calculate(), '.2f'))

