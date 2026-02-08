import random
random.seed(0)

flag = 'FGTE{redacted}'

cipher = []
for ch in flag:
    r = random.randint(32, 127)
    cipher.append(ord(ch) ^ r)

print(cipher)
