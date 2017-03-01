import math

def print_matrix( matrix ):
    row = ""
    for c in range( len(matrix) ):
        row += "[ "
        for r in range( len(matrix[0]) ):
            row += str( matrix[c][r] )
            row += " "
        row += "]\n"
    print row

def ident( matrix ):
    identity = new_matrix(len(matrix), len(matrix[0]))
    for c in range(len(matrix)):
        for r in range( len(matrix[0]) ):
            if (c==r):
                identity[c][r] = 1
            else:
                identity[c][r] = 0
    return identity

def scalar_mult( matrix, s ):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            matrix[c][r] *= s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    prod = new_matrix(len(m1), len(m2[0]))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                prod[i][j] += m1[i][k] * m2[k][j]
    return prod


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
