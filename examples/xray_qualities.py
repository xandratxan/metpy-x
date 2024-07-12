# Script to demonstrate the usage of XrayQualities class
from metpyx import XrayQualities

# Initialize an XrayQualities object
x = XrayQualities()

# List the X-ray radiation quality series
s = x.series
print(f'X-ray radiation quality series:\n{s}\n')

# List the L series radiation qualities
l = x.l_series
print(f'L series radiation qualities:\n{l}\n')

# List the N series radiation qualities
n = x.n_series
print(f'N series radiation qualities:\n{n}\n')

# List the W series radiation qualities
w = x.w_series
print(f'W series radiation qualities:\n{w}\n')

# List the H series radiation qualities
h = x.h_series
print(f'H series radiation qualities:\n{h}\n')

# Check if a series is an x-ray radiation quality series
print(f'Is L an x-ray radiation quality series?:\n{x.is_series('L')}\n')
print(f'Is X an x-ray radiation quality series?:\n{x.is_series('X')}\n')

# Check if a quality is an x-ray radiation quality
print(f'Is L10 an x-ray radiation quality?:\n{x.is_quality('L10')}\n')
print(f'Is L500 an x-ray radiation quality?:\n{x.is_quality('L500')}\n')

# Retrieve the radiation qualities of a radiation quality series
q = x.get_series_qualities('L')
print(f'L series radiation qualities:\n{q}\n')
print(f'X series radiation qualities:')
try:
    x.get_series_qualities('X')
except ValueError as e:
    print(f'{e}\n')

# Retrieve the series from a radiation quality
s = x.get_series('L10')
print(f'L10 quality belongs to series:\n{s}\n')
print(f'L500 quality belongs to series:')
try:
    x.get_series('L500')
except ValueError as e:
    print(f'{e}\n')

# Retrieve the peak kilovoltage from a radiation quality
kvp = x.get_peak_kilovoltage('L10')
print(f'Peak kilovoltage for L10 quality is:\n{kvp} kV\n')
print(f'Peak kilovoltage for L500 quality is:')
try:
    x.get_peak_kilovoltage('L500')
except ValueError as e:
    print(f'{e}\n')

# Retrieve the filtration thickness for a radiation quality
f = x.get_filtration_thickness('L10')
print(f'Filtration thickness for L10 quality is:\n{kvp}\n')
print(f'Filtration thickness for L500 quality is:')
try:
    x.get_filtration_thickness('L500')
except ValueError as e:
    print(f'{e}\n')
