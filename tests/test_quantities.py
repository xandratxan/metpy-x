import pytest

from metpyx.quantities import XrayQuantities


class TestXrayQuantities:
    def test_constructor(self):
        x = XrayQuantities()
        result = x.operational_quantities
        expected = ['H_prime(0.07)', 'H_prime(3)', 'H*(10)', 'Hp(0.07, rod)', 'Hp(0.07, pillar)', 'Hp(0.07, slab)',
                    'Hp(3, cyl)', 'Hp(10, slab)']
        assert result == expected, f'Operational quantities, expected {expected}, got {result}.'

    def test_is_quantity_valid_quantity(self):
        quantities = ['H_prime(0.07)', 'H_prime(3)', 'H*(10)', 'Hp(0.07, rod)', 'Hp(0.07, pillar)', 'Hp(0.07, slab)',
                      'Hp(3, cyl)', 'Hp(10, slab)']
        expected = [True] * len(quantities)
        x = XrayQuantities()
        for q, e in zip(quantities, expected):
            assert x.is_quantity(q) is e, f'{q} quantity, expected {e}, got {x.is_quantity(q)}.'

    def test_is_quantity_invalid_quantity(self):
        quantities = ['H', 'Hprime(0.07)', 'H_prime(0.3)', 'H*(0.07)', 'Hp(0.07, rad)', 'Hp(0.7, pillar)',
                      'H_p(0.07, slab)', 'Hp(0.07, cyl)', 'Hp(10, salb)']
        expected = [False] * len(quantities)
        x = XrayQuantities()
        for q, e in zip(quantities, expected):
            assert x.is_quantity(q) is e, f'{q} quantity, expected {e}, got {x.is_quantity(q)}.'

    def test_get_irradiation_angles_valid_quantity(self):
        angles = {
            'H_prime(0.07)': [0, 15, 30, 45, 60, 75, 90, 180],  # Table 1
            'H_prime(3)': [0, 15, 30, 45, 60, 75, 90, 180],  # Table 7
            'H*(10)': [0],  # Table 14
            'Hp(0.07, rod)': [0],  # Table 21
            'Hp(0.07, pillar)': [0],  # Table 27
            'Hp(0.07, slab)': [0, 15, 30, 45, 60, 75],  # Table 33
            'Hp(3, cyl)': [0, 15, 30, 45, 60, 75, 90],
            'Hp(10, slab)': [0, 15, 30, 45, 60, 75]
        }
        quantities = list(angles.keys())
        expected = [angles[q] for q in quantities]
        x = XrayQuantities()
        for q, e in zip(quantities, expected):
            assert x.get_irradiation_angles(q) == e, f'{q} quantity, expected {e}, got {x.get_irradiation_angles(q)}.'

    def test_get_irradiation_angles_invalid_quantity(self):
        x = XrayQuantities()
        with pytest.raises(ValueError) as exc_info:
            x.get_irradiation_angles('H')
        assert f'H is not an x-ray operational quantity.' in str(exc_info.value)
