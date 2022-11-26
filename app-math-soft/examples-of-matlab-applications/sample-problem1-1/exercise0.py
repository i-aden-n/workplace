import math as ma

x = ma.pi / 5

ri = ma.cos(x/2)**2
le = (ma.tan(x) + ma.sin(x))/(ma.tan(x)*2)

ri = round(ri, 10)
le = round(le, 10)

print(ri)
print(le)
print(ri == le)