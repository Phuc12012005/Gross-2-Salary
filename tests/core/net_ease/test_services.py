import pytest
from src.cat.core.net_ease.dto import SalaryInput
from src.cat.core.net_ease.services import NetEaseService


@pytest.mark.parametrize(
    "gross_salary, dependents, expected_insurance, expected_tax, expected_net",
    [
        # Test case 1: Low salary, no dependents — minimal or zero tax
        (8_000_000, 0, round(8_000_000 * 0.105), 0, round(8_000_000 - 8_000_000 * 0.105)),
        
        # Test case 2: Medium salary, 2 dependents
        (20_000_000, 2, round(20_000_000 * 0.105), 0, round(20_000_000 - 20_000_000 * 0.105 - 0)),

        # Test case 3: High salary, 0 dependents
        (50_000_000, 0, round(50_000_000 * 0.105), 5_187_500, round(50_000_000 - 50_000_000 * 0.105 - 5_187_500)),
    ]
)
def test_calculate_salary(gross_salary, dependents, expected_insurance, expected_tax, expected_net):
    service = NetEaseService()
    input_data = SalaryInput(gross_salary=gross_salary, number_of_dependents=dependents)
    result = service.calculate_salary(input_data)

    assert result.gross_salary == gross_salary
    assert result.number_of_dependents == dependents
    assert result.insurance == expected_insurance
    assert result.personal_income_tax == expected_tax
    assert result.net_salary == expected_net