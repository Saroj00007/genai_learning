import math
def dot_product(a, b):
    total = 0

    for x,y in zip(a, b):
        total += x*y

    print(total)
    return total

def magnitude(vector):
    total = 0

    for value in vector :
        total  += value**2
    
    print(math.sqrt(total))
    return math.sqrt(total)


def cosine_similariyt(a , b):

    dotproduct = dot_product(a , b)

    magnitudeA =magnitude(a) 
    magnitudeB = magnitude(b)

    return ((dotproduct) / (magnitudeA * magnitudeB))


x= [-2,-2]
y= [2,2]


print(cosine_similariyt(x  ,y))