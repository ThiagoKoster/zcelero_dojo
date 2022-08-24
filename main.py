from dataclasses import dataclass
from enum import Enum

""" 
    TODO: 1 - How can we remove duplicated code and split responsabilities?
    TODO: 2 - Implement the ZCelerian Employee: 
        - Receives a monthly base salary
        - Receives a commision for each recruited_candidates
        - Receives a bonus
        - Can go to conferences

    
"""


class EmployeeType(Enum):
    SalariedEmployee = 1
    SalariedEmployeeWithBonus = 2
    TechRecruiter = 3
    Freelancer = 4


@dataclass
class Employee:
    id: int
    name: str
    type: EmployeeType
    monthly_salary: float = 0
    bonus: float = 0
    rate: float = 0
    worked_hours: float = 0
    commission: float = 0
    recruited_candidates: float = 0

    def can_go_to_conference(self):
        if (
            self.type == EmployeeType.Freelancer
            or self.type == EmployeeType.TechRecruiter
        ):
            return False

        return True

    def salary(self):
        # An employee that receives a monthly salary.
        if self.type == EmployeeType.SalariedEmployee:
            return self.monthly_salary

        # An employee that receives a monthly salary AND a monthly bonus.
        if self.type == EmployeeType.SalariedEmployeeWithBonus:
            return self.bonus + self.monthly_salary

        # A third party that provide recruiting services. It receices a montlhy salary and a comission per recruited candidate.
        if self.type == EmployeeType.TechRecruiter:
            return self.commission * self.recruited_candidates + self.monthly_salary

        # A third party that is paid per worked hours at a flat rate.
        if self.type == EmployeeType.Freelancer:
            return self.rate * self.worked_hours


def get_collaborators():
    """Mocks a database call."""
    collaborators = []
    collaborators.append(
        Employee(
            1,
            type=EmployeeType.SalariedEmployee,
            name="Luke Skywalker",
            monthly_salary=70000,
        )
    )

    collaborators.append(
        Employee(
            id=2,
            type=EmployeeType.SalariedEmployeeWithBonus,
            name="Leia Skywalker",
            bonus=15000,
            monthly_salary=70000,
        )
    )

    collaborators.append(
        Employee(
            id=3,
            type=EmployeeType.TechRecruiter,
            name="Han Solo",
            monthly_salary=30000,
            commission=5000,
            recruited_candidates=5,
        )
    )

    collaborators.append(
        Employee(
            id=4,
            type=EmployeeType.Freelancer,
            name="Chewbacca",
            rate=500,
            worked_hours=160,
        )
    )

    return collaborators


def main():
    print("Calculating total cost...")
    total = 0
    for collaborator in get_collaborators():
        total += collaborator.salary()

    print(f"Total cost: {total}")


if __name__ == "__main__":
    main()
