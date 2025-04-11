### src/cat/core/net_ease/dto.py
from pydantic import BaseModel

class SalaryInput(BaseModel):
    gross_salary: float
    number_of_dependents: int

class SalaryOutput(BaseModel):
    gross_salary: float
    insurance: float
    personal_income_tax: float
    net_salary: float
    number_of_dependents: int
