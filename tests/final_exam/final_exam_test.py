from employee import Employee
from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from motif import non_contiguous_motif
from player import Player


def test_check_come_out_roll_w_8_9(self):
    d1 = 8
    d2 = 9
    self.assertEqual('True', player.calculate)
def test_check_come_out_roll_w_4_7(self):
    d1 = 4
    d2 = 7
    self.assertEqual('Loser', player.calculate)



def test_hourly_employee_w_10_and_80(self):
    hourly_rate = 10
    worked_hours = 80
    self.assertEqual(800,hourly_rate.calculate)
def test_salaried_employee_w_26000_and_10000(self):
    yearly_rate = 26000
    self.assertEqual(10000,salaried_employee.calculate)
def test_non_contiguous_motiff(self):
    values = ['A','C','G','T','A','C','G','T','G','A','C','G']
    self.assertEqual(3,8,10, motif.calculate)
