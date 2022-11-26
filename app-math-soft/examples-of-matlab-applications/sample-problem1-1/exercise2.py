import math as ma


alpha = ma.pi/6
beta = 3*ma.pi/8

ri = ma.sin(alpha) + ma.sin(beta)
le = 2*ma.sin((alpha + beta)/2)*ma.cos((alpha - beta)/2)

ri = round(ri, 10)
le = round(le, 10)

print(ri)
print(le)
print(ri == le)