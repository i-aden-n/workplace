import math as ma


x = ma.radians(24) 

# a
ri = ma.tan(x*3)
le = ((ma.tan(x)*3)-(ma.tan(x)**3))/(1-3*ma.tan(x)**2)

ri = round(ri, 10)
le = round(le, 10)

print('a')
print(ri)
print(le)
print(ri == le)

# b
ri = ma.cos(4*x)
le = 8*(ma.cos(x)**4 - ma.cos(x)**2) + 1

ri = round(ri, 10)
le = round(le, 10)

print('\nb')
print(ri)
print(le)
print(ri == le)