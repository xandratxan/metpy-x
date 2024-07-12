# Script to demonstrate the usage of XrayQuantities class
from metpyx import XrayQuantities

# Initialize an XrayQuantities object
x = XrayQuantities()

# List the operational quantities for x-rays
quantities = x.operational_quantities
print(f'Operational quantities for x-rays:\n{quantities}\n')

# Check if a quantity is an operational quantity for x-rays
print(f'Is H*(10) an operational quantity for x-rays?:\n{x.is_quantity('H*(10)')}\n')
print(f'Is H*(3) an operational quantity for x-rays?:\n{x.is_quantity('H*(3)')}\n')

# Retrieve the irradiation angles for an operational quantity
theta = x.get_irradiation_angles('Hp(0.07, slab)')
print(f'Irradiation angles for Hp(0.07, slab):\n{theta}\n')
print(f'Irradiation angles for H*(0.07):')
try:
    x.get_irradiation_angles('H*(0.07)')
except ValueError as e:
    print(f'{e}\n')
