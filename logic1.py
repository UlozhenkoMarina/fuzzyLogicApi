import skfuzzy as fuzzy
import numpy


#fuzzy number and fuzzy logic composition
def fuzzyNumberRelationComposition(A, R):
    if A.size != R.size:
        for i in range(0,R.size-A.size+1):
            A = numpy.concatenate((A,numpy.array([numpy.zeros(R[0].size+1)])))
    result = fuzzy.maxmin_composition(A, R)
    return result


#fuzzy output
def fuzzyOutput(A, B, A1):
    R = fuzzy.relation_min(A,B)
    if A1.size != R.size:
        for i in range(0, R.size - A1.size + 1):
            A1 = numpy.concatenate((A1, numpy.array([numpy.zeros(R[0].size + 1)])))
    result = fuzzy.maxmin_composition(A1,R)
    return result


#fuzzy output system
def fuzzyOutputSystem(A,B,A1):
    R = []
    for i in range(0, int(A.size/A[0].size)):
        R.append(fuzzy.relation_min(A[i],B[i]))
    R = numpy.array(R)
    mx = -100
    R_max = []
    h = []
    count = 0

    for i in range(0,int(R[0].size/R[0][0].size)):
        for j in range (0, int(R[0][0].size)):
            for k in range (0, int(R.size/R[0].size)):
                if mx < R [k][i][j]:
                    mx = R[k][i][j]
            h.append(mx)
            mx = -100
            count +=1
            if len(h) == int(R[0][0].size):
                 R_max.append(h)
                 h = []

    R_max = numpy.array(R_max)
    result = fuzzy.maxmin_composition(A1, R_max)
    return result