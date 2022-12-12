import string

def level01(x):
    # Your code here
    a2z = ''.join([chr(o) for o in range(97, 123)])
    z2a = a2z[::-1]
    
    trans = string.maketrans(a2z, z2a)
    return x.translate(trans)

def level02(x):
    x = sorted(x, reverse=True)
    print("now x --> ", x)
    if not sum(x) % 3:
        return x
    else:
        # from last 
        #if not x[0] % 3:
        #     return [x[0]] + level02(x[1:])
        #else:
        ret = []
        for i in range(len(x)):
            tempL = level02(x[0:i] + x[i+1:])
            if len(tempL) > len(ret) and tempL > ret:
                ret = tempL
        return ret
 
    

def solution02(x):
    # Your code here
    ret = level02(x)
    print("x: " , x, ", ret: ", ret)
    #return sum([pow(10, len(ret)-i-1) * ret[i] for i in range(0, len(ret))])
    

# ----------------------------- test -------------------------------------
# ----------------------------- level 01 -------------------------------------
print(level01("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(level01("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
# ----------------------------- level 02 -------------------------------------
a = [3, 1, 4, 1]
b = [3, 1, 4, 1, 5, 9]
c = [4, 1, 0, 4, 1, 4, 7]
d = [2, 2, 0]
e = [1, 1, 4]
f = [3]
g = [1, 3, 4, 5, 5, 6, 6, 6]
h = [3, 3, 3, 3, 3, 3,1, 1, 0]
i = [1, 1, 2, 2, 2, 2, 2, 2]
#print(solution02(a))
#print(solution02(b))
#print(solution02(c))
#print(solution02(d))
#print(solution02(e))
#print(solution02(f))
#print(solution02(g))

def solution03(x):
    sumOfX = sum(x)
    remain = sumOfX % 3
    if not remain:
        return x
    
    if remain == 1:
        if 1 in x:
            x.remove(1)
            return x
        if 4 in x:
            x.remove(4)
            return x
        if 7 in x:
            x.remove(7)
            return x
        if 2 in x:
            x.remove(2)
            return solution03(x)
        if 5 in x:
            x.remove(5)
            return solution03(x)
        if 8 in x:
            x.remove(8)
            return solution03(x)
    if remain == 2:
        if 2 in x:
            x.remove(2)
            return x
        if 5 in x:
            x.remove(5)
            return x
        if 8 in x:
            x.remove(8)
            return x
        if 1 in x:
            x.remove(1)
            return solution03(x)
        if 4 in x:
            x.remove(4)
            return solution03(x)
        if 7 in x:
            x.remove(7)
            return solution03(x)
            

def leve02_solution(L):
    ret = sorted(solution03(L), reverse=True)
    return sum([pow(10, len(ret)-i-1) * ret[i] for i in range(0, len(ret))])

j = [7,3, 1]
k = [4, 4]
m = [2, 1, 1]

sample = [a, b, c, d, e, f, g, h, i,j,k,m]
for s in sample:
    print("*" * 20)
    print(s)
    ret = solution03(s)
    print(ret, sum(ret))
    print(leve02_solution(s))
