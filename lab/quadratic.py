a, b, c = map(int, input().split())

d = ((b**2)-4*a*c)

if a==b==c==0:
    print(-1)
elif a==b==0:
    print(0)
elif a==0:
    print(1)
    print((c/b)*(-1))
elif d==0:
    print(1)
    print(b/(2*a))
elif d > 0:
    print(2)
    print(((b*(-1))-d**0.5)/(2*a))
    print(((b*(-1))+d**0.5)/(2*a))