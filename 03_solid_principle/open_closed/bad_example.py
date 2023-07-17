import math
from typing import Literal

# 従業員の職位
Grade = Literal["junior", "middle", "senior"]


class Employee:
    def __init__(self, name: str, grade: Grade) -> None:
        self.name = name
        self.grade = grade


class BonusCalculator:
    def __init__(self, base: int) -> None:
        self.base = base

    def get_bonus(self, employee: Employee) -> int:
        if employee.grade == "junior":
            return math.floor(self.base * 1.1)
        elif employee.grade == "middle":
            return math.floor(self.base * 1.5)
        elif employee.grade == "senior":
            return math.floor(self.base * 2)


if __name__ == "__main__":
    emp1 = Employee("Yamada", "junior")
    emp2 = Employee("Suzuki", "middle")
    emp3 = Employee("Tanaka", "senior")

    bonus_calculator = BonusCalculator(100)
    print(bonus_calculator.get_bonus(emp1))
    print(bonus_calculator.get_bonus(emp2))
    print(bonus_calculator.get_bonus(emp3))
