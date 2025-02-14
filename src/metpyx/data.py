#: Radiation quality series
SERIES = {
    'L': ['L10', 'L20', 'L30', 'L35', 'L55', 'L70', 'L100', 'L125', 'L170', 'L210', 'L240'],
    'N': ['N10', 'N15', 'N20', 'N25', 'N30', 'N40', 'N60', 'N80', 'N100', 'N120', 'N150', 'N200', 'N250', 'N300',
          'N350', 'N400'],
    'W': ['W30', 'W40', 'W60', 'W80', 'W110', 'W150', 'W200', 'W250', 'W300'],
    'H': ['H10', 'H20', 'H30', 'H40', 'H60', 'H80', 'H100', 'H150', 'H200', 'H250', 'H280', 'H300', 'H350', 'H400']
}
#: Operational quantities
OPERATIONAL_QUANTITIES = ['H_prime(0.07)', 'H_prime(3)', 'H*(10)', 'Hp(0.07, rod)', 'Hp(0.07, pillar)',
                          'Hp(0.07, slab)', 'Hp(3, cyl)', 'Hp(10, slab)']
#: Total filtration thickness for radiation qualities
TOTAL_FILTRATION = {
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
#: Irradiation angles for operational quantities
IRRADIATION_ANGLES = {
    'H_prime(0.07)': [0, 15, 30, 45, 60, 75, 90, 180],  # Table 1
    'H_prime(3)': [0, 15, 30, 45, 60, 75, 90, 180],  # Table 7
    'H*(10)': [0],  # Table 14
    'Hp(0.07, rod)': [0],  # Table 21
    'Hp(0.07, pillar)': [0],  # Table 27
    'Hp(0.07, slab)': [0, 15, 30, 45, 60, 75],  # Table 33
    'Hp(3, cyl)': [0, 15, 30, 45, 60, 75, 90],
    'Hp(10, slab)': [0, 15, 30, 45, 60, 75]
}
