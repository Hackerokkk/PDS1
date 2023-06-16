n = 9
bit_string1 = "101011100"
bit_string2 = "010011010"

# Завдання 1: Знаходження значень істинності логічних операцій
p = True
q = False

# Кон'юнкція (AND)
conj = p and q

# Диз'юнкція (OR)
disj = p or q

# Альтернативне "або" (XOR)
xor = p != q

# Імплікація (->)
impl = not p or q

# Еквівалентність (<->)
equiv = (not p or q) and (not q or p)

# Завдання 2: Виконання порозрядних операцій між двома бітовими рядками
num1 = int(bit_string1, 2)
num2 = int(bit_string2, 2)

# Порозрядна операція OR
bit_or = bin(num1 | num2)[2:].zfill(n)

# Порозрядна операція AND
bit_and = bin(num1 & num2)[2:].zfill(n)

# Порозрядна операція XOR
bit_xor = bin(num1 ^ num2)[2:].zfill(n)

# Виведення результатів
print("Значення істинності кон'юнкції:", conj)
print("Значення істинності диз'юнкції:", disj)
print("Значення істинності альтернативного 'або':", xor)
print("Значення істинності імплікації:", impl)
print("Значення істинності еквівалентності:", equiv)
print("Порозрядна операція OR:", bit_or)
print("Порозрядна операція AND:", bit_and)
print("Порозрядна операція XOR:", bit_xor)
