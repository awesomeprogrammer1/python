import pytest
from exponent_power import exponent_power


@pytest.mark.parametrize(
    "natural_number, result_exp, result_power",
    [
        (35, 32, 5),
        (129, 128, 7),
        (3, 2, 1),
    ],
)
def test_exponent_power(natural_number: int, result_exp: int, result_power: int):
    assert exponent_power(natural_number) == (result_exp, result_power)