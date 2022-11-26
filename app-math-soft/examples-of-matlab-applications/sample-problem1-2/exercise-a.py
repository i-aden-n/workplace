import math as ma

a, b, gamma = 5.3, 6, ma.radians(42)

c = (a**2 + b**2 - 2 * a * b * ma.cos(gamma)) ** 0.5
print('Answer for a:', c)

betta = (c**2 + a**2 - b**2)/(2 * a * c) 
alpha = (b**2 + c**2 - a**2)/(2 * b * c)
betta = round(ma.acos(betta), 3)
alpha = round(ma.acos(alpha), 3)
print(f'Answer for b: alpha = {ma.degrees(alpha)}, betta = {ma.degrees(betta)}')
print(f'Answer for c:', round(ma.degrees(alpha+betta+gamma)))