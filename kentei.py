# 検定統計値は　z = (mean - mue) / (s - sqrt(n))

import math

s = 10
n = 25
mean = 180
mue = 170
# significance_level 有意水準
sig_level = 5


res = (mean - mue) / (s / math.sqrt(n))

z = round(res, 2)

if sig_level == 10:
    if z > -1.65 and z < 1.65:
        result = '採択'
    else :
        result = '棄却'
elif sig_level == 5:
    if z > -1.96 and z < 1.96:
        result = '採択'
    else :
        result = '棄却'
else:
    if z > -2.58 and z < 2.58:
        result = '採択'
    else :
        result = '棄却'

print(f'z = {z}で{result}します')

