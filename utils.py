import math
import json

f = open('./data/mars.json')
cos_xk = 0
sin_xk = 0
f_xk = 0
cos2_xk = 0
sin_cos = 0
f_xk_cos = 0
sin2_xk = 0
f_xk_sin = 0
data = json.load(f)

omega = (2*math.pi)/4
print(omega)

for i in range (1, 13):
    cos_xk += math.cos(omega*i)
    sin_xk += math.sin(omega*i)
    sin_cos += math.cos(omega*i) * math.sin(omega*i)
    cos2_xk += (math.cos(omega*i) ** 2)
    sin2_xk += (math.sin(omega*i) ** 2)

j = 1
for value in data:
    f_xk += float(data[value])
    f_xk_cos += (float(data[value]) * math.cos(omega*j))
    f_xk_sin += (float(data[value]) * math.sin(omega*j))
    j += 1

print(cos_xk)
print(sin_xk)
print(f_xk)
print(cos2_xk)
print(sin_cos)
print(f_xk_cos)
print(sin2_xk)
print(f_xk_sin)

f.close()