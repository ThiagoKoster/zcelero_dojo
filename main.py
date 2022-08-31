from models.employee import (
    Freelancer,
    SalariedEmployee,
    SalariedEmployeeWithBonus,
    TechRecruiter,
)

""" 
    TODO: 1 - How can we remove duplicated code and split responsabilities?
    TODO: 2 - Implement the ZCelerian Employee: 
        - Receives a monthly base salary
        - Receives a commision for each recruited_candidates
        - Receives a bonus
        - Can go to conferences

    
"""


def get_collaborator():
    """Mocks a database call."""
    collaborator = []
    collaborator.append(
        SalariedEmployee(
            1,
            name="Luke Skywalker",
            monthly_salary=70000,
        )
    )

    collaborator.append(
        SalariedEmployeeWithBonus(
            id=2,
            name="Leia Skywalker",
            bonus=15000,
            monthly_salary=70000,
        )
    )

    collaborator.append(
        TechRecruiter(
            id=3,
            name="Han Solo",
            monthly_salary=30000,
            commission=5000,
            recruited_candidates=5,
        )
    )

    collaborator.append(
        Freelancer(
            id=4,
            name="Chewbacca",
            rate=500,
            worked_hours=160,
        )
    )

    return collaborator


def main():
    print("Calculating total cost...")
    total = 0
    for collaborator in get_collaborator():
        total += collaborator.salary()

    print(f"Total cost: {total}")


if __name__ == "__main__":
    main()
