import pytest
from freelancer import Freelancer
from salaried_employee import SalariedEmployee
from salaried_employee_with_bonus import SalariedEmployeeWithBonus
from tech_recruiter import TechRecruiter


@pytest.fixture
def salaried_employee():
    return SalariedEmployee(
        id=1,
        name="Luke Skywalker",
        monthly_salary=70000,
    )


@pytest.fixture
def salaried_employee_with_bonus():
    return SalariedEmployeeWithBonus(
        id=2,
        name="Leia Skywalker",
        bonus=15000,
        monthly_salary=70000,
    )


@pytest.fixture
def tech_recruiter():
    return TechRecruiter(
        id=3,
        name="Han Solo",
        monthly_salary=30000,
        commission=5000,
        recruited_candidates=5,
    )


@pytest.fixture
def freelancer():
    return Freelancer(id=4, name="Chewbacca", rate=500, worked_hours=160)


def test_salaried_employee(salaried_employee):
    assert salaried_employee.salary() == 70000


def test_salaried_employee_can_go_to_conferences(salaried_employee):
    assert salaried_employee.can_go_to_conference()


def test_salaried_employee_with_bonus(salaried_employee_with_bonus):
    assert salaried_employee_with_bonus.salary() == 85000


def test_salaried_employee_can_go_to_conferences(salaried_employee_with_bonus):
    assert salaried_employee_with_bonus.can_go_to_conference()


def test_tech_recruiter(tech_recruiter):
    assert tech_recruiter.salary() == 55000


def test_tech_recruiter_cant_go_to_conferences(tech_recruiter):
    assert not tech_recruiter.can_go_to_conference()


def test_freelancer(freelancer):
    assert freelancer.salary() == 80000


def test_freelancer_cant_go_to_conferences(freelancer):
    assert not freelancer.can_go_to_conference()
