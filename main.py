from models.employee import (
    Bonus,
    Commission,
    Employee,
    MonthlyContract,
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
        Employee(
            1,
            name="Luke Skywalker",
            contract=MonthlyContract(conference=True, _salary=70000),
        )
    )

    collaborator.append(
        Employee(
            id=2,
            name="Leia Skywalker",
            contract=MonthlyContract(
                conference=True, _salary=70000, bonus=Bonus(15000)
            ),
        )
    )

    collaborator.append(
        Employee(
            id=3,
            name="Han Solo",
            contract=MonthlyContract(
                conference=False, _salary=30000, commission=Commission(5000, 5)
            ),
        )
    )

    collaborator.append(
        Employee(
            id=3,
            name="Han Solo",
            contract=MonthlyContract(
                conference=False, _salary=30000, commission=Commission(5000, 5)
            ),
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
