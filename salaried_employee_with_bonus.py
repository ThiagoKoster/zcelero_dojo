from dataclasses import dataclass
from enum import Enum
from employee import BaseEmployee


@dataclass
class SalariedEmployeeWithBonus(BaseEmployee):
    monthly_salary: float = 0
    bonus: float = 0

    def can_go_to_conference(self):
        return True

    def salary(self):
        return self.monthly_salary + self.bonus
