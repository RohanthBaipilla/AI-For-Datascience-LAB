import math
def fuzzify(x, a, b, c, d):
 if x < a:
 return 0
 elif x <= b:
 return (x - a) / (b - a)
 elif x < c:
 return 1
 elif x <= d:
 return (d - x) / (d - c)
 else:
 return 0
def d_b(x, a, b, c, d):
 m = (a + b + c + d) / 2
 return m * fuzzify(x, a, b, c, d)
def d_m(x, a, b, c, d):
 y1 = fuzzify(x, a, b, c, d)
 y2 = fuzzify(x, a, c, d, b)
 return (y1 + y2) / 2
if __name__ == "__main__":
 x = 3
 a = 1
 b = 2
 c = 3
 d = 4
 print("Fuzzified value:", fuzzify(x, a, b, c, d))
 print("Defuzzified value (bisector):", d_b(x, a, b, c, d))
 print("Defuzzified value (mean of greatest):", d_m(x, a, b, c, d))