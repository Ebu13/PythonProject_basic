import sympy as sp

# Sembolik değişkenler tanımlama
x = sp.symbols('x')
y = sp.Function('y')(x)

# Diferansiyel denklemi tanımlama
diff_eq = sp.Eq(y.diff(x), -y ** 2 + (2 * x - 2) * y - x ** 2 + 2 * x + 1)

# Riccati özel çözümü tanımlama
particular_sol = x

# İlk değer koşulunu tanımlama
initial_condition = {y.subs(x, 1): 1}

# Genel çözümü bulma
general_sol = sp.dsolve(diff_eq, y, ics=initial_condition)

# Adımları ekrana yazdırma
print("Diferansiyel Denklem:")
print(diff_eq)
print()

print("Riccati Özel Çözümü:")
print("y(x) =", particular_sol)
print()

print("İlk Değer Koşulu:")
for key, value in initial_condition.items():
    print(f"y({key}) =", value)
print()

print("Genel Çözüm:")
print(general_sol)
