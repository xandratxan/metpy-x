import pytest

from metpyx.qualities import XrayQualities


class TestXrayQualities:
    def test_constructor(self):
        x = XrayQualities()
        result_series = x.series
        result_l = x.l_series
        result_n = x.n_series
        result_w = x.w_series
        result_h = x.h_series
        expected_series = ['L', 'N', 'W', 'H']
        expected_l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        expected_n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200',
                             'N250', 'N300', 'N350', 'N400']
        expected_w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        expected_h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300',
                             'H350', 'H400']
        assert result_series == expected_series, f'X-rays series, expected {expected_series}, got {result_series}.'
        assert result_l == expected_l_series, f'L series qualities, expected {expected_l_series}, got {result_l}.'
        assert result_n == expected_n_series, f'N series qualities, expected {expected_n_series}, got {result_n}.'
        assert result_w == expected_w_series, f'W series qualities, expected {expected_w_series}, got {result_w}.'
        assert result_h == expected_h_series, f'H series qualities, expected {expected_h_series}, got {result_h}.'

    def test_is_series(self):
        valid = ['L', 'N', 'W', 'H']
        invalid = ['X']
        series = invalid + valid
        expected = [False] * len(invalid) + [True] * len(valid)
        x = XrayQualities()
        for s, e in zip(series, expected):
            assert x.is_series(s) is e, f'{s} series, expected {e}, got {x.is_series(s)}'

    def test_is_quality(self):
        invalid = ['X10', 'L1000']
        l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250',
                    'N300', 'N350', 'N400']
        w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350',
                    'H400']
        x = XrayQualities()
        for quality in invalid:
            assert x.is_quality(quality) is False, f'{quality} quality, expected False, got {x.is_quality(quality)}.'
        for quality in l_series:
            assert x.is_quality(quality) is True, f'{quality} quality, expected True, got {x.is_quality(quality)}.'
        for quality in n_series:
            assert x.is_quality(quality) is True, f'{quality} quality, expected True, got {x.is_quality(quality)}.'
        for quality in w_series:
            assert x.is_quality(quality) is True, f'{quality} quality, expected True, got {x.is_quality(quality)}.'
        for quality in h_series:
            assert x.is_quality(quality) is True, f'{quality} quality, expected True, got {x.is_quality(quality)}.'

    def test_get_series_qualities_valid_series(self):
        series = ['L', 'N', 'W', 'H']
        l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250',
                    'N300', 'N350', 'N400']
        w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350',
                    'H400']
        expected = [l_series, n_series, w_series, h_series]
        x = XrayQualities()
        for s, e in zip(series, expected):
            assert x.get_series_qualities(s) == e, f'{s} series, expected {e}, got {x.get_series_qualities(s)}.'

    def test_get_series_qualities_invalid_series(self):
        x = XrayQualities()
        with pytest.raises(ValueError) as exc_info:
            x.get_series_qualities('X')
        assert f'X is not an x-ray radiation quality series.' in str(exc_info.value)

    def test_get_series_valid_quality(self):
        l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250',
                    'N300', 'N350', 'N400']
        w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350',
                    'H400']
        expected_l_series = ['L'] * len(l_series)
        expected_n_series = ['N'] * len(n_series)
        expected_w_series = ['W'] * len(w_series)
        expected_h_series = ['H'] * len(h_series)
        qualities = l_series + n_series + w_series + h_series
        expected = expected_l_series + expected_n_series + expected_w_series + expected_h_series
        x = XrayQualities()
        for q, e in zip(qualities, expected):
            assert x.get_series(q) == e, f'{q} quality, expected {e} series, got {x.get_series(q)} series.'

    def test_get_series_invalid_quality(self):
        qualities = ['X10', 'L0', 'N0', 'W0', 'H0']
        x = XrayQualities()
        for q in qualities:
            with pytest.raises(ValueError) as exc_info:
                x.get_series(q)
            assert f'{q} is not an x-ray radiation quality.' in str(exc_info.value)

    def test_peak_kilovoltage_valid_quality(self):
        l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250',
                    'N300', 'N350', 'N400']
        w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350',
                    'H400']
        expected_l_series = [10, 20, 30, 35, 55, 70, 100, 125, 170, 210, 240]
        expected_n_series = [10, 15, 20, 25, 30, 40, 60, 80, 100, 120, 150, 200, 250, 300, 350, 400]
        expected_w_series = [30, 40, 60, 80, 110, 150, 200, 250, 300]
        expected_h_series = [10, 20, 30, 40, 60, 80, 100, 150, 200, 250, 280, 300, 350, 400]
        qualities = l_series + n_series + w_series + h_series
        expected = expected_l_series + expected_n_series + expected_w_series + expected_h_series
        x = XrayQualities()
        for q, e in zip(qualities, expected):
            assert x.get_peak_kilovoltage(q) == e, f'{q} quality, expected {e} kV, got {x.get_peak_kilovoltage(q)} kV.'

    def test_peak_kilovoltage_invalid_quality(self):
        qualities = ['X10', 'L0', 'N0', 'W0', 'H0']
        x = XrayQualities()
        for q in qualities:
            with pytest.raises(ValueError) as exc_info:
                x.get_peak_kilovoltage(q)
            assert f'{q} is not an x-ray radiation quality.' in str(exc_info.value)

    def test_get_filtration_thickness_valid_quality(self):
        total_filtration = {
            'L': {
                'L10': {'Be': 1, 'Pb': 0.0, 'Sn': 0, 'Cu': 0.00, 'Al': 0.3},
                'L20': {'Be': 1, 'Pb': 0.0, 'Sn': 0, 'Cu': 0.00, 'Al': 2.0},
                'L30': {'Be': 1, 'Pb': 0.0, 'Sn': 0, 'Cu': 0.18, 'Al': 4.0},
                'L35': {'Be': 0, 'Pb': 0.0, 'Sn': 0, 'Cu': 0.25, 'Al': 4.0},
                'L55': {'Be': 0, 'Pb': 0.0, 'Sn': 0, 'Cu': 1.20, 'Al': 4.0},
                'L70': {'Be': 0, 'Pb': 0.0, 'Sn': 0, 'Cu': 2.50, 'Al': 4.0},
                'L100': {'Be': 0, 'Pb': 0.0, 'Sn': 2, 'Cu': 0.50, 'Al': 4.0},
                'L125': {'Be': 0, 'Pb': 0.0, 'Sn': 4, 'Cu': 1.00, 'Al': 4.0},
                'L170': {'Be': 0, 'Pb': 1.5, 'Sn': 3, 'Cu': 1.00, 'Al': 4.0},
                'L210': {'Be': 0, 'Pb': 3.5, 'Sn': 2, 'Cu': 0.50, 'Al': 4.0},
                'L240': {'Be': 0, 'Pb': 5.5, 'Sn': 2, 'Cu': 0.50, 'Al': 4.0},
            },
            'N': {
                'N10': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.00, 'Al': 0.1},
                'N15': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.00, 'Al': 0.5},
                'N20': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.00, 'Al': 1.0},
                'N25': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.00, 'Al': 2.0},
                'N30': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.00, 'Al': 4.0},
                'N40': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.21, 'Al': 4.0},
                'N60': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.60, 'Al': 4.0},
                'N80': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 2.00, 'Al': 4.0},
                'N100': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 5.00, 'Al': 4.0},
                'N120': {'Be': 0, 'Pb': 0, 'Sn': 1.0, 'Cu': 5.00, 'Al': 4.0},
                'N150': {'Be': 0, 'Pb': 0, 'Sn': 2.5, 'Cu': 0.00, 'Al': 4.0},
                'N200': {'Be': 0, 'Pb': 1, 'Sn': 3.0, 'Cu': 2.00, 'Al': 4.0},
                'N250': {'Be': 0, 'Pb': 3, 'Sn': 2.0, 'Cu': 0.00, 'Al': 4.0},
                'N300': {'Be': 0, 'Pb': 5, 'Sn': 3.0, 'Cu': 0.00, 'Al': 4.0},
                'N350': {'Be': 0, 'Pb': 7, 'Sn': 4.5, 'Cu': 0.00, 'Al': 4.0},
                'N400': {'Be': 0, 'Pb': 10, 'Sn': 6.0, 'Cu': 0.00, 'Al': 4.0},
            },
            'W': {
                'W30': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.0, 'Al': 2},
                'W40': {'Be': 1, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.0, 'Al': 4},
                'W60': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.3, 'Al': 4},
                'W80': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 0.5, 'Al': 4},
                'W110': {'Be': 0, 'Pb': 0, 'Sn': 0.0, 'Cu': 2.0, 'Al': 4},
                'W150': {'Be': 0, 'Pb': 0, 'Sn': 1.0, 'Cu': 0.0, 'Al': 4},
                'W200': {'Be': 0, 'Pb': 0, 'Sn': 2.0, 'Cu': 0.0, 'Al': 4},
                'W250': {'Be': 0, 'Pb': 0, 'Sn': 4.0, 'Cu': 0.0, 'Al': 4},
                'W300': {'Be': 0, 'Pb': 0, 'Sn': 6.5, 'Cu': 0.0, 'Al': 4},
            },
            'H': {
                'H10': {'Be': 1, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 0.00},
                'H20': {'Be': 1, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 0.15},
                'H30': {'Be': 1, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 0.50},
                'H40': {'Be': 1, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 1.00},
                'H60': {'Be': 1, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 3.90},
                'H80': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 0.00, 'Al': 7.20},
                'H100': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 0.15, 'Al': 4.00},
                'H150': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 0.50, 'Al': 4.00},
                'H200': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 1.00, 'Al': 4.00},
                'H250': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 1.60, 'Al': 4.00},
                'H280': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 3.00, 'Al': 4.00},
                'H300': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 2.20, 'Al': 4.00},
                'H350': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 3.40, 'Al': 4.00},
                'H400': {'Be': 0, 'Pb': 0, 'Sn': 0, 'Cu': 4.70, 'Al': 4.00},
            },
        }
        l_series = ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240']
        n_series = ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250',
                    'N300', 'N350', 'N400']
        w_series = ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300']
        h_series = ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350',
                    'H400']
        l_filtration = [total_filtration['L'][q] for q in l_series]
        n_filtration = [total_filtration['N'][q] for q in n_series]
        w_filtration = [total_filtration['W'][q] for q in w_series]
        h_filtration = [total_filtration['H'][q] for q in h_series]
        x = XrayQualities()
        for q, e in zip(l_series, l_filtration):
            assert x.get_filtration_thickness(q) == e, f'{q} quality, expected {e}, got {x.get_filtration_thickness(q)}'
        for q, e in zip(n_series, n_filtration):
            assert x.get_filtration_thickness(q) == e, f'{q} quality, expected {e}, got {x.get_filtration_thickness(q)}'
        for q, e in zip(w_series, w_filtration):
            assert x.get_filtration_thickness(q) == e, f'{q} quality, expected {e}, got {x.get_filtration_thickness(q)}'
        for q, e in zip(h_series, h_filtration):
            assert x.get_filtration_thickness(q) == e, f'{q} quality, expected {e}, got {x.get_filtration_thickness(q)}'

    def test_get_filtration_thickness_invalid_quality(self):
        qualities = ['X10', 'L0', 'N0', 'W0', 'H0']
        x = XrayQualities()
        for q in qualities:
            with pytest.raises(ValueError) as exc_info:
                x.get_filtration_thickness(q)
            assert f'{q} is not an x-ray radiation quality.' in str(exc_info.value)
