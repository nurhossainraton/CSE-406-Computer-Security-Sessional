import time

from BitVector import BitVector
import random
import math

def generatePrime(bits):
    check = 0
    bv = BitVector(intVal = 0)
    while check < 0.999:
        bv = bv.gen_random_bits(bits)
        check = bv.test_for_primality()
    return bv
def generateX(p):
    random_x = random.randint(1, p)
    return random_x

def generateY(p):
    random_y = random.randint(1, p)
    return random_y
def generateA(p):
    random_a = random.randint(1, p)
    return random_a

def generateE(p):
    e = random.randint(
        math.ceil(p + 1 - 2 * (math.sqrt(p))),
        math.floor(p+ 1 + 2 * (math.sqrt(p)))
    )
    return e

def generateB(x,y,a,p):
    b = (x**3+a*x-y**2)%p
    return b


def generateSforadd(x1, x2,y1, y2,p):
     temp= ((y2-y1)*pow((x2-x1),-1,p.int_val()))%p.int_val()
     return temp


def addingX(x1,x2,y1,y2,p):
    s = generateSforadd(x1,x2,y1,y2,p)
    return (s*s-x1-x2)%p.int_val()

def addingY(x1,x2,y1,y2,p):
    s = generateSforadd(x1,x2,y1,y2,p)
    return (s*(x1-addingX(x1,x2,y1,y2,p))-y1)%p.int_val()


def generateSformul(x1, x2, y1, y2,a,p):
    t= ((3*x1*x1+a)*pow((2*y1),-1,p.int_val()))%p.int_val()
    return t

def doublingX(x1,x2,y1,y2,a,p):
    s=generateSformul(x1,x2,y1,y2,a,p)
    return (s*s - x1 - x2) % p.int_val()
def doublingY(x1,x2,y1,y2,a,p):
    s=generateSformul(x1,x2,y1,y2,a,p)
    return (s * (x1 - doublingX(x1, x2, y1, y2,a,p)) - y1) % p.int_val()

def doubleandadd(d,x,y,a,p):
    t=[x,y].copy()
    point=[x,y]
    binary_representation = bin(d)[2:]

    for i in range(len(binary_representation)-1):
        t[0]=doublingX(t[0],t[0],t[1],t[1],a,p)
        t[1]=doublingY(t[0],t[0],t[1],t[1],a,p)
        if (binary_representation[i+1]=='1'):
            t[0]=addingX(t[0],point[0],t[1],point[1],p)
            t[1]=addingY(t[0],point[0],t[1],point[1],p)
    return t

def double_and_add(base_point, scalar, a,b,p):
    result = None
    binary_scalar = bin(scalar)[2:]
    for bit in binary_scalar:
        result = double_point(result, a,b,p)

        if bit == '1':
            result = add_points(result, base_point, a,b,p)

    return result

def double_point(point, a,b,p):
    if point is None:
        return None

    x, y = point

    s = (3 * x**2 + a) * pow(2 * y, -1, p) % p
    x_result = (s**2 - 2 * x) % p
    y_result = (s * (x - x_result) - y) % p

    return (x_result, y_result)

def add_points(point1, point2, a,b,p):
    if point1 is None:
        return point2
    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if point1 == point2:
        return double_point(point1, a,b,p)
    else:
        s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
        x_result = (s**2 - x1 - x2) % p
        y_result = (s * (x1 - x_result) - y1) % p

        return (x_result, y_result)

def generateKa(e):
    return (random.randint(2, e-1))
def generateKb(e):
    return (random.randint(2, e-1))

def returningvalues(bits):
    p = generatePrime(bits).int_val()
    x = generateX(p)
    y = generateY(p)
    a = generateA(p)
    b = generateB(x, y, a, p)
    e = generateE(p)
    return [p,x,y,a,b,e]

def task2(bits):
    p = generatePrime(bits).int_val()
    x = generateX(p)
    y = generateY(p)
    a = generateA(p)
    e = generateE(p)
    b = generateB(x,y,a,p)


    totA = 0
    totB = 0
    totR = 0
    for i in range(0, 5):
        ka = generateKa(e)
        kb = generateKb(e)
        startA = time.time()
        A = double_and_add((x, y),ka,a,b,p)
        endA = time.time()

        startB = time.time()
        B = double_and_add((x, y),kb,a,b,p)
        endB = time.time()

        startR = time.time()
        R = double_and_add((x,y),ka * kb, a,b,p)
        endR = time.time()

        totA += (endA - startA)
        totB += (endB - startB)
        totR += (endR - startR)

    avgA = totA / 5
    avgB = totB / 5
    avgR = totR / 5

    print(f"For {bits} bits")
    print(f"A {avgA} B {avgB} R {avgR}")

task2(128)
task2(192)
task2(256)


