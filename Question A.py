
import random

def is_overlapping(line_A, line_B):

    if line_A[0] > line_B[1]:
        return False

    elif line_A[1] < line_B[0]:
        return False
    
    return True

i = 0
limit = 1500

while i < 100:

    line_A = (random.randint(-limit,limit),random.randint(-limit,limit))

    line_B = (random.randint(-limit,limit),random.randint(-limit,limit))

    if line_A[0] < line_A[1] and line_B[0] < line_B[1]:

        print(f"Line A: {line_A}")
        print(f"Line_B: {line_B}")
        print(f"Lines are overlapping: {is_overlapping(line_A, line_B)}")
        print("----------------------------")
        i+= 1