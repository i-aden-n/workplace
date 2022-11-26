s = 'qwertyuiopassdfghjklzxcvbnm'
print(s[(s.index(input()) + 1) % len(s)])