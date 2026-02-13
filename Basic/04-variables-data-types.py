title = "04-變數(variables)與資料型別(data types)"

# 宣告變數
name = "劉家瑋" # string
age = 36 # int(integer)
height = 170.5 # float(floating point number)
weight = 70.5 # float(floating point number)
is_male = True # boolean
print(f"姓名: {name} | {type(name).__name__}")
print(f"年齡: {age} 歲 | {type(age).__name__}")
print(f"身高: {height} | {type(height).__name__}")
print(f"體重: {weight} | {type(weight).__name__}")
print(f"性別: {is_male} | {type(is_male).__name__}")

# 同時賦值多個相同值
a = b = c = 1
print(f"a: {a} | {type(a).__name__}")
print(f"b: {b} | {type(b).__name__}")
print(f"c: {c} | {type(c).__name__}")

# 同時賦值多個不同值
x, y, z = 1, 2, 3
print(f"x: {x} | {type(x).__name__}")
print(f"y: {y} | {type(y).__name__}")
print(f"z: {z} | {type(z).__name__}")
