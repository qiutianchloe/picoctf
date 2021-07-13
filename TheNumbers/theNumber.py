# p = 112 i = 105 c = 99 o = 111
# P = 80  I = 73  C = 67 O = 79
# 80 - 16 = 64
# 112 - 16  = 96

question = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
#This process we get the lowerletter of the flag
def process(num):
    return chr(num+96)

def process2(num):
    return chr(num+64)

result = map(process2, question)
print(''.join(result))

