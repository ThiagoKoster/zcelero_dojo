from dataclasses import dataclass
from enum import Enum
from employee import Employee, EmployeeType

""" 
    TODO: 1 - How can we remove duplicated code and split responsabilities?
    TODO: 2 - Implement the ZCelerian Employee: 
        - Receives a monthly base salary
        - Receives a commision for each recruited_candidates
        - Receives a bonus
        - Can go to conferences
"""


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
    """Don't change this method"""

    print("Calculating total cost...")
    total = 0
    for collaborator in get_collaborators():
        total += collaborator.salary()

    print(f"Total cost: {total}")
    return total


if __name__ == "__main__":
    main()
