### src/cat/core/net_ease/services.py
from src.cat.core.net_ease.dto import SalaryInput, SalaryOutput

class NetEaseService:
    def calculate_salary(self, data: SalaryInput) -> SalaryOutput:
        gross = data.gross_salary
        dependents = data.number_of_dependents

        insurance = gross * 0.105

        personal_deduction = 11000000
        dependent_deduction = 4400000 * dependents

        taxable_income = gross - insurance - personal_deduction - dependent_deduction
        taxable_income = max(0, taxable_income)

        brackets = [
            (5000000, 0.05),
            (10000000, 0.10),
            (18000000, 0.15),
            (32000000, 0.20),
            (52000000, 0.25),
            (80000000, 0.30),
            (float("inf"), 0.35),
        ]

        tax = 0
        prev_limit = 0
        for limit, rate in brackets:
            if taxable_income > limit:
                tax += (limit - prev_limit) * rate
                prev_limit = limit
            else:
                tax += (taxable_income - prev_limit) * rate
                break

        net_salary = gross - insurance - tax

        return SalaryOutput(
            gross_salary=gross,
            insurance=round(insurance),
            personal_income_tax=round(tax),
            net_salary=round(net_salary),
            number_of_dependents=dependents
        )