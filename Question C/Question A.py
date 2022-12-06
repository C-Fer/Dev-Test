
import random
#function definition
def is_overlapping(line_A, line_B):
    #Cases where there is no overlapping return false
    if line_A[0] > line_B[1]:
        return False

    elif line_A[1] < line_B[0]:
        return False
    
    return True #if overlapping exists it will return true

i = 0 #counter variable

limit = 15 #to generate numbers between -15 and 15

while i < 20: #to generate 20 examples
    #generate random lines between [-15,15]
    line_A = (random.randint(-limit,limit),random.randint(-limit,limit))

    line_B = (random.randint(-limit,limit),random.randint(-limit,limit))

    if line_A[0] < line_A[1] and line_B[0] < line_B[1]:

        print(f"Line A: {line_A}")
        print(f"Line_B: {line_B}")
        print(f"Lines are overlapping: {is_overlapping(line_A, line_B)}")
        print("----------------------------")
        i+= 1
