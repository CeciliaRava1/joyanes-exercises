vehicleCost = 20000
recoveryValue = 2000
yearsElapsed = 0
year = 2005
accumulatedDepreciation = 0

print('***************************************************')
print('Year | Vehicle Real Value | Accumulated Depreciation')

while yearsElapsed <= 6:
    if yearsElapsed == 0:
        accumulatedDepreciation = 0
    else:
        accumulatedDepreciation += int((vehicleCost - recoveryValue) / 6)
    vehicleRealValue = vehicleCost - accumulatedDepreciation
    print(f'{year} | {vehicleRealValue}               | {accumulatedDepreciation}')
    year += 1
    yearsElapsed += 1
