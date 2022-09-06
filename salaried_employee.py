from dataclasses import dataclass
from enum import Enum
from employee import BaseEmployee


@dataclass
class SalariedEmployee(BaseEmployee):
    monthly_salary: float = 0

    def can_go_to_conference(self):
        return True

    def salary(self):
        # An employee that receives a monthly salary.
        return self.monthly_salary
