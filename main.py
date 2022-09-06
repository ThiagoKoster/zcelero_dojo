from dataclasses import dataclass
from enum import Enum
from freelancer import Freelancer
from salaried_employee import SalariedEmployee
from salaried_employee_with_bonus import SalariedEmployeeWithBonus
from tech_recruiter import TechRecruiter

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
        SalariedEmployee(
            1,
            name="Luke Skywalker",
            monthly_salary=70000,
        )
    )

    collaborators.append(
        SalariedEmployeeWithBonus(
            id=2,
            name="Leia Skywalker",
            bonus=15000,
            monthly_salary=70000,
        )
    )

    collaborators.append(
        TechRecruiter(
            id=3,
            name="Han Solo",
            monthly_salary=30000,
            commission=5000,
            recruited_candidates=5,
        )
    )

    collaborators.append(
        Freelancer(
            id=4,
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
