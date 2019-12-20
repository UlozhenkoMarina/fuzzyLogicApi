
def fuzzyNumberRelationComposition(A,R):
    result = []
    mx = 0
    result = composition(R,A)
    return result


def print_in(a):
    for i in range(0,len(a)):
        print(a[i])

def composition(res,A1):
    mx = 0
    result=[]
    for i in range(0, len(res[0])):
        for j in range(0, len(A1)):
            mn = min(A1[j], res[j][i])
            mx = max(mx, mn)
        result.append(mx)
        mx = 0
    return result


def fuzzyOutput(A,B,A1):
    res = []
    result = []
    for i in range(0,len(A1)):
        for j in range(0,len(B)):
            result.append(min(A[i],B[j]))
        res.append(result)
        result=[]
    print_in(res)
    result = composition(res, A1)
    return result

